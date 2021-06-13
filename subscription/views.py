from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, HttpResponse)
from django.contrib import messages
from django.core.mail import send_mail


def Subscription(request):
    return render(request, 'subscription/subscription.html')


def Gold(request):

    if request.method == "POST":
        name = request.POST.get("txtName")
        email = request.POST.get("txtEmail")
        number = request.POST.get("txtPhone")
        message = request.POST.get("txtMsg")

        send_mail(
            f'Gold Subscription: Name: {name}, Tel: {number}',
            message,
            email,
            ['jonathanobrien@outlook.ie'],
            fail_silently=False,
        )

        if len(name) > 1:
            messages.success(request, "Thank you for contacting us.\
                Your message has been sent and we will respond to \
                    you as soon as possible. Have a nice day!")
        else:
            messages.error(request, "There seems to be an error with your form, \
                please try again or contact us via email: \
                    Admin@ManageMyWeb.org")

    return render(request, 'subscription/gold.html')


def Silver(request):
    if request.method == "POST":
        name = request.POST.get("txtName")
        email = request.POST.get("txtEmail")
        number = request.POST.get("txtPhone")
        message = request.POST.get("txtMsg")

        send_mail(
            f'Silver Subscription: Name: {name}, Tel: {number}',
            message,
            email,
            ['jonathanobrien@outlook.ie'],
            fail_silently=False,
        )

        if len(name) > 1:
            messages.success(request, "Thank you for contacting us.\
                Your message has been sent and we will respond to \
                    you as soon as possible. Have a nice day!")
        else:
            messages.error(request, "There seems to be an error with your form, \
                please try again or contact us via email: \
                    Admin@ManageMyWeb.org")
    return render(request, 'subscription/silver.html')
