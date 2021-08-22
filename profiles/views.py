from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from datetime import date
from django.contrib import messages
from .forms import UserProfileForm
from checkout.models import Order, OrderLineItem
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.conf import settings
from dateutil.relativedelta import relativedelta
from datetime import datetime

today = date.today()
currentDate = datetime.now()


@login_required
def after_login(request):
    user = request.user
    template = "profiles/after-login.html"
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        profile = False
    if profile:
        if profile.full_name:
            messages.success(
                request, f'Welcome back {profile.full_name}.')
        else:
            messages.success(
                request, 'Welcome back!')
    else:
        messages.info(
            request, 'Welcome back {user}. It seems like your profile is incomplete, please \
                update your profile when possible.')
    context = {
        "profile": profile,
        "user": user,
    }
    return render(request, template, context)


@login_required
def user_profile(request):
    """
    Display a user profile
    """
    user = request.user

    # Catch users with no profile, create one if needed
    try:
        profile = UserProfile.objects.get(user=user)
    except Exception:
        profile = UserProfile.objects.create(user=user)
    orders = False
    price = 0
    form = UserProfileForm(instance=profile)
    tax = settings.TAX_RATE
    try:
        orders = Order.objects.filter(user_profile=profile)

    except Exception:
        orders = False
        messages.error(request, "Error retreiving orders, \
        or you have no order history")

    line_items = []
    websites = []
    if orders:
        for order in orders:
            line_items += OrderLineItem.objects.filter(order=order.id)
            for i in line_items:
                """
                Feedback and update userprofile for subscriptions
                """
                if i.subscription:
                    profile.subscription = True
                    # Get the latest date then update
                    quantity = i.quantity
                    expiry = today + relativedelta(years=quantity)
                    if profile.subscription_expiry:
                        if expiry > profile.subscription_expiry:
                            profile.subscription_expiry = expiry
                        else:
                            pass
                    else:
                        profile.subscription_expiry = expiry
                profile.save()

                price = price + i.lineitem_total
                A = str(i.product.category)
                if (A == "business" or A == "personal" or A == "ecommerce"):
                    websites.append(i)
    if request.method == "POST":
        try:
            rating = request.POST.get('ratingForm')
            productID = request.POST.get('productID')
            orderID = request.POST.get('orderID')
            print(rating)
            print(productID)
            print(orderID)
            for line in line_items:
                if int(productID) == int(line.product.id):
                    product = get_object_or_404(Product, pk=int(productID))
                    product.rating_count = product.rating_count + 1
                    product.rating_total = product.rating_total + int(rating)
                    product.rating = (
                        product.rating_total / product.rating_count)
                    # product.expiry = today
                    product.save()
                    line.rating = int(rating)
                    line.save()
                else:
                    print('failed')
        except Exception:
            pass

        try:
            form = UserProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile Updated Successfully")
            else:
                messages.error(
                    request, "Update failed. Please ensure the form is valid")

        except Exception:
            pass

    if orders:
        no_orders = True
    else:
        no_orders = False
    template = 'profiles/user_profile.html'
    context = {
        "profile": profile,
        "form": form,
        "price": price,
        "user": user,
        "orders": orders,
        "no_orders": no_orders,
        "tax": tax,
        "line_items": line_items,
        "websites": websites,
    }
    return render(request, template, context)
