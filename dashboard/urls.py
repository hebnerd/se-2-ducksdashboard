"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('dashboard/', include('dashboard.urls'))
"""
from django.contrib import admin
from django.contrib.auth import login, views as auth_views
from django.urls import path, include, reverse_lazy
from django.views.generic.base import TemplateView
from admin_pages import views as admin_views

urlpatterns = [
    path('', include('site_pages.urls')),
    path('admin_pages/', include('admin_pages.urls')),
    path('login/', auth_views.LoginView.as_view(
        	template_name='users/login.html'), name='login'),
    path('accounts/login/', auth_views.LoginView.as_view(
        	template_name='users/login.html'), name='login'),
    path('users/', include('users.urls')),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]