'''
Forms for the application
'''

from django import forms
from django.contrib.auth.models import User

from .models import DIET_TYPE, HEALTH_TYPE, MEAL_TYPE, CreateRecipe, Profile

# from django.contrib.auth.models import Create_Recipe


class RecipeSearchForm(forms.Form):
    '''
    Recipe search form fields
    '''
    Recipe_Name = forms.CharField(widget=forms.TextInput())
    Ingrediants = forms.CharField(widget=forms.TextInput(), required=False)
    Meal_Type = forms.CharField(
        label='Meal Type', widget=forms.Select(choices=MEAL_TYPE), required=False)
    # Health_type=forms.CharField(max_length=40)
    Diet = forms.CharField(
        label='Diet Type', widget=forms.Select(choices=DIET_TYPE), required=False)
    Calories = forms.IntegerField(widget=forms.NumberInput(), required=False)
    Time = forms.IntegerField(widget=forms.NumberInput(), required=False)
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
    '''
    Create Recipe form fields
    '''
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
        '''
        Meta Create Recipe fields
        '''
        model = CreateRecipe
        fields = ['Recipe_Name', 'List_Ingredients', 'Meal_Type', 'Health_Type',
                  'Diet', 'Total_Calories', 'Time_Needed', 'Instructions', 'Upload_Image']


class SignUpForm(forms.ModelForm):
    '''
    User signup form fields
    '''
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        '''
        Metadata for the User model
        '''
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        help_texts = {
            'username': None
        }


class LoginForm(forms.Form):
    '''
    Login form fields
    '''
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class UpdateUserForm(forms.ModelForm):
    '''
    Update Username
    '''
    username = forms.CharField(max_length=100, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        '''
        metadata for update user
        '''
        model = User
        fields = ['username']


class UpdateProfileForm(forms.ModelForm):
    '''
    Update User profile
    '''
    image = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        '''
        metadata update profile
        '''
        model = Profile
        fields = ['image', 'bio']
