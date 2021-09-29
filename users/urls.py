"""Defines url patterns for the users app."""

from django.urls import path, reverse, reverse_lazy
from django.contrib.auth import login, views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        	template_name='users/login.html'), name='login'),
	path('logout/', views.logout_view, name='logout'),
	path('register/', views.register, name='register'),
	path('update_user/', views.update_user, name='update_user'),
	path('confirm_delete_user/<int:user_id>', views.confirm_delete_user, name='confirm_delete_user'),
	path('delete_user/<int:user_id>', views.delete_user, name='delete_user'),

	path('reset_password/', auth_views.PasswordResetView.as_view(
			template_name='users/reset_password_email.html',
			email_template_name='users/reset_email_message.html',
			success_url=reverse_lazy('users:password_reset_complete'),
		), name='reset_password'),
	
	path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
			template_name='users/reset_password_sent.html'), name='password_reset_done'),
	
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
			template_name='users/reset_password_confirm.html',
			success_url=reverse_lazy('users:password_reset_complete')
			), name='password_reset_confirm'),
	
	path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
			template_name='users/reset_password_complete.html'), name='password_reset_complete')
]
