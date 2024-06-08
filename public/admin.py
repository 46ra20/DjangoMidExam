from django.contrib import admin

# Register your models here.
from .models import CaregoryModel,ProductModel

admin.site.register(CaregoryModel)
admin.site.register(ProductModel)
