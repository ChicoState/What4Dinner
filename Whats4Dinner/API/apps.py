'''
Project config file.
'''
from django.apps import AppConfig


class ApiConfig(AppConfig):
    '''
    Default Project config.
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'API'
