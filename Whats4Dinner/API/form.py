'''
Forms definitions for the project.
'''
from django import forms
from django.contrib.auth.models import User

from API.models import DIET_TYPE, HEALTH_TYPE, MEAL_TYPE


class RecipeSearchForm(forms.Form):
    '''
    Parameters for recipe search form on search page
    '''
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
    '''
    Parameters for User sign up form
    '''
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        '''
        Metadata to save when saving the user to the DB.
        '''
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        help_texts = {
            'username': None
        }


class LoginForm(forms.Form):
    '''
    Parameters for the user login form.
    '''
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
