from django.shortcuts import render, redirect  
from django.http import JsonResponse, HttpResponse
from .models import *
from Employee.models import Employee
import requests, json
from random import randint
from rest_framework.decorators import api_view    
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import JSONParser
# Create your views here.  

#Create Category 
@api_view(['POST'])
def create(request):
    try:
        GroupName = request.data['GroupName']
        object = Category.objects.last()
        Number = int(object.Number)+1
        json = {
            "GroupName":GroupName,
            "Number":str(Number)
        }
        serializer = CategorySerializer(data=json)
        if serializer.is_valid():
            serializer.save()
        return Response({"message": "Success","status": 200}, status=200)
    except Exception as e:
        print(str(e))   
        return Response({"message": str(e),"status": 200}, status=500) 

#Update Category     
@api_view(['POST'])
def update(request):
    try:
        Id = request.data['id']
        GroupName = request.data['GroupName']
        object = Category.objects.get(id=Id)
        json = {
            "GroupName":GroupName,
        }
        serializer = CategorySerializer(object, data=json, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response({"message": "Success","status": 200}, status=200)
    except Exception as e:
        print(str(e))   
        return Response({"message": str(e),"status": 200}, status=500)     

#Category All API
@api_view(["GET"])
def all(request):
    cat_obj = Category.objects.all()
    cat_json = CategorySerializer(cat_obj, many=True)
    return Response({"message": "Success","status": 200,"data":cat_json.data})

#Category All API
@api_view(["POST"])
def all_filter(request):
    SalesEmployeeCode = request.data['SalesEmployeeCode']
    emp = Employee.objects.get(SalesEmployeeCode=SalesEmployeeCode)
    if emp.role=='admin':
        cat_obj = Category.objects.all()
        cat_json = CategorySerializer(cat_obj, many=True)
        return Response({"message": "Success","status": 200,"data":cat_json.data})
    else:
        div = emp.div
        try:
            div = div.split(",")
            print(div)
            cat_obj = Category.objects.filter(Number__in=div)
            cat_json = CategorySerializer(cat_obj, many=True)
            return Response({"message": "Success","status": 200,"data":cat_json.data})
        except Exception as e:
            return Response({"message": str(e),"status": 201,"data":[]})


#Category One API
@api_view(["POST"])
def one(request):
    Number=request.data['Number']
    cat_obj = Category.objects.get(Number=Number)
    cat_json = CategorySerializer(cat_obj, many=False)
    return Response({"message": "Success","status": 200,"data":cat_json.data})
