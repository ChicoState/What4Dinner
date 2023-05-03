from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'API'

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
