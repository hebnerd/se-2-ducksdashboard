from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SiteLook(models.Model):
    """Contains attributes that affect the appearance of the site."""
    navigation_img      = models.FileField()
    navigation_img_size = models.CharField(max_length=12, blank=True, null=True)

class UserProfile(models.Model):
    profile_img      = models.FileField(null=True, blank=True)
    profile_img_name = models.TextField(default='profile-default.gif')
    profile_role     = models.CharField(max_length=13, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


#################### Metrics:
# TODO: Implement each of these. These are the options that let us specify # of bins (e.g. top 5, top 10 most popular) and time range.

class PetSalesOpts(models.Model): # Most popular pets sold per unit of time
    top_num_categories = models.IntegerField(default=6)
    top_num_breeds = models.IntegerField(default=6)
    timerange = models.IntegerField(default=7)
    display = models.BooleanField(default=False)

class ProductSalesOpts(models.Model): # Most popular store products sold per unit of time
    top_num_products = models.IntegerField(default=6)
    timerange = models.IntegerField(default=7)
    display = models.BooleanField(default=False)

class SiteVisitsOpts(models.Model): # This is referring to the Session table -- [...]/monitoring/usage/visits
    top_num_by_location = models.IntegerField(default=6)
    display_type = models.IntegerField(default=0)
    timerange = models.IntegerField(default=7)
    display = models.BooleanField(default=False)

class PagesViewedOpts(models.Model): # Pages_Viewed table -- Most popular pages viewed per unit of time.
    top_num_pages = models.IntegerField(default=6)
    timerange = models.IntegerField(default=7)
    display = models.BooleanField(default=False)

class UsersOpts(models.Model): # No. users registered per unit of time, no. users online now
    timerange_registered = models.IntegerField(default=0)
    show_users_online = models.BooleanField(default=True)
    display = models.BooleanField(default=False)

class DayAndTimeOpts(models.Model): # Most popular days and times
    top_num_days = models.IntegerField(default=6)
    top_num_times = models.IntegerField(default=6)
    timerange = models.IntegerField(default=7)
    display = models.BooleanField(default=False)
