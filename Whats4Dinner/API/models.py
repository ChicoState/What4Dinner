from django.db import models
from django.db.models import Model

MEAL_TYPE = [
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('dinner', 'Dinner')
]

DIET_TYPE = [
    ('balanced', 'Balanced'),
    ('high-fiber', 'High-Fiber'),
    ('high-protein', 'High-Protein'),
    ('low-carb', 'Low-Carb'),
    ('low-fat', 'Low-Fat'),
    ('low-sodium', 'Low-Sodium'),
]


# Create your models here.
class Recipe_Search(models.Model):
    Recipe_Name = models.CharField(max_length=50)
    Image=models.ImageField
    Ingrediants=models.CharField(max_length=300)
    Meal_Type=models.CharField(choices=MEAL_TYPE, max_length=20)
    Health_type=models.CharField(max_length=40)
    Diet=models.CharField(choices=DIET_TYPE,max_length=40)
    Calories=models.IntegerField()
    Time=models.IntegerField()
    
class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=50)
    like_recipe=models.URLField(max_length=200)
    experience=models.CharField(max_length=500)
    calories_count=models.IntegerField()