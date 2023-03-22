from API.models import DIET_TYPE, HEALTH_TYPE, MEAL_TYPE, Recipe_Search
from django import forms
from django.contrib.auth.models import User


class RecipeSearchForm(forms.Form):
    Recipe_Name = forms.CharField(widget=forms.TextInput())
    Number_Of_Ingredients = forms.CharField(
        widget=forms.TextInput(), required=False)
    Meal_Type = forms.CharField(
        label='Meal Type', widget=forms.Select(choices=MEAL_TYPE), required=False)
    Health_Type = forms.CharField(
        label='Health Type', widget=forms.Select(choices=HEALTH_TYPE), required=False)
    Diet = forms.CharField(
        label='Diet Type', widget=forms.Select(choices=DIET_TYPE), required=False)
    Calorie_Range = forms.CharField(widget=forms.TextInput(), required=False)
    Max_Amount_Of_Time = forms.IntegerField(
        widget=forms.NumberInput(), required=False)


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        help_texts = {
            'username': None
        }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
