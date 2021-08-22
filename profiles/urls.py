from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_profile, name="user_profile"),
    path('after-login/', views.after_login, name="after-login"),
]
