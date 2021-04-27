from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from products.models import Product
from .models import OrderLineItem, Order
from cart.contexts import cart_contents
from django.contrib.auth.models import User
from dateutil.relativedelta import relativedelta

import stripe
from datetime import datetime


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    today = datetime.now()
    next_year = today + relativedelta(years=1)

    if request.method == "POST":
        cart = request.session.get('cart', {})
        current_cart = cart_contents(request)
        if current_cart['subscription']:
            subscription = True
            expiry = next_year
        else:
            subscription = False
            expiry = today

        form_data = {
            "full_name": request.POST['full_name'],
            "email": request.POST['email'],
            "phone_number": request.POST['phone_number'],
            "country": request.POST['country'],
            "postcode": request.POST['postcode'],
            "town_or_city": request.POST['town_or_city'],
            "street_address1": request.POST['street_address1'],
            "street_address2": request.POST['street_address2'],
            "subscription": subscription,
            "expiry": expiry,
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        if subscription:
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=item_data,
                                subscription=subscription,
                                expiry=expiry,
                            )
                        order_line_item.save()
                    else:
                        for subscription, quantity in (item_data['subscription'].items()):
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                            )
                        if subscription:
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                subscription=subscription,
                                expiry=expiry,
                            )
                            order_line_item.save()
                        else:
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart wasn't found \
                            in our database."
                        "Please contact us for assistance.")
                    )
                    order.delete()
                    return redirect(reverse('cart'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_number]))
        else:
            messages.error(request, "There was an error with your form. \
                Please check all your information is correct.")
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There's nothing in your cart \
                at the moment")
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key

        if current_cart['subscription']:
            today = datetime.now()
            end_subscription = today + relativedelta(years=1)
        else:
            today = datetime.now()
            end_subscription = today
        if User:
            username = None
            email = None
            try:
                username = request.user.username
                email = request.user.email
            except Exception:
                username = "Unknown"
                email = "Unknown"
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
                metadata={
                    "user": username,
                    "email": email,
                    "purchase": f'Purchase: {today}, \
                        Expiry: {end_subscription}'
                    },
                receipt_email=email,
            )
        else:
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Please check the environment!')

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle All Successful Checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}. \
        Thank You.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        "order": order,
        "save_info": save_info,
    }
    return render(request, template, context)
