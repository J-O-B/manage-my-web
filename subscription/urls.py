from django.urls import path
from . import views

urlpatterns = [
    path('', views.Subscription, name="subscription"),
    path('gold/', views.Gold, name="gold"),
    path('silver/', views.Silver, name="silver"),
]
