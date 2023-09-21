from django.shortcuts import render, redirect  
from django.http import JsonResponse, HttpResponse
from .models import Issue
import json
from django.contrib import messages

from rest_framework.decorators import api_view    
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import JSONParser

from Inspection.IssueCategory.models import IssueCategory
from Employee.models import Employee

#Issue All API
@api_view(["GET"])
def all(request):    
    obj = Issue.objects.all() 
    obj_json = IssueSerializer(obj, many=True)
    show(obj_json.data)
    return Response({"message": "Success", "status": 200, "data":obj_json.data})

#Issue One API
@api_view(["POST"])
def one(request):
    try:
        id=request.data['id']
        obj = Issue.objects.filter(id=id)
        obj_json = IssueSerializer(obj, many=True)
        show(obj_json.data)
        return Response({"message": "Success", "status": 200, "data":obj_json.data})
    except Exception as e:
         return Response({"message":str(e), "status":"201","data":[]})


#Issue delete
@api_view(["POST"])
def delete(request):
    try:
        fetchid=request.data['id']
        fetchdata=Issue.objects.filter(pk=fetchid).delete()
        return Response({"message": "Success", "status": 200, "data":[]})
    except Exception as e:
         return Response({"message":str(e), "status":"201","data":[]})

#Issue Create API
@api_view(['POST'])
def create(request):
    try:
        Title = request.data["Title"]
        IssueCategory = request.data["IssueCategory"]
        CreatedBy = request.data["CreatedBy"]
        CreatedDate = request.data["CreatedDate"]
        CreatedTime = request.data["CreatedTime"]

        model=Issue(Title = Title,IssueCategory = IssueCategory,CreatedBy = CreatedBy,CreatedDate = CreatedDate,CreatedTime = CreatedTime)
        model.save()
        return Response({"message": "Success", "status": 200, "data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":201,"data":[]})
		
#Issue Update API
@api_view(['POST'])
def update(request):
    try:
        fetchid = request.data['id']
        model = Issue.objects.get(pk = fetchid)
        model.Title = request.data["Title"]
        model.IssueCategory = request.data["IssueCategory"]
        model.save()
        return Response({"message": "Success", "status": 200, "data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":201,"data":[]})

#{"filter":{"CreatedBy":116}, "fields":["id","Title"]}
#Issue Filter Listing 
@api_view(["POST"])
def filter(request):
    try:
        if Issue.objects.filter(**request.data['filter']).exists():            
            objs = Issue.objects.filter(**request.data['filter']).values(*request.data['fields']).order_by("-id")
            
            obj_json = IssueSerializer(objs, many=True)
            if "CreatedBy" in request.data['fields']:
                show(obj_json.data)
            return Response({"message": "Success","status": 200,"data":obj_json.data})
        else:      
            return Response({"message": "Success","status": 200,"data":[]})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})


#IssueCategoryName = IssueCategory.objects.filter(pk=obj['IssueCategory']).values('id', "Title")[0]
#IssueCategoryName = IssueCategory.objects.filter(pk=obj['IssueCategory'])[0].Title
def show(objs):
    for obj in objs:
        if Employee.objects.filter(SalesEmployeeCode=obj['CreatedBy']).exists():
            CreatedByName = Employee.objects.filter(SalesEmployeeCode=obj['CreatedBy'])[0].SalesEmployeeName
            obj['CreatedByName'] = CreatedByName
            print("CreatedByName")		
            print(CreatedByName)
        else:
            obj['CreatedByName'] = ""
                            