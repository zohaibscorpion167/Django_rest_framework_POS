from django.shortcuts import render, HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from .models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import JSONParser



class RestaurantApiView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]
    def get(self, request):
        restaurants= Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class OrderDetailsApi(APIView):
    def get_object(self,Order_ID):
        try:
            return Restaurant.objects.get(Order_ID=Order_ID)

        except Restaurant.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request,Order_ID):
        order = self.get_object(Order_ID)
        serializer = RestaurantSerializer(order)
        return Response(serializer.data)

    def put(self, request,Order_ID):
        order = self.get_object(Order_ID)
        serializer = RestaurantSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,Order_ID):
        order= self.get_object(Order_ID)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    