from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):
    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You Didn't Enter Any Search Criteria.")
                return redirect(reverse('products'))
            
            queries = (
                Q(name__icontains=query) | Q(description__icontains=query))
            products = products.filter(queries)

    template = 'products/products.html'
    context = {
        'products': products,
        'search_term': query
    }
    return render(request, template, context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    template = 'products/product_detail.html'
    context = {
        'product': product,
    }
    return render(request, template, context)