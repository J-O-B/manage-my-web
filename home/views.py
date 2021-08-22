from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.core.mail import send_mail


def Index(request):
    return render(request, 'home/index.html')


@require_POST
def ChatBotHook(request):
    if request.method == "POST":
        try:
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
            send_mail(
                'Chat Message',
                f'{message}, from: {first_name} {last_name}, phone: {phone}',
                f'{email}',
                ['jonathanmichaelobrien@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, response)
        except Exception as e:
            message.error(request, f'Error: {e}')

    return redirect('home')
