from django import forms
from API.models import Recipe_Search
from django.contrib.auth.models import User


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
