from django.apps import AppConfig


class MiniblogappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'miniblogapp'

    # def ready(self):
    #     import miniblogapp.signals