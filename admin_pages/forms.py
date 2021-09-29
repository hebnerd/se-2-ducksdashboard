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
