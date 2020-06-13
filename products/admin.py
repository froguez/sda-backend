from django.contrib import admin
from products.models import Product, Dimension, Category

admin.site.register(Product)
admin.site.register(Dimension)
admin.site.register(Category)
