import random
from API.form import (LoginForm, RecipeSearchForm, SignUpForm,
                      UpdateProfileForm, UpdateUserForm, RecipeCreateForm)
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import CreateRecipe, RecomendedRecipes
from .API_data import get_api_data, parse_api_data
import urllib.parse

from decouple import config

# from django.contrib.auth.forms import SignUp

# Create your views here.

@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return redirect("/")

def home(request):
    return render(request, "API/home.html")


def about(request):
    return render(request, "API/about.html")

# def search_api(request):
#     print(request.body)
#     endpoint = "https://api.edamam.com/api/recipes/v2"
#     query = request.body
#     app_id = config("RECPIE_APPLICATION_ID")
#     secret_key = config("RECIPE_SEARCH_API_KEY")
#     # https://api.edamam.com/api/recipes/v2?type=public&q=chicken&app_id=f93954c5&app_key=76167920eae1f7ffb1d134d573e1b9a0%20
#     url = urllib.parse.quote_plus(
#         endpoint+"?type=public"+"&q="+query+"&app_id="+app_id+"&app_key="+secret_key)
#     print(url)

def search(request):
    if request.method == "POST":
        search_api(request)
    return render(request, "API/search.html")

@login_required(login_url='/login/')
def userprofile(request):
    return render(request, "API/userprofile.html")


def search_api(request):
    print(request.body)
    endpoint = "https://api.edamam.com/api/recipes/v2"
    query = request.body
    app_id = config("RECPIE_APPLICATION_ID")
    secret_key = config("RECIPE_SEARCH_API_KEY")
    # https://api.edamam.com/api/recipes/v2?type=public&q=chicken&app_id=f93954c5&app_key=76167920eae1f7ffb1d134d573e1b9a0%20
    url = urllib.parse.quote_plus(
        endpoint+"?type=public"+"&q="+query+"&app_id="+app_id+"&app_key="+secret_key)
    print(url)
    if (request.method== "POST"):
        form = RecipeSearchForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['Recipe_Name']
            text2 = form.cleaned_data['Ingrediants']
            text3 = form.cleaned_data['Meal_Type']
            text4 = form.cleaned_data['Diet']
            text5 = form.cleaned_data['Calories']
            text6 = form.cleaned_data['Time']
            print(text)
            print(text2)
            print(text3)
            print(text4)
            print(text5)
            print(text6)
        context = {
            "form_data": RecipeSearchForm,
            "Recipe_Name": text,
            "Ingrediants": text2,
            "Meal_Type": text3,
            "Diet": text4,
            "Calories": text5,
            "Time": text6
        }
        return render(request, "API/search.html", context)

    else:
        context = {
            "form_data": RecipeSearchForm
        }
        return render(request, "API/search.html", context)

def signup(request):
    if (request.method == "POST"):
        signup_form = SignUpForm(request.POST)
        if (signup_form.is_valid()):
            user = signup_form.save()
            user.set_password(user.password)
            user.save()
            return redirect("/")
        else:
            page_data = { "signup_form": signup_form }
            return render(request, "API/signup.html", page_data)
    else:
        signup_form = SignUpForm()
        page_data = { "signup_form": signup_form }
        return render(request, "API/signup.html", page_data)
def user_login(request):
    if(request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return redirect(userprofile)

                else:
                    return HttpResponseRedirect("Your account is not setup.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return render(request, 'API/login.html', {"login_form": LoginForm})
        else:
            return render(request, "API/login.html", {"login_form": LoginForm})
    else:
            return render(request, "API/login.html", {"login_form": LoginForm})

@login_required(login_url='/login/')
def updateProfile(request):
    if request.method == 'POST':
        updateUser = UpdateUserForm(request.POST, instance=request.user)
        updateProfile = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if updateUser.is_valid() and updateProfile.is_valid():
            updateUser.save()
            updateProfile.save()
            messages.success(request, f'Your account has been updated!')
            return redirect(userprofile) # Redirect back to profile page

    else:
        updateUser = UpdateUserForm(instance=request.user)
        updateProfile = UpdateProfileForm(instance=request.user.profile)

    context = {
        'updateUser': updateUser,
        'updateProfile': updateProfile
    }

    return render(request, 'API/updateProfile.html', context)
