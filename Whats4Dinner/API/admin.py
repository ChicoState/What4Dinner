'''
admin view
'''
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, RecipeSearch, CreateRecipe, RecomendedRecipes


# Register your models here.
admin.site.register(RecipeSearch)
admin.site.register(Profile)
admin.site.register(CreateRecipe)
admin.site.register(RecomendedRecipes)
