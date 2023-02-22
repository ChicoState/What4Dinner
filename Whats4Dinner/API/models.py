from django.db import models
from django.db.models import Model

# Create your models here.
class Recipe_Search(models.Model):
    Recipe_Name = models.CharField(max_length=50)
    Image=models.ImageField
    Ingrediants=models.CharField(max_length=300)
    Meal_Type=models.CharField(max_length=20)
    Health_type=models.CharField(max_length=40)
    Diet=models.CharField(max_length=40)
    Calories=models.IntegerField()
    Time=models.IntegerField()
    
