'''
admin view
'''
from django.contrib import admin
from .models import Profile, RecipeSearch, User, CreateRecipe, RecomendedRecipes
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(RecipeSearch)
admin.site.register(Profile)
admin.site.register(CreateRecipe)
admin.site.register(RecomendedRecipes)
