from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    products = Product.objects.all()

    template = 'products/products.html'
    context = {
        'products': products,
    }
    return render(request, template, context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    template = 'products/product_detail.html'
    context = {
        'product': product,
    }
    return render(request, template, context)