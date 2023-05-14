'''
admin view
'''
from django.contrib import admin

from .models import CreateRecipe, Profile, RecipeSearch, RecomendedRecipes

# Register your models here.
admin.site.register(RecipeSearch)
admin.site.register(Profile)
admin.site.register(CreateRecipe)
admin.site.register(RecomendedRecipes)
