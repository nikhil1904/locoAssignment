# Packages
from abc import ABC

from rest_framework import serializers
import random

# Modules
from .models import Transaction


class TransactionSerializerView(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['transaction_id', 'type', 'amount', 'parent']
