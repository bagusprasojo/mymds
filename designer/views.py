from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProductForm
from store.models import Product, MyColor, Variation, BaseProductGalery
from accounts.models import UserProfile
from orders.models import Order
from django.urls import reverse

# Create your views here.
def my_products(request):
    products = Product.objects.filter(user=request.user).order_by('-created_date')

    context = {
        'products':products
    }
    return render(request, 'designer/my_products.html', context)

def dashboard_designer(request):
    userprofile = get_object_or_404(UserProfile, user=request.user)

    products = Product.objects.order_by('-created_date').filter(user=request.user)
    product_count = products.count()
    context = {
        'product_count':product_count,
        'userprofile':userprofile,
    }
    return render(request, 'designer/dashboard_designer.html', context)


def save_variations(product, variations, colors):
    if variations:
        for variation in variations:
            variation.delete()

            
    for color in colors:
        variation = Variation()
        variation.product = product
        variation.variation_category = 'color'
        variation.variation_value = color
        variation.is_active = True
        variation.save()

@login_required(login_url = 'login')
def delete_product(request, product_id):
    single_product = Product.objects.get(id = product_id )
    single_product.delete()

    products = Product.objects.filter(user=request.user).order_by('-created_date')

    context = {
        'products':products
    }
    
    return render(request, 'designer/my_products.html', context)


@login_required(login_url = 'login')
def edit_product(request, product_slug):
    single_product = Product.objects.get(slug = product_slug )
    product_form = ProductForm(instance=single_product)
    
    colors = MyColor.objects.all()
    context = {
        'product_form':product_form,
        'colors':colors,
        'product_id':single_product.id,
    }

    return render(request, 'designer/add_product.html', context)
    

@login_required(login_url = 'login')
def add_product(request, product_id):
    if request.method == 'POST':

        if product_id:
            old_product = get_object_or_404(Product, id=product_id)
            product_form = ProductForm(request.POST, request.FILES, instance=old_product)
        else:
            product_form = ProductForm(request.POST, request.FILES)

        image = product_form['image'].value()
        if product_form.is_valid() and image:
            product_saved = product_form.save()
            product_saved.user = request.user;
            product_saved = product_saved.save()

            variations = Variation.objects.filter(product = product_saved, variation_category='color')
            colors = request.POST.getlist('colors')
            save_variations(product_saved, variations, colors)
            # if variations:
            #     for variation in variations:
            #         variation.delete()

            # colors = request.POST.getlist('colors')
            # for color in colors:
            #     variation = Variation()
            #     variation.product = product_saved
            #     variation.variation_category = 'color'
            #     variation.variation_value = color
            #     variation.is_active = True
            #     variation.save()


            product_form = ProductForm()
            messages.success(request, "Your product has been saved")
        else:       
            if not image:
                messages.error(request, "Image can not be empty")
            else:     
                messages.error(request, product_form.errors)

    else:
        product_form = ProductForm()

    colors = MyColor.objects.all()
    context = {
        'product_form':product_form,
        'colors':colors,
        'product_id':0,
    }

    return render(request, 'designer/add_product.html', context)
