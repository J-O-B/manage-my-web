from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json


def about(request):
    return render(request, 'about/about.html')


@csrf_exempt
def chatbotHook(request, data):
    data = json.loads(data)
    email_subject = data["subject"]
    client_name = data["name"]
    client_email = data["email"]
    # now send an email to admin with request to contact client
    return render(request, 'about/about.html')
