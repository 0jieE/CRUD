from django.db import models
from decimal import Decimal

class Fruits(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))

