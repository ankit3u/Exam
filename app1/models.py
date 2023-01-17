from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()
    price=models.DecimalField(max_digits=5,decimal_places=3)
