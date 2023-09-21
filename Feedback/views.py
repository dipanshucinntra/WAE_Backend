from django.shortcuts import render, redirect  
from django.http import JsonResponse, HttpResponse
from .models import *
from Attachment.models import *

import json

from django.contrib import messages

from rest_framework.decorators import api_view    
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import *
from Attachment.serializers import *
from rest_framework.parsers import JSONParser


#Feedback One API
@api_view(["POST"])
def one(request):
    try:
        id=request.data['id']
        obj = Feedback.objects.filter(id=id)
        ser = FeedbackSerializer(obj, many=True)
        print(ser.data)
        res = showFeedback(ser.data)                
        return Response({"message": "Success", "status": 200, "data":res})
    except Exception as e:
         return Response({"message":str(e), "status":"201","data":[]})

#Feedback All API
@api_view(["GET"])
def all(request):    
    try:    
        objs = Feedback.objects.all() 
        ser = FeedbackSerializer(objs, many=True)
        res = showFeedback(ser.data)  
        return Response({"message": "Success", "status": 200, "data":res})
    except Exception as e:
         return Response({"message":str(e), "status":"201","data":[]})

#Feedback All filter by CardCode API
@api_view(["POST"])
def all_filter(request):    
    try:    
        CardCode = request.data['CardCode']
        objs = Feedback.objects.filter(CardCode=CardCode) 
        ser = FeedbackSerializer(objs, many=True)
        res = showFeedback(ser.data)  
        return Response({"message": "Success", "status": 200, "data":res})
    except Exception as e:
         return Response({"message":str(e), "status":"201","data":[]})

def showFeedback(objs):
    allObj = [];
    for obj in objs:
        if Attachment.objects.filter(LinkID = obj['id'], LinkType="Feedback").exists():
            attObj = Attachment.objects.filter(LinkID = obj['id'], LinkType="Feedback")
            ser = AttachmentSerializer(attObj, many=True)
            obj['Attach'] = ser.data
        else:
            obj['Attach'] = []
        
        allObj.append(obj)        
    return allObj

#Feedback delete
@api_view(["POST"])
def delete(request):
    try:
        fetchid=request.data['id']
        fetchdata=Feedback.objects.filter(pk=fetchid).delete()
        return Response({"message": "Success", "status": 200, "data":[]})
    except Exception as e:
         return Response({"message":str(e), "status":"201","data":[]})

#Feedback Create API
@api_view(['POST'])
def create(request):
    try:
        Remark = request.data["Remark"]
        Type = request.data["Type"]
        Rating = request.data["Rating"]
        SourceType = request.data["SourceType"]
        SourceID = request.data["SourceID"]
        CardCode = request.data["CardCode"]
        CreatedDate = request.data["CreatedDate"]
        CreatedTime = request.data["CreatedTime"]

        model=Feedback(Remark = Remark,Type = Type,Rating=Rating, SourceType = SourceType,SourceID = SourceID,CardCode = CardCode,CreatedDate = CreatedDate,CreatedTime = CreatedTime)
        model.full_clean()
        model.save()
        obj = Feedback.objects.latest('id')
        
        print(request.FILES.getlist('Attach'))
        for File in request.FILES.getlist('Attach'):
            attachmentsImage_url = ""
            target ='./bridge/static/image/Attachment'
            os.makedirs(target, exist_ok=True)
            fss = FileSystemStorage()
            file = fss.save(target+"/"+File.name, File)
            productImage_url = fss.url(file)
            attachmentsImage_url = productImage_url.replace('/bridge', '')
            print(attachmentsImage_url)

            att=Attachment(File=attachmentsImage_url, Caption=File.name, LinkType="Feedback", LinkID=obj.id, CreateDate=CreatedDate, CreateTime=CreatedTime, UpdateDate=CreatedDate, UpdateTime=CreatedTime)
            
            att.save()

        return Response({"message": "Success", "status": 200, "data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":201,"data":[]})
		
#Feedback Update API
@api_view(['POST'])
def update(request):
    try:
        fetchid = request.data['id']
        model = Feedback.objects.get(pk = fetchid)
        model.Remark = request.data["Remark"]
        model.Type = request.data["Type"]
        model.Rating = request.data["Rating"]
        model.SourceType = request.data["SourceType"]
        model.SourceID = request.data["SourceID"]
        model.CardCode = request.data["CardCode"]
        model.CreatedDate = request.data["CreatedDate"]
        model.CreatedTime = request.data["CreatedTime"]
        model.full_clean()
        model.save()
        return Response({"message": "Success", "status": 200, "data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":201,"data":[]})
		