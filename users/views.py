from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from admin_pages.models import UserProfile
from .forms import *

def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('login'))


@login_required
def register(request):
    """Register a new user."""
    if (request.method != 'POST'):
        form = SignUpForm()
    else:
        form = SignUpForm(data=request.POST)

        if (form.is_valid()):
            data = form.cleaned_data
            new_usr = User.objects.create_user(username=data['username'], email=data['email'],
                                                password=data['password'])
            fname = data['first_name']
            lname = data['last_name']
            new_usr.first_name = fname
            new_usr.last_name = lname
            new_usr.is_staff = data['is_staff']
            new_usr.save()
            new_usr.refresh_from_db()

            usr_profile = UserProfile(
                user=new_usr,
                profile_role='Hacker'
            )
            usr_profile.save()

            return HttpResponseRedirect(reverse('admin_pages:manage_users'))

    context = { 'form': form }
    return render(request, 'users/register.html', context)


@login_required
def update_user(request):
    user = User.objects.get(id=request.user.id)

    if request.method != 'POST':
        form = UpdateUserForm(initial={ 
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
         })
    else:
        form = UpdateUserForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            fname = data['first_name']
            lname = data['last_name']
            email = data['email']

            user.first_name = fname
            user.last_name = lname
            user.email = email
            user.save()

            return HttpResponseRedirect(reverse('admin_pages:admin_index'))
   
    context = { 'form': form }
    return render(request, 'users/update_user.html', context)


@login_required
def confirm_delete_user(request, user_id):
    """Display a confirmation dialog view before deleting a user."""
    user = User.objects.get(id=user_id)

    context = { 'user': user }
    return render(request, 'users/confirm_delete_user.html', context)


@login_required
def delete_user(request, user_id):
    """Delete the user."""
    User.objects.get(id=user_id).delete()
    return HttpResponseRedirect(reverse('admin_pages:manage_users'))
