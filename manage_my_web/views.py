from django.shortcuts import render


def Not_Found(request, exception):
    return render(request, "404.html")
