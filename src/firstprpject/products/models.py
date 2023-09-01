from django.db import models

# Create your models here.
from django.db.models import Model


class Product(Model):
    title = models.CharField(max_length=120)  # max-length os default here
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=2.3)
    summary = models.TextField(default='this is summary')
    featured = models.BooleanField(default=True)
    # blank for input field (required)
    # null for database migration (code)
