from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "API/home.html")

def about(request):
    return render(request, "API/about.html")

def search(request):
    return render(request, "API/search.html")