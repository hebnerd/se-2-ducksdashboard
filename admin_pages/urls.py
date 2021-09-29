from django.urls import path, include
from . import views

app_name='admin_pages'

urlpatterns = [
    path('', views.admin_index, name='admin_index'),
    path('manage_site_look', views.manage_site_look, name='manage_site_look'),
    path('manage_home', views.manage_home, name='manage_home'),
    path('manage_users', views.manage_users, name='manage_users'),
    path('manage_user_profile', views.manage_user_profile, name='manage_user_profile'),
]