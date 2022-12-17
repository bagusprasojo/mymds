from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ReviewRating
from category.models import Category
from carts.views import _cart_id
from carts.models import CartItem
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from .forms import ReviewForm
from django.contrib import messages, auth

# Create your views here.
def store(request, category_slug = None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories,is_available=True).order_by('product_name')
    else:
        products = Product.objects.all().filter(is_available=True).order_by('product_name')


    paginator = Paginator(products,6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    product_count = products.count()

    context = {
        'products' : paged_products,
        'product_count' : product_count,

    }

    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug = product_slug )
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request), product = single_product).exists()
        reviews = ReviewRating.objects.filter(product = single_product)
    except Exception as e:
        raise e

    context = {
        'single_product':single_product,
        'in_cart':in_cart,
        'reviews':reviews
    }

    return render(request, 'store/product_detail.html', context)

def search(request):
    # keyword = ''
    # products = Product.objects.filter(product_description__icontains='keywXXord').order_by('-created_date')

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']

    if keyword:
        products = Product.objects.filter(Q(product_description__icontains=keyword) | Q(product_name__icontains=keyword)).order_by('-created_date')
        print('as')

    context = {
        'products':products,
        'product_count':products.count(),
    }

    return render(request, 'store/store.html', context)

def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')

    try:
        product = Product.objects.get(pk = product_id)

        if request.method == 'POST':
            form = ReviewForm(request.POST)
            try:
                review = ReviewRating.objects.get(user = request.user, product = product)
                pesan= 'Thankyou ! Your review has been updated'
            except ReviewRating.DoesNotExist:
                review = ReviewRating()
                pesan = 'Thankyou ! Your review has been saved'

            if form.is_valid():
                review.subject = form.cleaned_data['subject']
                review.rating = form.cleaned_data['rating']
                review.review = form.cleaned_data['review']
                review.ip = request.META.get('REMOTE_ADDR')
                review.product = product
                review.user = request.user

                review.save()

    except Product.DoesNotExist:
        pesan = 'Product not found'

    messages.success(request, pesan)
    return redirect(url)
