from django import forms
from API.models import Recipe_Search
from API.models import MEAL_TYPE, DIET_TYPE, HEALTH_TYPE
from django.contrib.auth.models import User

class RecipeSearchForm(forms.Form):
    Recipe_Name = forms.CharField(widget=forms.TextInput())
    Ingrediants=forms.CharField(widget=forms.TextInput())
    Meal_Type=forms.CharField(label= 'Meal Type', widget= forms.Select(choices=MEAL_TYPE))
    Health_Type=forms.CharField(label= 'Health Type', widget= forms.Select(choices=HEALTH_TYPE))
    Diet=forms.CharField(label= 'Diet Type', widget=forms.Select(choices=DIET_TYPE))
    Calorie_Range=forms.CharField(widget=forms.TextInput())
    Max_Amount_Of_Time=forms.IntegerField(widget=forms.NumberInput())

    # class Meta():
    #     model = Recipe_Search
    #     fields = {'Recipe_Name','Ingrediants','Meal_Type','Health_type',
    #               'Diet', 'Calories', 'Time'}


class SignUpForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        help_texts = {
            'username': None
            }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
