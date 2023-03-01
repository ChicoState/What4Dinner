from django import forms
from API.models import Recipe_Search

class RecipeSearchForm(forms.Form):
    Recipe_Name = forms.CharField(max_length=50)
    Ingrediants=forms.CharField(max_length=300)
    Meal_Type=forms.CharField(max_length=20)
    # Health_type=forms.CharField(max_length=40)
    # Diet=forms.CharField(max_length=40)
    # Calories=forms.IntegerField()
    # Time=forms.IntegerField()  

    # class Meta():
    #     model = Recipe_Search
    #     fields = {'Recipe_Name','Ingrediants','Meal_Type','Health_type',
    #               'Diet', 'Calories', 'Time'}