from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product


def view_cart(request):
    """ A view to render a users shopping cart """
    title = "Shopping Cart"

    template = 'cart/cart.html'
    context = {
        'title': title,
    }
    return render(request, template, context)


def adjust_cart(request, item_id):
    """ Adjust the contents of a users cart items """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} Quantity To {cart[item_id]}')

    else:
        cart.pop(item_id)
        messages.success(request, f'Removed "{product.name}" From Your Cart.')

    request.session['cart'] = cart
    return redirect(reverse('cart'))


def remove_from_cart(request, item_id):
    """ Remove Specific Cart Items """

    try:
        product = get_object_or_404(Product, pk=item_id)

        cart = request.session.get('cart', {})

        cart.pop(item_id)
        messages.success(request, f'Removed "{product.name}" From Your Cart.')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error Removing Item: {e}')
        return HttpResponse(status=500)


def add_to_cart(request, item_id):
    """ Add a quantity of the specific product to the cart """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    try:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} Quantity To {cart[item_id]}')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} To Your Cart.')
    except Exception as e:
        messages.error(request, f'{e}')
    request.session['cart'] = cart
    return redirect(redirect_url)
