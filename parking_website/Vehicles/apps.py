from django.apps import AppConfig
from django.conf import settings

class VehiclesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Vehicles"

    def ready(self):
        if not settings.DEBUG:
            import Vehicles.signals
