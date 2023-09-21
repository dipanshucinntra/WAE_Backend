from django.shortcuts import render, redirect  
from django.http import JsonResponse, HttpResponse
from .models import Inspection
import json
from django.contrib import messages

from rest_framework.decorators import api_view    
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import JSONParser

#Inspection All API
@api_view(["GET"])
def all(request):    
    obj = Inspection.objects.all() 
    obj_json = InspectionSerializer(obj, many=True)
    return Response({"message": "Success", "status": 200, "data":obj_json.data})

#Inspection One API
@api_view(["POST"])
def one(request):
    try:
        id=request.data['id']
        obj = Inspection.objects.get(id=id)
        obj_json = InspectionSerializer(obj)
        return Response({"message": "Success", "status": 200, "data":obj_json.data})
    except Exception as e:
         return Response({"message":str(e), "status":"201","data":[]})


#Inspection delete
@api_view(["POST"])
def delete(request):
    try:
        fetchid=request.data['id']
        fetchdata=Inspection.objects.filter(pk=fetchid).delete()
        return Response({"message": "Success", "status": 200, "data":[]})
    except Exception as e:
         return Response({"message":str(e), "status":"201","data":[]})

#Inspection Create API
@api_view(['POST'])
def create(request):
    try:
        IssueType = request.data["IssueType"]
        Description = request.data["Description"]
        TicketId = request.data["TicketId"]
        CreatedBy = request.data["CreatedBy"]
        CreatedDate = request.data["CreatedDate"]
        CreatedTime = request.data["CreatedTime"]

        model=Inspection(IssueType = IssueType,Description = Description,TicketId = TicketId,CreatedBy = CreatedBy,CreatedDate = CreatedDate,CreatedTime = CreatedTime)
        model.save()
        return Response({"message": "Success", "status": 200, "data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":201,"data":[]})
		
#Inspection Update API
@api_view(['POST'])
def update(request):
    try:
        fetchid = request.data['id']
        model = Inspection.objects.get(pk = fetchid)
        model.IssueType = request.data["IssueType"]
        model.Description = request.data["Description"]
        model.TicketId = request.data["TicketId"]
        model.CreatedBy = request.data["CreatedBy"]
        model.CreatedDate = request.data["CreatedDate"]
        model.CreatedTime = request.data["CreatedTime"]
        model.save()
        return Response({"message": "Success", "status": 200, "data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":201,"data":[]})

#{"filter":{"CreatedBy":112, "IssueType": "Wire"}, "fields":["id","IssueType","Description","TicketId"]}
#Inspection Filter Listing 
@api_view(["POST"])
def filter(request):
    try:
        if Inspection.objects.filter(**request.data['filter']).exists():            
            objs = Inspection.objects.filter(**request.data['filter']).values(*request.data['fields']).order_by("-id")
            obj_json = InspectionSerializer(objs, many=True)
            return Response({"message": "Success","status": 200,"data":obj_json.data})
        else:      
            return Response({"message": "Success","status": 200,"data":[]})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})

