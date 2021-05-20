from django.shortcuts import render
from django.http import JsonResponse


def chat(request):
    """ A view to render the chatbot application """

    template = 'chatbot/chatbot.html'
    result = ""
    context = {
        "result": result,
    }

    return render(request, template, context)
