from django.db import models

class Home(models.Model):
    """Contains attributes that determine the content of the home page."""
    title          = models.CharField(max_length=60, blank=True, null=True, default='Pet Shop Metrics')
    alert_banner   = models.CharField(max_length=300, blank=True, null=True, default='')
    about_descr    = models.CharField(max_length=400, blank=True, null=True, default='')