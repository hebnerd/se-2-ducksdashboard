from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.views.decorators.cache import never_cache

from dashboard import settings
from .models import *
from .forms import *

def index(request):
    """Displays the landing page.
    Parameters:
    request (HttpRequest): An HTTP Request object. 
    Returns:
    HttpResponse: Directs the user to the landing page.
    """
    home = Home.objects.get(id=1)
    context = { 'home': home }
    return render(request, 'site_pages/index.html', context)