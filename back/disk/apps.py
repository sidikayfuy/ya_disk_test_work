from django.apps import AppConfig
from django.db.models.signals import post_migrate
from .startup import check_api_availability
from django.core.exceptions import ImproperlyConfigured


class DiskConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'disk'

    def ready(self):
        check_api_availability()

