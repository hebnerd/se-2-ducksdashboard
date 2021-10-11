from django.shortcuts import render

from dashboard import settings
from .models import *
from .forms import *
from admin_pages.models import *

from . import data_aggregator

def index(request):
    """Displays the landing page.
    Parameters:
    request (HttpRequest): An HTTP Request object. 
    Returns:
    HttpResponse: Directs the user to the landing page.
    """
    home = Home.objects.get(id=1)
    petSalesOpts = PetSalesOpts.objects.get(id=1)
    productSalesOpts = ProductSalesOpts.objects.get(id=1)
    siteVisitsOpts = SiteVisitsOpts.objects.get(id=1)
    pagesViewedOpts = PagesViewedOpts.objects.get(id=1)
    usersOpts = UsersOpts.objects.get(id=1)

    pet_categories_list, pet_categories_values_list = data_aggregator.get_pet_sales_categories(petSalesOpts.timerange, petSalesOpts.top_num_categories)
    pet_breeds_list, pet_breeds_values_list = data_aggregator.get_pet_sales_breeds(petSalesOpts.timerange, petSalesOpts.top_num_breeds)

    context = {
        'home': home,
        'petSalesOpts': petSalesOpts,
        'productSalesOpts': productSalesOpts,
        'siteVisitsOpts': siteVisitsOpts,
        'pagesViewedOpts': pagesViewedOpts,
        'usersOpts': usersOpts,
        
        'pet_categories_list': pet_categories_list,
        'pet_categories_values_list': pet_categories_values_list,

        'pet_breeds_list': pet_breeds_list,
        'pet_breeds_values_list': pet_breeds_values_list,
    }
    return render(request, 'site_pages/index.html', context)