from django.shortcuts import render, get_object_or_404
from .models import UserProfile, create_or_update_user_profile
from datetime import datetime
from django.contrib import messages
from .forms import UserProfileForm
from checkout.models import Order, OrderLineItem
from products.models import Product


import json

today = datetime.today()


def after_login(request):
    user = request.user
    template = "profiles/after-login.html"
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        profile = False
    if profile:
        messages.success(
            request, f'Welcome back {profile.full_name}.')
    else:
        messages.info(
            request, 'Welcome back {user}. It seems like your profile is incomplete, please \
                update your profile when possible.')
    context = {
        "profile": profile,
        "user": user,
    }
    return render(request, template, context)


def user_profile(request):
    """
    Display a user profile
    """
    user = request.user
    profile = UserProfile.objects.get(user=user)
    orders = ""
    price = 0
    try:
        orders = Order.objects.filter(user_profile=profile)
        line_items = []
        for order in orders:
            line_items += OrderLineItem.objects.filter(order=order.id)

        for i in line_items:
            price = price + i.lineitem_total

    except Exception:
        messages.error(request, "Error retreiving orders, or you have no order history")

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
                    product.rating = product.rating_total / product.rating_count
                    product.save()
                    line.rating = int(rating)
                    line.save()
                else:
                    print('failed')
        except Exception:
            pass

    form = UserProfileForm
    template = 'profiles/user_profile.html'
    context = {
        "profile": profile,
        "form": form,
        "price": price,
        "user": user,
        "orders": orders,
        "line_items": line_items,
    }
    return render(request, template, context)
