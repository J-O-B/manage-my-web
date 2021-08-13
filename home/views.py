from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST


def Index(request):
    return render(request, 'home/index.html')


@require_POST
def ChatBotHook(request):
    if request.method == "POST":
        first_name = request.POST.get('fnameChat')
        last_name = request.POST.get('lnameChat')
        email = request.POST.get('emailChat')
        phone = request.POST.get('phoneChat')
        message = request.POST.get('messageChat')

        response = (
            f"Thank You {first_name}, \
                We will respond to your request in the coming days on: \
                {email} \
                    Thank You."
        )
        messages.success(request, response)

    return redirect('home')
