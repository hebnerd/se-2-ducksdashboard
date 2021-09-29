from django import forms
from .models import *

class HomeForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        required=False,
    )
    alert_banner = forms.CharField(
        label='Alert Banner:',
        required=False,
    )
    about_descr = forms.CharField(
        label='About Description',
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Describe the Pet Shop dashboard.',
            'rows': 3,
            'cols': 15,
        })
    )

    class Meta:
        model = Home
        fields = [ 'title', 'alert_banner', 'about_descr' ]