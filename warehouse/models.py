from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=128)
    product_code = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Material(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField()
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title + " " + str(self.quantity)


class Warehouse(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    remainder = models.IntegerField(default=0)
    price = models.FloatField()

    def __str__(self):
        return self.material.title


class OrderProduct(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name.title + " " + str(self.product_qty)
