from django.shortcuts import render, redirect  
from django.http import JsonResponse, HttpResponse
from .models import IssueCategory
from Employee.models import Employee
import json
from django.contrib import messages

from rest_framework.decorators import api_view    
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import JSONParser

#IssueCategory All API
@api_view(["GET"])
def all(request):    
    obj = IssueCategory.objects.all() 
    obj_json = IssueCategorySerializer(obj, many=True)
    show(obj_json.data)
    return Response({"message": "Success", "status": 200, "data":obj_json.data})

#IssueCategory One API
@api_view(["POST"])
def one(request):
    try:
        id=request.data['id']
        obj = IssueCategory.objects.get(id=id)
        obj_json = IssueCategorySerializer(obj)
        return Response({"message": "Success", "status": 200, "data":obj_json.data})
    except Exception as e:
         return Response({"message":str(e), "status":"201","data":[]})


#IssueCategory delete
@api_view(["POST"])
def delete(request):
    try:
        fetchid=request.data['id']
        fetchdata=IssueCategory.objects.filter(pk=fetchid).delete()
        return Response({"message": "Success", "status": 200, "data":[]})
    except Exception as e:
         return Response({"message":str(e), "status":"201","data":[]})

#IssueCategory Create API
@api_view(['POST'])
def create(request):
    try:
        Title = request.data["Title"]
        CreatedBy = request.data["CreatedBy"]
        CreatedDate = request.data["CreatedDate"]
        CreatedTime = request.data["CreatedTime"]

        model=IssueCategory(Title = Title,CreatedBy = CreatedBy,CreatedDate = CreatedDate,CreatedTime = CreatedTime)
        model.save()
        return Response({"message": "Success", "status": 200, "data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":201,"data":[]})
		
#IssueCategory Update API
@api_view(['POST'])
def update(request):
    try:
        fetchid = request.data['id']
        model = IssueCategory.objects.get(pk = fetchid)
        model.Title = request.data["Title"]
        model.CreatedBy = request.data["CreatedBy"]
        model.CreatedDate = request.data["CreatedDate"]
        model.CreatedTime = request.data["CreatedTime"]
        model.save()
        return Response({"message": "Success", "status": 200, "data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":201,"data":[]})

#{"filter":{"CreatedBy":116}, "fields":["id","Title","CreatedBy"]}
#IssueCategory Filter Listing 
@api_view(["POST"])
def filter(request):
    try:
        if IssueCategory.objects.filter(**request.data['filter']).exists():            
            objs = IssueCategory.objects.filter(**request.data['filter']).values(*request.data['fields']).order_by("-id")
            
            obj_json = IssueCategorySerializer(objs, many=True)
            print("obj_json.data")
            print(obj_json.data)
            if "CreatedBy" in request.data['fields']:
                show(obj_json.data)
            return Response({"message": "Success","status": 200,"data":obj_json.data})
        else:      
            return Response({"message": "Success","status": 200,"data":[]})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})

def show(objs):
    for obj in objs:
        if Employee.objects.filter(SalesEmployeeCode=obj['CreatedBy']).exists():
            CreatedByName = Employee.objects.filter(SalesEmployeeCode=obj['CreatedBy'])[0].SalesEmployeeName
            obj['CreatedByName'] = CreatedByName
            print("CreatedByName")		
            print(CreatedByName)
        else:
            obj['CreatedByName'] = ""
                        