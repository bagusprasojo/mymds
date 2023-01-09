from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from store.models import Product, MyColor
from accounts.models import UserProfile
from orders.models import Order

# Create your views here.
def my_products(request):
    products = Product.objects.filter(user=request.user).order_by('-created_date')

    context = {
        'products':products
    }
    return render(request, 'designer/my_products.html', context)

def dashboard_designer(request):
    userprofile = get_object_or_404(UserProfile, user=request.user)

    orders = Order.objects.order_by('-created_at').filter(user=request.user, is_ordered=True)
    order_count = orders.count()
    context = {
        'order_count':order_count,
        'userprofile':userprofile,
    }
    return render(request, 'designer/dashboard_designer.html', context)


@login_required(login_url = 'login')
def add_product(request):

    if request.method == 'POST':
        # user_form = UserForm(request.POST, instance=request.user)
        # profile_form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        #
        # if user_form.is_valid() and profile_form.is_valid():
        #     user_form.save()
        #     profile_form.save()
        #
        #     messages.success(request, "Your profiles have been updated")
        #     return redirect('edit_profile')
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()

        # product = Product()
        # product.product_name = request.POST['product_name']
        # product.product_description = request.POST['product_description']
        # product.image = request.POST['image']
        #
        # print(product.product_name)
        # print(product.product_description)
        # print(product.image)

    else:
        product_form = ProductForm()

    colors = MyColor.objects.all()
    print(colors)
    context = {
        'product_form':product_form,
        'colors':colors,
    }

    return render(request, 'designer/add_product.html', context)
