'''
admin view
'''
from django.contrib import admin

from .models import Profile, RecipeSearch, User

# Register your models here.
admin.site.register(RecipeSearch)
admin.site.register(User)
admin.site.register(Profile)
