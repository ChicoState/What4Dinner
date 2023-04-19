from API.models import DIET_TYPE, HEALTH_TYPE, MEAL_TYPE, Recipe_Search, Create_Recipe
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
# from django.contrib.auth.models import Create_Recipe


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
    
class RecipeCreateForm(forms.ModelForm):
    Recipe_Name = forms.CharField(widget=forms.TextInput())
    List_Ingredients = forms.CharField(widget=forms.TextInput())
    Meal_Type = forms.CharField(
        label='Meal Type', widget=forms.Select(choices=MEAL_TYPE))
    Health_Type = forms.CharField(
        label='Health Type', widget=forms.Select(choices=HEALTH_TYPE))
    Diet = forms.CharField(
        label='Diet Type', widget=forms.Select(choices=DIET_TYPE))
    Total_Calories = forms.CharField(widget=forms.TextInput())
    Time_Needed = forms.CharField(widget=forms.TextInput())
    Instructions = forms.CharField(widget=forms.TextInput())
    Upload_Image = forms.ImageField()

    class Meta():
            model = Create_Recipe
            fields = ['Recipe_Name', 'List_Ingredients', 'Meal_Type','Health_Type',
                       'Diet', 'Total_Calories','Time_Needed','Instructions','Upload_Image']


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
