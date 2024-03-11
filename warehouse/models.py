from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=128)
    product_code = models.IntegerField(default=0)


class Material(models.Model):
    title = models.CharField(max_length=128)


class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)


class Warehouse(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    remainder = models.IntegerField(default=0)
    price = models.FloatField()
