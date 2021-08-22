from django.shortcuts import render


def policy(request):
    template = 'policy/policy.html'
    return render(request, template)
