from django.shortcuts import render, redirect


def view_cart(request):
    """ A view to render a users shopping cart """
    title = "Shopping Cart"
    
    template = 'cart/cart.html'
    context = {
        'title': title,
    }
    return render(request, template, context)


def add_to_cart(request, item_id):
    """ Add a quantity of the specific product to the cart """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
    
    request.session['cart'] = cart
    return redirect(redirect_url)
