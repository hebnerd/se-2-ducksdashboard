from django.shortcuts import render

from dashboard import settings
from .models import *
from .forms import *
from admin_pages.models import *

def index(request):
    """Displays the landing page.
    Parameters:
    request (HttpRequest): An HTTP Request object. 
    Returns:
    HttpResponse: Directs the user to the landing page.
    """
    context = {
        'home': Home.objects.get(id=1),
        'petSalesOpts': PetSalesOpts.objects.get(id=1),
        'productSalesOpts': ProductSalesOpts.objects.get(id=1),
        'siteVisitsOpts': SiteVisitsOpts.objects.get(id=1),
        'pagesViewedOpts': PagesViewedOpts.objects.get(id=1),
        'usersOpts': UsersOpts.objects.get(id=1)
    }
    return render(request, 'site_pages/index.html', context)