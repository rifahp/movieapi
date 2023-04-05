from django.shortcuts import render
from rest_framework.views import APIView
from.models import Dishes
from rest_framework.response import Response

# Create your views here.

class DishList(APIView):
    def get(self,request,*args,**kwargs):
        return Response(data=Dishes)
    def post(self,request,*args,**kwargs):
        data=request.data
        Dishes.append(data)
        return Response(data=Dishes)

