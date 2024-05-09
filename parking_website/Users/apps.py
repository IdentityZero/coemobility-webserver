from django.apps import AppConfig
from django.conf import settings


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Users"

    def ready(self):
        if settings.DEBUG == False:
            print("Signals ready")
            import Users.signals