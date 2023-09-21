from django.shortcuts import render, redirect  
from django.http import JsonResponse, HttpResponse
from .models import BPCurrency
import requests, json

from django.contrib import messages

from rest_framework.decorators import api_view    
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import BPCurrencySerializer
from rest_framework.parsers import JSONParser
# Create your views here.  

#BPPosition Create API
@api_view(['POST'])
def create(request):
    
    CurrCode = request.data['CurrCode']
    CurrName = request.data['CurrCode']
    DocCurrCod = request.data['DocCurrCod']
    model = BPCurrency(CurrCode=CurrCode, CurrName=CurrName, DocCurrCod=DocCurrCod)
    model.save()    
    cur = BPCurrency.objects.latest('id')
    return Response({"message":"successful","status":200,"data":[{"id":cur.id}]})

#BPCurrency All API
@api_view(["GET"])
def all(request):
    bpcurrency_obj = BPCurrency.objects.all() 
    bpcurrency_json = BPCurrencySerializer(bpcurrency_obj, many=True)
    return Response({"message": "Success","status": 200,"data":bpcurrency_json.data})

#BPEmployee One API
@api_view(["POST"])
def one(request):
    id=request.data['id']
    cur_obj = BPCurrency.objects.get(id=id)
    cur_json = BPCurrencySerializer(cur_obj)
    return Response({"message": "Success","status": 200,"data":[cur_json.data]})


    CurrCode = request.data['CurrCode']
    CurrName = request.data['CurrCode']
    DocCurrCod = request.data['DocCurrCod']


#BPPosition Update API
@api_view(['POST'])
def update(request):    
    try:
        fetchid = request.data['id']
        model = BPCurrency.objects.get(pk = fetchid)
        model.CurrName = request.data['CurrName']
        model.CurrCode = request.data['CurrCode']
        model.DocCurrCod = request.data['DocCurrCod']
        model.save()
        return Response({"message":"successful","status":"200", "data":[]})
        
        pos_data = {
            'Name':request.data['Name'],
            'Description':request.data['Description']
        }
        
        print(pos_data)
        
        res = settings.CALLAPI('patch', '/EmployeePosition('+model.PositionID+')', 'api', pos_data)
        
        if len(res.content) !=0 :
            res1 = json.loads(res.content)
            SAP_MSG = res1['error']['message']['value']
            return Response({"message":"Partely successful","status":"202","SAP_error":SAP_MSG, "data":[context]})
        else:
            return Response({"message":"successful","status":"200", "data":[context]})
    except Exception as e:
        return Response({"message":str(e),"status":"201","data":[]})


#BPPosition delete
@api_view(['POST'])
def delete(request):    
    try:
        fetchid=request.data['id']
        pos=BPCurrency.objects.get(pk=fetchid)
        #PositionID = pos.PositionID
        
        fetchdata=BPCurrency.objects.filter(pk=fetchid).delete()
        return Response({"message":"successful","status":"200","data":[]})      
    except:
         return Response({"message":"Id wrong","status":"201","data":[]})
