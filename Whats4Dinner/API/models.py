from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from PIL import Image

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
