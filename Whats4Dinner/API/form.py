from django import forms
from API.models import Recipe_Search, Profile
from API.models import MEAL_TYPE, DIET_TYPE
from django.contrib.auth.models import User


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

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username']

class UpdateProfileForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['image', 'bio']
