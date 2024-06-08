from django.shortcuts import render
from .models import ProductModel,CaregoryModel

# Create your views here.

def ShowCaregoryWise(request,category_id):
    category = CaregoryModel.objects.all()
    cars = ProductModel.objects.filter(category_id=category_id)
    return render(request,'homepage.html',{'category':category,'cars':cars})

def ShowCarDetails(request,id):
    car = ProductModel.objects.get(pk=id)
    return render(request,'car_details.html',{'car':car})

