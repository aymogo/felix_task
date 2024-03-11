from django.contrib import admin
from .models import Product, Material, ProductMaterial, Warehouse, OrderProduct

admin.site.register(Product)
admin.site.register(Material)
admin.site.register(ProductMaterial)
admin.site.register(Warehouse)
admin.site.register(OrderProduct)