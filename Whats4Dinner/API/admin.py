'''
admin views
'''
from django.contrib import admin

from API.models import RecipeSearch, User

# Register your models here.
admin.site.register(RecipeSearch)
admin.site.register(User)
