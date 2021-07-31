from decimal import Decimal

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Modules


class Transaction(MPTTModel):
    transaction_id = models.BigAutoField(primary_key=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    type = models.CharField(max_length=20)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return f"{self.transaction_id}"
