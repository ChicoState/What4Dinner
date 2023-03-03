from django import forms
from API.models import Recipe_Search
from API.models import MEAL_TYPE, DIET_TYPE

class RecipeSearchForm(forms.Form):
    Recipe_Name = forms.CharField(widget=forms.TextInput())
    Ingrediants=forms.CharField(widget=forms.TextInput())
    Meal_Type=forms.CharField(label= 'Meal Type', widget= forms.Select(choices=MEAL_TYPE))
    # Health_type=forms.CharField(max_length=40)
    Diet=forms.CharField(label= 'Diet Type', widget=forms.Select(choices=DIET_TYPE))
    Calories=forms.IntegerField(widget=forms.NumberInput())
    Time=forms.IntegerField(widget=forms.NumberInput())

    # class Meta():
    #     model = Recipe_Search
    #     fields = {'Recipe_Name','Ingrediants','Meal_Type','Health_type',
    #               'Diet', 'Calories', 'Time'}