from django.shortcuts import render
from account.models import Restaurant  

def homepage(request):
    restaurant_name = None
    restaurant = Restaurant.objects.first()
    if restaurant:
        restaurant_name = restaurant.name
    
    return render(request, 'home.html', {'restaurant_name': restaurant_name})