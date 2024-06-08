from django.db import models

# Create your models here.

class CaregoryModel(models.Model):
    category_name = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.category_name

class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(CaregoryModel,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

