from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from carts.models import CartItem
import datetime
from .forms import OrderForm
from .models import Order, Payment, OrderProduct
from store.models import Product
import json
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Create your views here.
def payments(request):
    body = json.loads(request.body)
    print(body)

    order = Order.objects.get(user = request.user, is_ordered=False, order_number=body['orderID'])

    payment = Payment(
        user = request.user,
        payment_id = body['transID'],
        payment_method = body['payment_method'],
        amount_paid = order.order_total,
        status = body['status']
    )

    payment.save()
    order.is_ordered = True
    order.payment = payment
    order.save()

    # move the cart to Order Product Table
    cart_items = CartItem.objects.filter(user = request.user)
    for item in cart_items:
        order_product = OrderProduct(user=request.user, order=order, payment=payment)
        order_product.product = item.product
        order_product.quantity = item.quantity
        order_product.product_price = item.product.price
        order_product.ordered = True
        order_product.save()

        cart_item = CartItem.objects.get(pk=item.id)
        product_variations = cart_item.variations.all()
        order_product = OrderProduct.objects.get(pk=order_product.id)
        order_product.variations.set(product_variations)
        order_product.save()

        # Reduce the quantity of the sold product
        product = Product.objects.get(pk=item.product.id)
        product.stock -= item.quantity
        product.save()

    #clear the cart
    cart_items.delete()

    # send email to customer
    mail_subject = 'Thank you for your order(s)'
    message = render_to_string('orders/order_rceived_email.html', {
        'user': request.user,
        'order':order,
    })

    to_email = request.user.email
    send_email = EmailMessage(mail_subject, message, to=[to_email])
    send_email.send()

    # send order number and transaction to sendData() / json response

    data = {
        'order_number':order.order_number,
        'transID': payment.payment_id
    }

    # Store transaction inside payment model

    return JsonResponse(data)

def place_order(request, total=0, quantity=0,):
    current_user = request.user

    #if no cart redirect to shop
    cart_items = CartItem.objects.filter(user = current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('store')

    grand_total = 0
    tax = 0

    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity  += cart_item.quantity

    tax = (2 * total)/100
    grand_total = total + tax

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            data = Order()

            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.city = form.cleaned_data['city']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.order_note = form.cleaned_data['order_note']

            data.order_total = grand_total
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            # generate order number
            yr = int(datetime.date.today().strftime('%Y'))
            mt = int(datetime.date.today().strftime('%m'))
            dt = int(datetime.date.today().strftime('%d'))
            d = datetime.date(yr,mt,dt)
            current_date = d.strftime('%Y%m%d')

            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

            order = Order.objects.get(user=current_user, order_number=order_number, is_ordered=False)
            context = {
                'order': order,
                'cart_items': cart_items,
                'total': total,
                'tax': tax,
                'grand_total': grand_total
            }

            return render(request, 'orders/payments.html', context)
        else:
            return HttpResponse('NOT VALID')
    else:
        return redirect('checkout')

def paypal(request):
    return render(request, "orders/paypal.html")

def order_complete(request):
    order_number = request.GET.get('order_number')
    print(order_number)
    payment_id = request.GET.get('payment_id')

    try:
        order = Order.objects.get(order_number = order_number)
        order_products = OrderProduct.objects.filter(order = order)

        sub_total = 0
        for item in order_products:
            sub_total += item.product_price * item.quantity

        payment = Payment.objects.get(payment_id = payment_id)

        context = {
            'order' : order,
            'order_products':order_products,
            'payment':payment,
            'sub_total':sub_total,
        }

        return render(request, "orders/order_complete.html", context)
    except (Payment.DoesNotExist, Order.DoesNotExist):
        return redirect('home')
