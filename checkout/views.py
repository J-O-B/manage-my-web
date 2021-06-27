from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, HttpResponse)
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.conf import settings
from .forms import OrderForm
from products.models import Product
from profiles.models import UserProfile
from .models import OrderLineItem, Order
from django.utils.safestring import mark_safe
from cart.contexts import cart_contents
from django.contrib.auth.models import User
from dateutil.relativedelta import relativedelta
from datetime import datetime, date
from contact.models import EmailMarketing

import stripe
import json


currentDate = date.today()


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        cart = request.session.get('cart', {})
        current_cart = cart_contents(request)
        if current_cart['subscription']:
            subscription = True
        else:
            subscription = False

        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(cart),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
            'subscription': subscription,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def mockingPubKey():
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    return stripe_public_key


def mockingSecKey():
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    return stripe_secret_key


def checkout(request):
    """
    The checkout view to handle the page, its variables,
    as well as provide inputs to users that can be handed to
    stripe for payment processing.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    today = datetime.now()
    next_year = today + relativedelta(years=1)

    if request.method == "POST":
        cart = request.session.get('cart', {})
        current_cart = cart_contents(request)

        try:
            number = 0
            number = number + int(EmailMarketing.objects.count())
            try:
                listings = EmailMarketing.objects.filter(email=request.POST.get('email'))
            except Exception:
                listings = False
            if not listings:
                if number >= 1:
                    id = number + 1
                else:
                    id = 1
                list = EmailMarketing(
                    id,
                    email=request.POST.get('email'),
                    users_name=request.POST.get('full_name'),
                    category="Prev Buyer")
                list.save()
        except Exception:
            pass

        if current_cart['subscription']:
            subscription = True
            subscriber = "Yes"
        else:
            subscription = False
            subscriber = "No"

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
        }
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            # Processing Order
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.subscriber = subscriber
            order.subscription = subscription
            user = request.user
            if str(user) != "AnonymousUser":
                try:
                    # Check For Current User Profile
                    order.user_profile = UserProfile.objects.get(
                        user=user.id)
                except Exception:
                    # Create Profile If It Doesn't Exist
                    user_profile = UserProfile.objects.create(user=user)
                finally:
                    # Add the order to the new profile if just created
                    order.user_profile = UserProfile.objects.get(
                        user=user.id)
            order.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                            subscription=subscription,
                        )
                        product.sold = product.sold + item_data
                        product.available = product.available - item_data
                        product.save()
                        order_line_item.save()
                    else:
                        for quantity in item_data.items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                subscription=subscription,
                            )
                            product.sold = product.sold + quantity
                            product.available = product.available - quantity
                            product.save()
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
            request.session['subscription'] = subscription

            # Add Credentials to Profile:
            if request.session['save_info']:
                try:
                    old_profile = UserProfile.objects.get(
                        user=user.id)
                except Exception:
                    old_profile = UserProfile.objects.create(user=user)

            return redirect(reverse(
                'checkout_success', args=[order.order_number]))
        else:
            messages.error(request, mark_safe("There was an error with your form.<br/> \
                Please check all your information is correct."))
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There's nothing in your cart \
                at the moment")
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        if current_cart['subscription']:
            subscription = True
            expiry = str(next_year)
        else:
            subscription = False
            expiry = str(today)
        date = str(today)
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key

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
                    "name": username,
                    "email": email,
                    "date": date,
                    "expiry": expiry,
                    "subscription": str(subscription),
                    "grand_total": total,
                }
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
    subscription = request.session.get('subscription')
    user = request.user
    if user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=user)

        except Exception:
            user_profile = UserProfile.objects.create(user=user)

    order = get_object_or_404(Order, order_number=order_number)
    updated = False
    if save_info:
        user_profile.full_name = order.full_name
        user_profile.email = order.email
        user_profile.phone_number = order.phone_number
        user_profile.country = order.country
        user_profile.postcode = order.postcode
        user_profile.town_or_city = order.town_or_city
        user_profile.street_address1 = order.street_address1
        user_profile.street_address2 = order.street_address2
        updated = True
    if subscription and user.is_authenticated:
        try:
            line_items = OrderLineItem.objects.get(order_number=order_number)
            current_expiry = user_profile.subscription_expiry
            for item in line_items:
                if item.subscription:
                    years = item.quantity
                    new_expiry = currentDate + relativedelta(years=years)
                    if new_expiry > current_expiry:
                        user_profile.subscription_expiry = new_expiry
                else:
                    pass
        except:
            # catch any errors
            pass
        updated = True
    
    if updated:
        user_profile.save()

    messages.success(request, mark_safe(f'<strong>Order Successfully Processed!</strong><br><br> \
        <small>Your order number is: <br><em>{order_number}\
            </em></small>.<br><br>A confirmation email will be\
                sent to {order.email}.<br><br> \
                    <strong>Thank You.</strong>'))

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        "order": order,
        "save_info": save_info,
        "subscription": subscription,
    }
    return render(request, template, context)


def checkout_receipt(request, order_number):
    """
    Deliver a webpage that can be easily printed.
    """
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_receipt.html'
    context = {
        "order": order,
    }
    return render(request, template, context)
