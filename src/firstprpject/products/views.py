from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm, ProductRawForm


# Create your views here.
def home_view(request, *args, **kwargs):
    if request.method == 'POST':
        longitude = request.POST.get("longitude")
        latitude = request.POST.get("latitude")
        housing_median_age = request.POST.get("housing_median_age")

        total_rooms = request.POST.get("total_rooms")
        total_bedrooms = request.POST.get("total_bedrooms")
        population = request.POST.get("population")
        households = request.POST.get("households")
        median_income = request.POST.get("median_income")

        median_house_value = request.POST.get("median_house_value")
        ocean_proximity = request.POST.get("ocean_proximity")

        predicted_value = "predicted_value"

        context = {'pred': predicted_value}
        return render(request, 'product/home.html', context=context)

    else:
        context = {}
        return render(request, 'product/home.html', context=context)


