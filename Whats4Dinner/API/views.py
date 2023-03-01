import urllib.parse

from decouple import config
from django.shortcuts import render
from API.form import RecipeSearchForm


# Create your views here.


def home(request):
    return render(request, "API/home.html")


def about(request):
    return render(request, "API/about.html")


def search(request):
    if request.method == "POST":
        search_api(request)
    return render(request, "API/search.html")


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
            print(text)  
            print(text2)  
            print(text3)  
        context = {
            "form_data": RecipeSearchForm,
            "Recipe_Name": text,
            "Ingrediants": text2,
            "Meal_Type": text3
        }
        return render(request, "API/search.html", context)

    else:
        context = {
            "form_data": RecipeSearchForm
        }
        return render(request, "API/search.html", context)
