from django.shortcuts import render
from public.models import CaregoryModel,ProductModel


def Home(request):
    category = CaregoryModel.objects.all()
    cars = ProductModel.objects.all()
    return render(request,'homepage.html',{'category':category,'cars':cars})