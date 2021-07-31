from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum
from .models import Transaction
from .serializers import TransactionSerializerView


# Create your views here.


class TransactionViewSet(viewsets.ModelViewSet):
    """
    Viewswet for Creating, Updating, Listing, Retrieving Transactions
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializerView
    lookup_field = 'pk'


class TransactionTypesView(APIView):
    """
    FUNCTIONALITY OF LISTING IDS OF IDS WITH THE GIVEN TYPE!
    """

    def get(self, request, type):
        """

        :return: List of ids
        """
        try:
            ids_list = Transaction.objects.filter(type=type).values_list('transaction_id', flat=True)
            return Response(ids_list, status.HTTP_200_OK)

        except Exception as e:
            return Response("Error", status=status.HTTP_400_BAD_REQUEST)


class TransactionSumView(APIView):
    """
    FUNCTIONALITY OF FINDING SUM OF ALL TRANSACTIONS LINKED!
    """

    def get(self, request, transaction_id):
        """
        Sum of all child transaction
        :param transaction_id:
        :param request: transaction_id
        :return: Sum of Amounts
        """
        try:
            transactions_sum = Transaction.objects.get_queryset_descendants(queryset=Transaction.objects.filter(transaction_id=transaction_id), include_self=True).aggregate(Sum('amount'))
            return Response(transactions_sum, status=status.HTTP_200_OK)

        except Exception as e:
            return Response("Error", status=status.HTTP_400_BAD_REQUEST)
