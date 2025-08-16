from django.shortcuts import render

def homepage(request):
    restaurant_name = "My Awesome Restaurant"  # or fetch from model/settings
    return render(request, "home/homepage.html", {"restaurant_name": restaurant_name})