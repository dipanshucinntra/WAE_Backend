from django.shortcuts import render, redirect  
from django.http import JsonResponse, HttpResponse
#from .forms import DropDownForm  
from .models import DropDown, StaticDropDown  
from Tickets.models import *  
import requests, json

from django.contrib import messages

from rest_framework.decorators import api_view    
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import DropDownSerializer, StaticDropDownSerializer
from rest_framework.parsers import JSONParser
# Create your views here.  
from django.conf import settings

#DropDown Create API
@api_view(['POST'])

def create(request):
    try:
        print(request.data)
        request.data['Data'] = json.dumps(request.data['Data'])
        
        DropDownName= request.data['DropDownName']
        Data= request.data['Data']
        DropDownValue= request.data['DropDownValue']
        DropDownDescription= request.data['DropDownDescription']
        Parent= request.data['Parent']
        Field1= request.data['Field1']
        Field2= request.data['Field2']
        Field3= request.data['Field3']
        Field4= request.data['Field4']
        Field5= request.data['Field5']
        CreatedBy= request.data['CreatedBy']
        CreateDate= request.data['CreateDate']
        CreateTime= request.data['CreateTime']
        UpdateDate= request.data['UpdateDate']
        UpdateTime= request.data['UpdateTime']
        UpdatedBy= request.data['UpdatedBy']

        model = DropDown(DropDownName=DropDownName, Data=Data, DropDownValue=DropDownValue, DropDownDescription=DropDownDescription, Parent=Parent, Field1=Field1, Field2=Field2, Field3=Field3, Field4=Field4, Field5=Field5, CreatedBy_id=CreatedBy, CreateDate=CreateDate, CreateTime=CreateTime, UpdateDate=UpdateDate, UpdateTime=UpdateTime, UpdatedBy_id=UpdatedBy)
        model.save()
        dd = DropDown.objects.latest('id').id

        print(request.data['DropDownName'])
        print(request.data['Field1'])
        if request.data['DropDownName'] == "Checklist":
            tktObj = Tickets.objects.filter(Type = request.data['Field1']).exclude(Status="Resolved")
            if len(tktObj) != 0:
                for obj in tktObj:
                    print(obj)
                    print("o type", obj.Type)
                    print("dd", request.data['DropDownValue'])
                    TicketChecklist(
                        TicketId = obj.id,
                        Name = request.data['DropDownValue'],
                        Description = request.data['DropDownDescription'],
                        Data = request.data['Data'],
                        Comment = "",
                        Duration = ""
                    ).save()
            
            return Response({"message":"successful", "status":200,"data":[]})
        else:
            return Response({"message":"Not valid", "status":201,"data":[]})
    except Exception as e:
        return Response({"message":str(e), "status":201, "data":[]})


def create_old(request):
    try:
        print(request.data)
        request.data['Data'] = json.dumps(request.data['Data'])
        
        
        cby = Employee.objects.get(SalesEmployeeCode=request.data['CreatedBy'])
        uby = Employee.objects.get(SalesEmployeeCode=request.data['UpdatedBy'])
        
        request.data['CreatedBy'] = cby
        request.data['UpdatedBy'] = uby
        
        #dd = DropDownSerializer(instance=cby, instance=uby, data=request.data, many=True) 
        dd = DropDownSerializer(data=request.data) 
        
        if DropDown.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This data already exists')
     
        if dd.is_valid():
            dd.save()
            print(request.data['DropDownName'])
            print(request.data['Field1'])
            if request.data['DropDownName'] == "Checklist":
                tktObj = Tickets.objects.filter(Type = request.data['Field1']).exclude(Status="Resolved")
                if len(tktObj) != 0:
                    for obj in tktObj:
                        print(obj)
                        print("o type", obj.Type)
                        print("dd", request.data['DropDownValue'])
                        TicketChecklist(
                            TicketId = obj.id,
                            Name = request.data['DropDownValue'],
                            Description = request.data['DropDownDescription'],
                            Data = request.data['Data'],
                            Comment = "",
                            Duration = ""
                        ).save()
            
            return Response({"message":"successful", "status":200,"data":[]})
        else:
            return Response({"message":"Not valid", "status":201,"data":[]})
    except Exception as e:
        return Response({"message":str(e), "status":201, "data":[]})

#DropDown All API
@api_view(["GET"])
def all(request):
    try:
        if request.query_params:
            dds = DropDown.objects.filter(**request.query_params.dict()).order_by('-id')
        else:
            dds = DropDown.objects.all().order_by('-id')
        
        if dds:
            serializer = DropDownSerializer(dds, many=True)
            return Response({"message": "Success","status": 200,"data":serializer.data})
        else:
            return Response({"message": "Success","status": "200","data":[]})
    except Exception as e:
        return Response({"message": str(e),"status": "201","data":[]})

#Static DropDown All API
@api_view(["GET"])
def static_all(request):
    try:
        if request.query_params:
            dds = StaticDropDown.objects.filter(**request.query_params.dict()).order_by('id')
        else:
            dds = StaticDropDown.objects.all().order_by('-id')
        
        if dds:
            serializer = StaticDropDownSerializer(dds, many=True)
            return Response({"message": "Success","status": 200,"data":serializer.data})
        else:
            return Response({"message": "Success","status": "200","data":[]})
    except Exception as e:
        return Response({"message": str(e),"status": "201","data":[]})

#DropDown Update API
@api_view(['POST'])
def update(request):
    try:
        fetchid = request.data['id']
        dd = DropDown.objects.get(pk=fetchid)
        data = DropDownSerializer(instance=dd, data=request.data)     
        if data.is_valid():
            data.save()
            return Response({"message":"successful","status":"200","data":[]})
        else:
            return Response({"message":"ID Wrong","status":"201","data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":"201","data":[]})

#DropDown delete
@api_view(['POST'])
def delete(request):
    fetchid=request.data['id']
    try:
        fetchdata=DropDown.objects.filter(pk=fetchid).delete()        
        return Response({"message":"successful","status":"200","data":[]})        
    except Exception as e:
         return Response({"message":str(e),"status":"201","data":[]})

