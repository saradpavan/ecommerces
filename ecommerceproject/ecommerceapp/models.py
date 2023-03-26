from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.EmailField()
    Name = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)


class Product(models.Model):
    product_id =models.AutoField
    product_name=models.CharField(max_length=50)
    category = models.CharField(max_length=100,default="")
    subcategory = models.CharField(max_length=100,default="")
    price = models.IntegerField(default="0")
    desc = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.product_name

