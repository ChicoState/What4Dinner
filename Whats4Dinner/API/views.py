'''
All views for the website
'''
import random

from API.form import (LoginForm, RecipeCreateForm, RecipeSearchForm,
                      SignUpForm, UpdateProfileForm, UpdateUserForm)
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from .api_data import get_api_data, parse_api_data
from .models import CreateRecipe, RecomendedRecipes

# from django.contrib.auth.forms import SignUp

# Create your views here.


@login_required(login_url='/login/')
def user_logout(request):
    '''
    User logout view
    '''
    logout(request)
    return redirect("/")


def home(request):
    '''
    Random Recipe View.
    '''
    try:
        recipe = random.choice(RecomendedRecipes.objects.all())
    except IndexError:
        recipe = ""
    print(recipe)  # make sure that the recipe object is being retrieved correctly
    return render(request, 'API/home.html', {'recipe': recipe})


def about(request):
    '''
    About page view
    '''
    return render(request, "API/about.html")


@login_required(login_url='/login/')
def userprofile(request):
    '''
    User profile view
    '''
    return render(request, "API/userprofile.html")


@login_required(login_url='/login/')
def edit_profile(request):
    '''
    Edit profile view
    '''
    return render(request, "API/editProfile.html")


@login_required(login_url='/login/')
def search(request):
    '''
    Search page view
    '''
    if request.method == "POST":
        form = RecipeSearchForm(request.POST)
        if form.is_valid():
            recipe_name = form.cleaned_data['Recipe_Name']
            num_of_ingredients = form.cleaned_data['Number_Of_Ingredients']
            meal_type = form.cleaned_data['Meal_Type']
            health_type = form.cleaned_data['Health_Type']
            diet = form.cleaned_data['Diet']
            calories = form.cleaned_data['Calorie_Range']
            time = form.cleaned_data['Max_Amount_Of_Time']
            res = get_api_data(query=recipe_name,
                               num_of_ingredients=num_of_ingredients,
                               diet_type=diet,
                               health_type=health_type,
                               meal_type=meal_type,
                               calories=calories,
                               time=time)
            parsed_data = parse_api_data(res.json())
            # Sorts the recipes by recipe name
            # parsed_data.sort(key=lambda x: x['label'], reverse=False)
            context = {
                "form_data": RecipeSearchForm,
                "num_results": len(parsed_data),
                "parsed_data": parsed_data,
            }
            return render(request, "API/search.html", context)
        context = {
            "form_data": RecipeSearchForm
        }
        return render(request, "API/search.html", context)
    context = {
        "form_data": RecipeSearchForm
    }
    return render(request, "API/search.html", context)


@login_required(login_url='/login/')
def create(request):
    '''
    Create Page view
    '''
    if request.method == "POST":
        create_form = RecipeCreateForm(request.POST, request.FILES)
        if create_form.is_valid():
            # Create a Recipe object and set its attributes
            recipe = create_form.save(commit=False)
            recipe.Create_RecipeName = create_form.cleaned_data['Recipe_Name']
            recipe.Create_Ingrediants = create_form.cleaned_data['List_Ingredients']
            recipe.Create_Meal_Type = create_form.cleaned_data['Meal_Type']
            recipe.Create_Health_Type = create_form.cleaned_data['Health_Type']
            recipe.Create_Diet = create_form.cleaned_data['Diet']
            recipe.Create_Calories = create_form.cleaned_data['Total_Calories']
            recipe.Create_Time = create_form.cleaned_data['Time_Needed']
            recipe.Create_Instruct = create_form.cleaned_data['Instructions']
            recipe.Upload_Image = create_form.cleaned_data['Upload_Image']
            recipe.save()

            # Set the context with the values of the Recipe object
            context = {
                "form": RecipeCreateForm,
                "Recipe_Name": recipe.Create_RecipeName,
                "List_Ingredients": recipe.Create_Ingrediants,
                "Meal_Type": recipe.Create_Meal_Type,
                "Health_Type": recipe.Create_Health_Type,
                "Diet": recipe.Create_Diet,
                "Total_Calories": recipe.Create_Calories,
                "Time_Needed": recipe.Create_Time,
                "Instructions": recipe.Create_Instruct,
                "Upload_Image": recipe.Upload_Image,
                "message": "Recipe created successfully!",
            }

            # Add success message to messages framework
            messages.success(request, 'Recipe created successfully!')

            return render(request, "API/create.html", context)
        # If the form is not valid, render the form with error messages
        return render(request, "API/create.html", {'form': create_form})
    # If it's a GET request, render the form
    return render(request, "API/create.html", {'form': RecipeCreateForm()})


def signup(request):
    '''
    User signup view
    '''
    if request.method == "POST":
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            user.set_password(user.password)
            user.save()
            return render(request, "API/login.html")
        page_data = {"signup_form": signup_form}
        return render(request, "API/signup.html", page_data)
    signup_form = SignUpForm()
    page_data = {"signup_form": signup_form}
    return render(request, "API/signup.html", page_data)


def user_login(request):
    '''
    User login view
    '''
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect(userprofile)
                return HttpResponseRedirect("There is no account \
                                            associated with that username.")
            print("Someone tried to login and failed.")
            print(
                f"They used username: {username} and password: {password}")
            return render(request, 'API/login.html', {"login_form": LoginForm})
        return render(request, "API/login.html", {"login_form": LoginForm})
    return render(request, "API/login.html", {"login_form": LoginForm})


@login_required(login_url='/login/')
def profile(request):
    '''
    User profile view.
    '''
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(
            request.POST, request.FILES, instance=request.user)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(userprofile)
    user_form = UpdateUserForm(instance=request.user)
    profile_form = UpdateProfileForm(instance=request.user)
    return render(request, 'API/editProfile.html',
                  {'user_form': user_form, 'profile_form': profile_form})


@login_required(login_url='/login/')
def recipe_details(request):
    '''
    Created Recipe View.
    '''
    recipe_obj = CreateRecipe.objects.all()
    return render(request, 'API/recipes.html',
                  {'recipe_obj': recipe_obj})
