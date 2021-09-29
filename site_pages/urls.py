from django.urls import path, include
from . import views

app_name='site_pages'

urlpatterns = [
    path('', views.index, name='index'),
]