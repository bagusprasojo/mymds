from django.shortcuts import render
from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('-created_date')
    # print(products)

    # for x in products:
        # print(x.product_name)

    context = {
        'products' : products
    }
    return render(request, 'home.html', context)
