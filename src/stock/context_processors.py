from django.conf import settings
from .models import Profile
from django.urls import resolve


def global_vars(request):
    user = request.user
    profile = Profile.objects.filter(user__pk=user.pk).first()
    current_url = resolve(request.path_info).url_name
    print(type(current_url),"_______________________________")
    return {'profile': profile, "current_url":current_url}

def current_url_var(request,*args):
    current_url = resolve(request.path_info).url_name
    if current_url in args:
        return {'current_url2':True}
    return {'current_url2':True}