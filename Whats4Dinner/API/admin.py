from django.contrib import admin
from .models import Profile, RecipeSearch, User, Create_Recipe, RecomendedRecipes
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(RecipeSearch)
admin.site.register(Profile)
admin.site.register(Create_Recipe)
admin.site.register(RecomendedRecipes)
