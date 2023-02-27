from django.contrib import admin
from .models import Recipe_Search
from .models import User

# Register your models here.
admin.site.register(Recipe_Search)
admin.site.register(User)