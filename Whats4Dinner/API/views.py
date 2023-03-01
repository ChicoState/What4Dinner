from django.shortcuts import render
from API.form import RecipeSearchForm


# Create your views here.

def home(request):
    return render(request, "API/home.html")

def about(request):
    return render(request, "API/about.html")

def search(request):
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
    

    
