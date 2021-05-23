from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name="about"),
    path('chatbotHook/<data>/', views.chatbotHook, name="chatbotHook"),
]
