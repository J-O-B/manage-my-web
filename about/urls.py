from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name="about"),
    path('website-management/', views.webManage, name="website-management"),
    path('seo/', views.seo, name="seo"),
]
