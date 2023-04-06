from API.form import LoginForm, RecipeSearchForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from API.form import UpdateUserForm, UpdateProfileForm
from .API_data import get_api_data, parse_api_data

#from django.contrib.auth.forms import SignUp

# Create your views here.


@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return redirect("/")


def home(request):
    return render(request, "API/home.html")


def about(request):
    return render(request, "API/about.html")


@login_required(login_url='/login/')
def userprofile(request):
    return render(request, "API/userprofile.html")

@login_required(login_url='/login/')
def edit_profile(request):
   return render(request, "API/editProfile.html")


@login_required(login_url='/login/')
def search(request):
    if (request.method == "POST"):
        form = RecipeSearchForm(request.POST)
        if form.is_valid():
            recipe_name = form.cleaned_data['Recipe_Name']
            num_of_ingredients = form.cleaned_data['Number_Of_Ingredients']
            meal_type = form.cleaned_data['Meal_Type']
            health_type = form.cleaned_data['Health_Type']
            diet = form.cleaned_data['Diet']
            calories = form.cleaned_data['Calorie_Range']
            time = form.cleaned_data['Max_Amount_Of_Time']
            res = get_api_data(query=recipe_name, num_of_ingredients=num_of_ingredients, diet_type=diet,
                               health_type=health_type, meal_type=meal_type, calories=calories, time=time)
            parsed_data = parse_api_data(res.json())
            # Sorts the recipes by recipe name
            parsed_data.sort(key=lambda x: x['label'], reverse=False)
            print(parsed_data)
            context = {
                "form_data": RecipeSearchForm,
                "num_results": len(parsed_data),
                "parsed_data": parsed_data,
            }
            return render(request, "API/search.html", context)
        else:
            context = {
                "form_data": RecipeSearchForm
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
            return render(request, "API/login.html")
        else:
            page_data = {"signup_form": signup_form}
            return render(request, "API/signup.html", page_data)
    else:
        signup_form = SignUpForm()
        page_data = {"signup_form": signup_form}
        return render(request, "API/signup.html", page_data)


def user_login(request):
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect(userprofile)
                else:
                    return HttpResponseRedirect("There is no account associated with that username.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(
                    username, password))
                return render(request, 'API/login.html', {"login_form": LoginForm})
        else:
            return render(request, "API/login.html", {"login_form": LoginForm})
    else:
        return render(request, "API/login.html", {"login_form": LoginForm})



@login_required(login_url='/login/')
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(userprofile)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user)

    return render(request, 'API/editProfile.html', {'user_form': user_form, 'profile_form': profile_form})
