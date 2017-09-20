from django.conf import settings

def global_setting(request):
    return settings.SUMMER_CONFIG
