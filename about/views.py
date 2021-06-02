from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import json


def about(request):
    return render(request, 'about/about.html')
