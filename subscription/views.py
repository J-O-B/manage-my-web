from django.shortcuts import render


def Subscription(request):
    return render(request, 'subscription/subscription.html')


def Gold(request):
    return render(request, 'subscription/gold.html')


def Silver(request):
    return render(request, 'subscription/silver.html')