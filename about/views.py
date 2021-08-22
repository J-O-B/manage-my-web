from django.shortcuts import render


def about(request):
    return render(request, 'about/about.html')


def webManage(request):
    return render(request, 'about/management.html')


def seo(request):
    return render(request, 'about/seo.html')
