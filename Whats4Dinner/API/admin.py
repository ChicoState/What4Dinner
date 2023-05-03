from django.contrib import admin
from .models import Recipe_Search
from django.contrib.auth.models import User
from .models import Profile

# Register your models here.
admin.site.register(Recipe_Search)
admin.site.register(Profile)
