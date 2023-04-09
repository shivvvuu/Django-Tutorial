from django.shortcuts import render
from .serializer import StockSerializer
from rest_framework.response import Response
# Create your views here.
from .models import Stock
from rest_framework.views import APIView

class StockList(APIView):
    
    def get(self, request):
        stock = Stock.objects.all()
        serializer = StockSerializer(stock, many=True)
        
        return Response(serializer.data)
        
    def post(self, request):
        pass