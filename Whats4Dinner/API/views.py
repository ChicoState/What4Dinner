from API.form import LoginForm, RecipeSearchForm, SignUpForm, RecipeCreateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Create_Recipe

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
    
@login_required(login_url='/login/')
def create(request):
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
            }
            
            return render(request, "API/create.html", context)
        else:
            # If the form is not valid, render the form with error messages
            return render(request, "API/create.html", {'form': create_form})
    else:
        # If it's a GET request, render the form
        return render(request, "API/create.html", {'form': RecipeCreateForm()})




# @login_required(login_url='/login/')
# def create(request):
#     if (request.method== "POST"):
#         create_form = RecipeCreateForm(request.POST, request.FILES)
#         if create_form.is_valid():
#             Created = create_form.save()
            
#             Name = create_form.cleaned_data['Recipe_Name']
#             Ingrediants = create_form.cleaned_data['List_Ingredients']
#             Meal = create_form.cleaned_data['Meal_Type']
#             Health = create_form.cleaned_data['Health_Type']    
#             Diet = create_form.cleaned_data['Diet']
#             Calories = create_form.cleaned_data['Total_Calories']
#             Time = create_form.cleaned_data['Time_Needed']
#             image1 = create_form.cleaned_data['Upload_Image'] 
#             context = {
#             "form": RecipeCreateForm,
#             "Recipe_Name": Name,
#             "List_Ingredients": Ingrediants,
#             "Meal_Type": Meal,
#             "Health_Type": Health,
#             "Diet": Diet,
#             "Total_Calories": Calories,
#             "Time_Needed": Time,
#             "Upload_Image": image1,
#             }
#             Created(Recipe_Name=Name,List_Ingredients=Ingrediants,Meal_Type=Meal,Health_Type=Health,Diet=Diet,Total_Calories=Calories,Time_Needed=Time,Upload_Image=image1).save()
#     #     Create_Recipe(Create_RecipeName=Name,Create_Ingrediants=Ingrediants,Create_Meal_Type=Meal,Create_Health_Type=Health,Create_Diet=Diet,Create_Calories=Calories,Create_Time=Time,Upload_Image=image1).save()

#         return render(request, "API/create.html", context)
#     return render(request, "API/create.html", {'form': RecipeCreateForm}) 

    # else:
    #     context = {
    #         "form_data": RecipeCreateForm
    #     }
    #     return render(request, "API/create.html", context)


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
