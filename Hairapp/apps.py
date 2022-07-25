from django.apps import AppConfig


class HairappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Hairapp'

    def ready(self):
        import Hairapp.signals