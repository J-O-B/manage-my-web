from django.shortcuts import render


def view_cart(request):
    """ A view to render a users shopping cart """
    title = "Shopping Cart"
    
    template = 'cart/cart.html'
    context = {
        'title': title,
    }
    return render(request, template, context)