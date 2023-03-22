from django.db import models

MEAL_TYPE = [
    ("", "None"),
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('dinner', 'Dinner')
]

DIET_TYPE = [
    ("", "None"),
    ('balanced', 'Balanced'),
    ('high-fiber', 'High-Fiber'),
    ('high-protein', 'High-Protein'),
    ('low-carb', 'Low-Carb'),
    ('low-fat', 'Low-Fat'),
    ('low-sodium', 'Low-Sodium'),
]

HEALTH_TYPE = [
    ("", "None"),
    ('alcohol-cocktail', 'Alcohol-Cocktail'),
    ('alcohol-free', 'Alcohol-Free'),
    ('celery-free', 'Celery-Free'),
    ('crustacean-free', 'Crustacean-Free'),
    ('dairy-free', 'Dairy-Free'),
    ('dash', 'DASH'),
    ('egg-free', 'Egg-Free'),
    ('fish-free', 'Fish-Free'),
    ('foodmap-free', 'Foodmap-Free'),
    ('gluten-free', 'Gluten-Free'),
    ('immuno-supportive', 'Immuno-Supportive'),
    ('keto-friendly', 'Keto-Friendly'),
    ('kidney-friendly', 'Kidney-Friendly'),
    ('kosher', 'Kosher'),
    ('low-fat-abs', 'Low-Fat-Abs'),
    ('low-potassium', 'Low-Potassium'),
    ('low-sugar', 'Low-Sugar'),
    ('lupine-free', 'Lupine-Free'),
    ('mediterranean', 'Mediterranean'),
    ('mollusk-free', 'Mollusk-Free'),
    ('mustard-free', 'Mustard-Free'),
    ('no-oil-added', 'No-Oil-Added'),
    ('paleo', 'Paleo'),
    ('peanut-free', 'Peanut-Free'),
    ('pescatarian', 'Pescatarian'),
    ('pork-free', 'Pork-Free'),
    ('red-meat-free', 'Red-Meat-Free'),
    ('sesame-free', 'Sesame-Free'),
    ('shellfish-free', 'Shellfish-Free'),
    ('soy-free', 'Soy-Free'),
    ('sugar-conscious', 'Sugar-Concious'),
    ('sulfite-free', 'Sulfite-Free'),
    ('tree-nut-free', 'Tree-Nut-Free'),
    ('vegan', 'Vegan'),
    ('vegetarian', 'Vegetarian'),
    ('wheat-free', 'Wheat-Free'),
]


# Create your models here.
class Recipe_Search(models.Model):
    Recipe_Name = models.CharField(max_length=50)
    Image = models.ImageField
    Ingrediants = models.CharField(max_length=300, null=True)
    Meal_Type = models.CharField(choices=MEAL_TYPE, max_length=20, null=True)
    Health_Type = models.CharField(
        choices=HEALTH_TYPE, max_length=40, null=True)
    Diet = models.CharField(choices=DIET_TYPE, max_length=40, null=True)
    Calories = models.CharField(max_length=50, null=True)
    Time = models.IntegerField(null=True)


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    like_recipe = models.URLField(max_length=200)
    experience = models.CharField(max_length=500)
    calories_count = models.IntegerField()
