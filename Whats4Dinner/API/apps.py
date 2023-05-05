'''
Pre-generated App data
'''
from django.apps import AppConfig


class ApiConfig(AppConfig):
    '''
    API configuration
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'API'

class UserConfig(AppConfig):
    '''
    User configuration
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals
