from django.shortcuts import render
from .models import UserProfile, create_or_update_user_profile
from datetime import datetime
from django.contrib import messages
from .forms import UserProfileForm

today = datetime.today()


def after_login(request):
    user = request.user
    template = "profiles/after-login.html"
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        profile = False
    if profile:
        messages.success(
            request, f'Welcome back {profile.full_name}.')
    else:
        messages.info(
            request, 'Welcome back {user}. It seems like your profile is incomplete, please \
                update your profile when possible.')
    context = {
        "profile": profile,
        "user": user,
    }
    return render(request, template, context)


def user_profile(request):
    """
    Display a user profile
    """
    form = UserProfileForm
    template = 'profiles/user_profile.html'
    context = {
        "profile": UserProfile,
        "form": form,
    }
    return render(request, template, context)
