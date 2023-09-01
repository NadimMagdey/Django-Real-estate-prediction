from django.contrib import admin

# Register your models here.
from .models import  models,  Product

admin.site.register(Product)
