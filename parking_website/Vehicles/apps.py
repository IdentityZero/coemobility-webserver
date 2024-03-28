from django.apps import AppConfig


class VehiclesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Vehicles"

    def ready(self):
        import Vehicles.signals
