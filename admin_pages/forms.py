from django import forms
from .models import *

class ImageOptions:
    PERCENTAGES = (
            ('width: 10%;', '10%'),
            ('width: 20%;', '20%'),
            ('width: 30%;', '30%'),
            ('width: 40%;', '40%'),
            ('width: 50%;', '50%'),
            ('width: 60%;', '60%'),
            ('width: 70%;', '70%'),
            ('width: 80%;', '80%'),
            ('width: 90%;', '90%'),
            ('width: 100%;', '100%'),
        )

    POSITIONS = (
        ('float: left;', 'float left'),
        ('float: right;', 'float right'),
        ('display: inline;', 'inline'),
        ('display: block;', 'block'),
        ('display: inline-block;', 'inline-block'),
    )


class MetricsDisplayOpts:
    MAX_BINS = (
        (6, '6'),
        (8, '8'),
        (10, '10'),
        (12, '12'),
        (14, '14'),
        (16, '16'),
        (18, '18'),
        (20, '20'),
    )
    TIME_RANGE = (
        (1, 'Day'),
        (7, 'Week'),
        (30, 'Month'), # Keeping month simple -- we will just get last 30 days.
    )
    DISPLAY_TYPE = (
        (0, 'Top Regions'),
        (1, 'Top Countries'),
    )

PROFILE_ROLES = (
    ('Product Owner', 'Product Owner'),
    ('Scrum Master', 'Scrum Master'),
    ('Developer', 'Developer'),
    ('Client', 'Client'),
    ('Hacker', 'Hacker'),
)

class SiteLookForm(forms.ModelForm):
    navigation_img = forms.FileField(
        label='Nav Image',
        required=False,
        widget=forms.FileInput(attrs={
            'multiple': False,
            'accept': 'image/*'
        })
    )

    navigation_img_size = forms.CharField(
        label='Nav Image Size',
        required=False,
        widget=forms.Select(
            choices=ImageOptions.PERCENTAGES
        )
    )

    favicon = forms.FileField(
        label='Favicon Image',
        required=False,
        widget=forms.FileInput(attrs={
            'multiple': False,
            'accept': 'image/x-icon'
        })
    )

    class Meta:
        model = SiteLook
        fields = [
            'navigation_img', 'navigation_img_size',
            'favicon'
        ]


class UserProfileForm(forms.ModelForm):
    profile_img = forms.FileField(
        label='Profile Image',
        required=False,
        widget=forms.FileInput(attrs={
            'multiple': False,
            'accept': 'image/*'
        })
    )
    
    profile_role = forms.CharField(
        label='Role',
        required=False,
        widget=forms.Select(
            choices=PROFILE_ROLES
        )
    )

    class Meta:
        model = UserProfile
        fields = [ 'profile_img', 'profile_role', 'user' ]

# TODO: Make ModelForms for each of the DisplayOpts models
class PetSalesOptsForm(forms.ModelForm):
    top_num_categories = forms.IntegerField(
        label='Most Popular, # of Categories',
        widget=forms.Select(
            choices=MetricsDisplayOpts.MAX_BINS
        )
    )

    top_num_breeds = forms.IntegerField(
        label='Most Popular, # of Breeds',
        widget=forms.Select(
            choices=MetricsDisplayOpts.MAX_BINS
        )
    )

    timerange = forms.IntegerField(
        label='Time range',
        widget=forms.Select(
            choices=MetricsDisplayOpts.TIME_RANGE
        )
    )

    display = forms.BooleanField(
        label='Show on Dashboard',
        required=False
    )

    class Meta:
        model = PetSalesOpts
        fields = [
            'top_num_categories', 'top_num_breeds',
            'timerange', 'display'
        ]

class ProductSalesOptsForm(forms.ModelForm):
    top_num_products = forms.IntegerField(
        label='Most Popular, # of Products',
        widget=forms.Select(
            choices=MetricsDisplayOpts.MAX_BINS
        )
    )

    timerange = forms.IntegerField(
        label='Time range',
        widget=forms.Select(
            choices=MetricsDisplayOpts.TIME_RANGE
        )
    )

    display = forms.BooleanField(
        label='Show on Dashboard',
        required=False
    )

    class Meta:
        model = ProductSalesOpts
        fields = [
            'top_num_products', 'timerange',
            'display'
        ]

class SiteVisitsOptsForm(forms.ModelForm):
    top_num_by_location = forms.IntegerField(
        label='Most Popular by Location',
        widget=forms.Select(
            choices=MetricsDisplayOpts.MAX_BINS
        )
    )

    display_type = forms.IntegerField(
        label='Display Type',
        widget=forms.Select(
            choices=MetricsDisplayOpts.DISPLAY_TYPE
        )
    )

    timerange = forms.IntegerField(
        label='Time range',
        widget=forms.Select(
            choices=MetricsDisplayOpts.TIME_RANGE
        )
    )

    display = forms.BooleanField(
        label='Show on Dashboard',
        required=False
    )

    class Meta:
        model = SiteVisitsOpts
        fields = [
            'top_num_by_location', 'display_type',
            'timerange', 'display'
        ]

class PagesViewedOptsForm(forms.ModelForm):
    top_num_pages = forms.IntegerField(
        label='Most Popular, # of pages',
        widget=forms.Select(
            choices=MetricsDisplayOpts.MAX_BINS
        )
    )

    timerange = forms.IntegerField(
        label='Time range',
        widget=forms.Select(
            choices=MetricsDisplayOpts.TIME_RANGE
        )
    )

    display = forms.BooleanField(
        label='Show on Dashboard',
        required=False
    )

    class Meta:
        model = PagesViewedOpts
        fields = [
            'top_num_pages', 'timerange', 
            'display'
        ]

class UsersOptsForm(forms.ModelForm):
    timerange_registered = forms.IntegerField(
        label='Time range registered',
        widget=forms.Select(
            choices=MetricsDisplayOpts.TIME_RANGE
        )
    )

    show_users_online = forms.BooleanField(
        label='Show users online',
        required=False
    )

    display = forms.BooleanField(
        label='Show on Dashboard',
        required=False
    )

    class Meta:
        model = UsersOpts
        fields = [
            'timerange_registered', 'show_users_online',
            'display'
        ]

class DayAndTimeOptsForm(forms.ModelForm):
    top_num_days = forms.IntegerField(
        label='Most Popular, # of Days',
        widget=forms.Select(
            choices=MetricsDisplayOpts.MAX_BINS
        )
    )

    top_num_times = forms.IntegerField(
        label='Most Popular, # of Times',
        widget=forms.Select(
            choices=MetricsDisplayOpts.MAX_BINS
        )
    )

    timerange = forms.IntegerField(
        label='Time range',
        widget=forms.Select(
            choices=MetricsDisplayOpts.TIME_RANGE
        )
    )

    display = forms.BooleanField(
        label='Show on Dashboard',
        required=False
    )

    class Meta:
        model = DayAndTimeOpts
        fields = [
            'top_num_days', 'top_num_times',
            'timerange', 'display'
        ]