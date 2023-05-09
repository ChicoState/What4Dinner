'''
Model declarations
'''
from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.db.models import Model
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
class RecipeSearch(models.Model):
    '''
    Recpe search model declaration
    '''
    Recipe_Name = models.CharField(max_length=50)
    Image = models.ImageField
    Ingrediants = models.CharField(max_length=300, null=True)
    Meal_Type = models.CharField(choices=MEAL_TYPE, max_length=20, null=True)
    Health_Type = models.CharField(
        choices=HEALTH_TYPE, max_length=40, null=True)
    Diet = models.CharField(choices=DIET_TYPE, max_length=40, null=True)
    Calories = models.CharField(max_length=50, null=True)
    Time = models.IntegerField(null=True)
    # Added field for shareable link
    shareable_link = models.URLField(max_length=200, unique=True)

class CreateRecipe(models.Model):
    Create_RecipeName = models.CharField(null=False,max_length=50)
    Create_Ingrediants=models.CharField(null=False,max_length=300)
    Create_Meal_Type=models.CharField(choices=MEAL_TYPE, max_length=20, null=False)
    Create_Health_Type=models.CharField(choices=HEALTH_TYPE, max_length=40, null=False)
    Create_Diet=models.CharField(choices=DIET_TYPE, max_length=40, null=False)
    Create_Calories=models.CharField(null=False, max_length=50)
    Create_Time=models.CharField(null=False, max_length=50)
    Create_Instruct = models.CharField(null=False, max_length=10000, default='')
    Upload_Image=models.ImageField(null=True, blank=True, upload_to="Uploads/")

class RecomendedRecipes(models.Model):
    '''
    Random Recipe create model declaration
    '''
    Rec_Recipe_Name = models.CharField(null=False,max_length=50)
    Rec_URL = models.URLField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)
    bio = models.TextField(null=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username

    def save(self):
        super().save()

        img = Image.open(self.image.path)


        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
