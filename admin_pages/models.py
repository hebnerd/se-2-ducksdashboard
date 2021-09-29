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

class PetSalesDisplayOpts(models.Model): # Most popular pets sold per unit of time
    # Define attributes here
    pass


class ProductSalesDisplayOpts(models.Model): # Most popular store products sold per unit of time
    # Define attributes here
    pass


class SiteVisitsDisplayOpts(models.Model): # This is referring to the Session table -- [...]/monitoring/usage/visits
    # Define attributes here
    pass


class PagesViewedDisplayOpts(models.Model): # Pages_Viewed table -- Most popular pages viewed per unit of time.
    # Define attributes here
    pass


class UsersDisplayOpts(models.Model): # No. users registered per unit of time, no. users online now
    # Define attributes here
    pass
