from django.apps import AppConfig


class HairusersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Hairusers'

    def ready(self):
        import Hairusers.signals

