from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

from dashboard import settings
from site_pages.models import Home
from site_pages.forms import HomeForm
from .models import *
from .forms import *

import os


STATIC_DIR      = settings.STATIC_ROOT
ROBOTS_TXT_DIR  = settings.BASE_DIR + '/templates/'
STATIC_IMGS_DIR = STATIC_DIR + '/images/'
NAV_ICON_DIR    = STATIC_DIR + '/nav_image/'


def try_delete_files(path):
    """Attempts to delete all files in the directory, path.

    Parameters:
    path (string): the file path from which to remove all files.

    Returns:
    bool: Indicates whether all file deletions succeeded or not.
    """
    failure = False
    try:
        for root, dirs, files in os.walk(path):
            for f in files:
                try:
                    os.remove(os.path.join(root, f))
                except:
                    failure = True
        return failure
    except:
        return False


@login_required
def admin_index(request):
    user = request.user
    context = { 'current_user': user.first_name }

    return render(request, 'admin_pages/index.html', context)
  

@login_required
def manage_site_look(request):
    site_look = SiteLook.objects.get(id=1)

    if (request.method != 'POST'):
        form = SiteLookForm(instance=site_look)
    else:
        fs_storage = FileSystemStorage(location=NAV_ICON_DIR)
        form = SiteLookForm(instance=site_look, data=request.POST)

        if len(request.FILES) != 0:
            if 'navigation_img' in request.FILES.keys():
                try_delete_files(NAV_ICON_DIR)
                image = request.FILES['navigation_img']
                fs_storage.save('nav_image.png', image)
            
            if 'favicon' in request.FILES.keys():
                fs_storage = FileSystemStorage(location=STATIC_IMGS_DIR)
                try:
                    os.remove(os.path.join(STATIC_IMGS_DIR, 'favicon.ico'))
                except:
                    pass
                image = request.FILES['favicon']
                fs_storage.save('favicon.ico', image)

        if form.is_valid():
            form.save()
        
        return HttpResponseRedirect(reverse('admin_pages:admin_index'))
    
    context = { 'form': form }
    return render(request, 'admin_pages/manage_site_look/manage_site_look.html', context)


@login_required
def manage_home(request):
    home = Home.objects.get(id=1)
    if request.method != 'POST':
        form = HomeForm(instance=home)
    else:
        form = HomeForm(instance=home, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_pages:admin_index'))
    context = { 'form': form }
    return render(request, 'admin_pages/manage_home/manage_home.html', context)


@login_required
def manage_user_profile(request):
    profile = UserProfile.objects.get(user=User.objects.get(id=request.user.id))
    if request.method != 'POST':
        form = UserProfileForm(instance=profile)
    else:
        form = UserProfileForm(instance=profile, data=request.POST)

        if form.is_valid():
            form.save()

            if len(request.FILES) != 0:
                fs_storage = FileSystemStorage(location=STATIC_IMGS_DIR)
                if ((profile.profile_img_name != '') 
                    and (profile.profile_img_name != 'profile-default.gif')): # Prevent deletion of default image.
                    try:
                        os.remove(os.path.join(STATIC_IMGS_DIR,
                            profile.profile_img_name))
                    except:
                        pass
                icon = request.FILES['profile_img']
                filename = fs_storage.save(icon.name, icon)
                profile.profile_img_name = filename
                profile.save()
            return HttpResponseRedirect(reverse('admin_pages:admin_index'))
    
    context = { 'profile': profile, 'form': form }
    return render(request, 'admin_pages/manage_user_profile/manage_user_profile.html',
                    context)


@login_required
def manage_users(request):
    """Provides the user a form template to facilitate creation and deletion of a
    User admin (ish) account. The user is considered an admin for access to the 
    Admin Pages and API but is not a true Django admin which is unnecessary since
    there are no admin-registered models.

    Parameters:
    request (HttpRequest): An HTTP Request object. 

    Returns:
    HttpResponse: Directs the user to the appropriate URL.
    """
    if request.user.is_staff:
        users = User.objects.all()

        context = { 'users': users }
        return render(request, 'admin_pages/manage_users/manage_users.html', context)
    else:
        return HttpResponseRedirect(reverse('admin_pages:admin_index'))

@login_required
def manage_pet_sales_opts(request):
    pet_sales_opts = PetSalesOpts.objects.get(id=1)
    if request.method != 'POST':
        form = PetSalesOptsForm(instance=pet_sales_opts)
    else:
        form = PetSalesOptsForm(instance=pet_sales_opts, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_pages:admin_index'))
    context = { 'form': form }
    return render(request, 'admin_pages/manage_metrics_display_opts/manage_petsales.html', context)

@login_required
def manage_product_sales_opts(request):
    product_sales_opts = ProductSalesOpts.objects.get(id=1)
    if request.method != 'POST':
        form = ProductSalesOptsForm(instance=product_sales_opts)
    else:
        form = ProductSalesOptsForm(instance=product_sales_opts, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_pages:admin_index'))
    context = { 'form': form } 
    return render(request, 'admin_pages/manage_metrics_display_opts/manage_productsales.html', context)

@login_required
def manage_site_visits_opts(request):
    site_visits_opts = SiteVisitsOpts.objects.get(id=1)
    if request.method != 'POST':
        form = SiteVisitsOptsForm(instance=site_visits_opts)
    else:
        form = SiteVisitsOptsForm(instance=site_visits_opts, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_pages:admin_index'))
    context = { 'form': form } 
    return render(request, 'admin_pages/manage_metrics_display_opts/manage_sitevisits.html', context)

@login_required
def manage_pages_viewed_opts(request):
    pages_viewed_opts = PagesViewedOpts.objects.get(id=1)
    if request.method != 'POST':
        form = PagesViewedOptsForm(instance=pages_viewed_opts)
    else:
        form = PagesViewedOptsForm(instance=pages_viewed_opts, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_pages:admin_index'))
    context = { 'form': form } 
    return render(request, 'admin_pages/manage_metrics_display_opts/manage_pagesviewed.html', context)

@login_required
def manage_users_opts(request):
    users_opts = UsersOpts.objects.get(id=1)
    if request.method != 'POST':
        form = UsersOptsForm(instance=users_opts)
    else:
        form = UsersOptsForm(instance=users_opts, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_pages:admin_index'))
    context = { 'form': form } 
    return render(request, 'admin_pages/manage_metrics_display_opts/manage_users.html', context)

@login_required
def manage_day_and_time_opts(request):
    day_and_time_opts = DayAndTimeOpts.objects.get(id=1)
    if request.method != 'POST':
        form = DayAndTimeOptsForm(instance=day_and_time_opts)
    else:
        form = DayAndTimeOptsForm(instance=day_and_time_opts, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_pages:admin_index'))
    context = { 'form': form }
    return render(request, 'admin_pages/manage_metrics_display_opts/manage_dayandtime.html', context)