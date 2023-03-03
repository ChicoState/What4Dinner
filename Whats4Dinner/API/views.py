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
            "form_data": RecipeSearchForm()
        }
        return render(request, "API/search.html", context)
    

    
