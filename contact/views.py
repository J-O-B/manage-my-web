from django.shortcuts import render
from .models import LeadGen
from datetime import date
from django.contrib import messages
from django.core.mail import send_mail

today = date.today()


def contact(request):
    if request.method == "POST":
        subject = request.POST.get('subject_data')
        full_name = request.POST.get('full_name_data')
        email = request.POST.get('email_data')
        message = request.POST.get('message_data')
        date = today


        send_mail(
            f'{subject}',
            f'{full_name} has asked: {message}. Date: {date}',
            f'{email}',
            ['jonathanmichaelobrien@gmail.com'],
            fail_silently=False,
        )

        number = 0
        number = number + int(LeadGen.objects.count())
        if number >= 1:
            id = number + 1
        else:
            id = 1

        try:
            lead = LeadGen(id, full_name, email, subject, message, date)

            lead.save()
            messages.success(request,
                             "Thank you, your message has been sent.")

        except Exception as e:
            messages.error(request,
                           f"An error occurred with the following:{e}")

    template = "contact/contact.html"
    return render(request, template)
