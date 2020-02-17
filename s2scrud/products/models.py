from django.db import models

# Create your models here.

class Attribute(models.Model):

    size = models.CharField(max_length=100)
    grams = models.CharField(max_length=100)
    foo = models.CharField(max_length=100)

    def __str__(self):
        return self.size


class Product(models.Model):

    sku = models.CharField(max_length=5, unique=True)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)

    def __str__(self):
        return self.sku