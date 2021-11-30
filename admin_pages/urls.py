from django.urls import path, include
from . import views

app_name='admin_pages'

urlpatterns = [
    path('', views.admin_index, name='admin_index'),
    path('manage_site_look', views.manage_site_look, name='manage_site_look'),
    path('manage_home', views.manage_home, name='manage_home'),
    path('manage_users', views.manage_users, name='manage_users'),
    path('manage_user_profile', views.manage_user_profile, name='manage_user_profile'),

    # Metrics
    path('manage_pet_sales_opts', views.manage_pet_sales_opts, name='manage_pet_sales_opts'),
    path('manage_product_sales_opts', views.manage_product_sales_opts, name='manage_product_sales_opts'),
    path('manage_site_visits_opts', views.manage_site_visits_opts, name='manage_site_visits_opts'),
    path('manage_pages_viewed_opts', views.manage_pages_viewed_opts, name='manage_pages_viewed_opts'),
    path('manage_users_opts', views.manage_users_opts, name='manage_users_opts'),
    path('manage_day_and_time_opts', views.manage_day_and_time_opts, name='manage_day_and_time_opts'),
]