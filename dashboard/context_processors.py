from django.contrib.auth.models import User
from admin_pages.models import SiteLook, UserProfile

def add_to_context(request):
    site_look = SiteLook.objects.get(id=1)
    profile = None
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)

    return {
        'navigation_img_size': site_look.navigation_img_size,
        'profile': profile
    }
