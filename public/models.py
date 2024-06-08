from django.db import models

# Create your models here.

class CaregoryModel(models.Model):
    category_name = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.category_name

class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(CaregoryModel,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

class Comments(models.Model):
    name = models.CharField(max_length=30)
    title=models.CharField(max_length=100)
    comment = models.TextField()
    comment_link = models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name+self.title