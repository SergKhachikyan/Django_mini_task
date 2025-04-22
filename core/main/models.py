from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 60)
    image = models.ImageField(upload_to='category_images')
    price = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length = 60)
    image = models.ImageField(upload_to='category_images')
    price = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name