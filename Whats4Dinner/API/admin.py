'''
admin views
'''
from django.contrib import admin

from .models import RecipeSearch, User

# Register your models here.
admin.site.register(RecipeSearch)
admin.site.register(User)
