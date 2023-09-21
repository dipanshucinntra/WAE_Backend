from django.shortcuts import render, redirect  
from django.http import JsonResponse, HttpResponse
from .models import Form
import json
from django.contrib import messages

from rest_framework.decorators import api_view    
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import JSONParser

#Form All API
@api_view(["GET"])
def all(request):    
    obj = Form.objects.all() 
    obj_json = FormSerializer(obj, many=True)
    return Response({"message": "Success", "status": 200, "data":obj_json.data})

#Form One API
@api_view(["POST"])
def one(request):
    try:
        id=request.data['id']
        obj = Form.objects.get(id=id)
        obj_json = FormSerializer(obj)
        return Response({"message": "Success", "status": 200, "data":obj_json.data})
    except Exception as e:
         return Response({"message":str(e), "status":"201","data":[]})


#Form delete
@api_view(["POST"])
def delete(request):
    try:
        fetchid=request.data['id']
        fetchdata=Form.objects.filter(pk=fetchid).delete()
        return Response({"message": "Success", "status": 200, "data":[]})
    except Exception as e:
         return Response({"message":str(e), "status":"201","data":[]})

#Form Create API
@api_view(['POST'])
def create(request):
    try:
        Title = request.data["Title"]
        CreatedBy = request.data["CreatedBy"]
        CreatedDate = request.data["CreatedDate"]
        CreatedTime = request.data["CreatedTime"]
        Data = request.data["Data"]

        model=Form(Title = Title,CreatedBy = CreatedBy,CreatedDate = CreatedDate,CreatedTime = CreatedTime,Data = Data)
        model.save()
        return Response({"message": "Success", "status": 200, "data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":201,"data":[]})
		
#Form Update API
@api_view(['POST'])
def update(request):
    try:
        fetchid = request.data['id']
        model = Form.objects.get(pk = fetchid)
        model.Title = request.data["Title"]
        model.CreatedBy = request.data["CreatedBy"]
        model.CreatedDate = request.data["CreatedDate"]
        model.CreatedTime = request.data["CreatedTime"]
        model.Data = request.data["Data"]
        model.save()
        return Response({"message": "Success", "status": 200, "data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":201,"data":[]})
		