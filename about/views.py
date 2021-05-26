from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import json


def about(request):
    return render(request, 'about/about.html')


@csrf_exempt
def chatbotHook(request, data):
    data = json.loads(data)
    try:
        email_subject = str(data["subject"])
        client_name = str(data["name"])
        client_email = str(data["email"])
    except Exception:
        pass
    # now send an email to admin with request to contact client

    if client_email:
        send_mail(
            email_subject,
            f'A user called {client_name} just requested info via the chatbot. \
              Direct a reply to {client_email}',
            client_email,
            ['jonathanobrien@outlook.ie'],
            fail_silently=False,
        )
    return render(request, 'about/about.html')
