from django.shortcuts import render
from .chatbot import talk


def chat(request):
    message = ""
    response = ""
    if request.method == "POST":
        message = request.POST.get('inmessage')
        response = talk(message)

    template = 'chatbot/chatbot.html'
    context = {
        'chat': chat,
        'response': response,
    }
    return render(request, template, context)
