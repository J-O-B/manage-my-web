from django.shortcuts import render
from .models import UserProfile


def check_or_create(request):
    """
    If user fields are none, update the basics
    """
    user = UserProfile


def user_profile(request):
    """
    Display a user profile
    """

    template = 'profiles/user_profile.html'
    context = {
        "profile": UserProfile,
    }
    return render(request, template, context)
