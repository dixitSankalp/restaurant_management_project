from django.conf import settings
from django.shortcuts import render

def homepage(request):
    restaurant_name = settings.RESTAURANT_NAME
    restaurant_phone = settings.RESTAURANT_PHONE
    return render(request, "home/homepage.html", {
        "restaurant_name": restaurant_name,
        "restaurant_phone": restaurant_phone,
    })

def contact_us(request):
    return render(request, "home/contact.html")