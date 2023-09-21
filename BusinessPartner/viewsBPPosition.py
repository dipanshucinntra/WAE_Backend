from django.conf import settings
from django.shortcuts import render, redirect  
from django.http import JsonResponse, HttpResponse
from .forms import BPPosition
from .models import BPPosition
import requests, json

from django.contrib import messages

from rest_framework.decorators import api_view    
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import BPPositionSerializer
from rest_framework.parsers import JSONParser
# Create your views here.  

#BPPosition Create API
@api_view(['POST'])
def create(request):
    
    Name = request.data['Name']
    Description = request.data['Description']

    model = BPPosition(Name=Name, Description=Description)

    model.save()    
    pos = BPPosition.objects.latest('id')
    fetchid = pos.id

    if settings.SAP == True:
        r = requests.post(settings.BASEURL+'/Login', data=json.dumps(settings.SAPDB), verify=False)
        token = json.loads(r.text)['SessionId']
        print(token)

        pos_data = {
                    "Name": request.data['Name'],
                    "Description": request.data['Description']
                    }

        res = requests.post(settings.BASEURL+'/EmployeePosition', data=json.dumps(pos_data), cookies=r.cookies, verify=False)

        live = json.loads(res.text)

        if "PositionID" in live:
            print(live['PositionID'])
            
            model = BPPosition.objects.get(pk = fetchid)
            model.PositionID = live['PositionID']
            model.save()
            
            return Response({"message":"successful","status":200,"data":[{"id":pos.id, "PositionID":live['PositionID']}]})
        else:
            SAP_MSG = live['error']['message']['value']
            print(SAP_MSG)
            if "already exists" in SAP_MSG:
                fetchdata=BPPosition.objects.filter(pk=fetchid).delete()
                return Response({"message":"Not created","SAP_error":SAP_MSG, "status":202,"data":[]})
            else:
                return Response({"message":"Partely successful","SAP_error":SAP_MSG, "status":202,"data":[]})
    else:
        model = BPPosition.objects.get(pk = fetchid)
        model.PositionID = fetchid
        model.save()
        return Response({"message":"successful","status":200,"data":[{"id":pos.id, "PositionID":fetchid}]})
    

#BPPosition All API
@api_view(["GET"])
def all(request):    
    bpposition_obj = BPPosition.objects.all() 
    bpposition_json = BPPositionSerializer(bpposition_obj, many=True)
    return Response({"message": "Success","status": 200,"data":bpposition_json.data})


#BPEmployee One API
@api_view(["POST"])
def one(request):
    id=request.data['id']
    bpposition_obj = BPPosition.objects.get(id=id)
    bpposition_json = BPPositionSerializer(bpposition_obj)
    return Response({"message": "Success","status": 200,"data":[bpposition_json.data]})

#BPPosition Update API
@api_view(['POST'])
def update(request):
    fetchid = request.data['id']
    try:
        model = BPPosition.objects.get(pk = fetchid)
        model.Name = request.data['Name']
        model.Description = request.data['Description']
        model.save()
        if settings.SAP == True:

            context = {
                'id':request.data['id'],
                'Name':request.data['Name'],
                'Description':request.data['Description']
                }
            
            r = requests.post(settings.BASEURL+'/Login', data=json.dumps(settings.SAPDB), verify=False)
            token = json.loads(r.text)['SessionId']
            print(token)
            
            pos_data = {
                'Name':request.data['Name'],
                'Description':request.data['Description']
            }
            
            print(pos_data)

            print(settings.BASEURL+'/EmployeePosition('+model.PositionID+')');
        
            res = requests.patch(settings.BASEURL+'/EmployeePosition('+model.PositionID+')', data=json.dumps(pos_data), cookies=r.cookies, verify=False)
            
            if len(res.content) !=0 :
                res1 = json.loads(res.content)
                SAP_MSG = res1['error']['message']['value']
                return Response({"message":"Partely successful","status":"202","SAP_error":SAP_MSG, "data":[context]})
            else:
                return Response({"message":"successful","status":"200", "data":[context]})
        else:
            return Response({"message":"successful","status":"200", "data":[]})
            
    except:
        return Response({"message":"ID Wrong","status":"201","data":[context]})


#BPPosition delete
@api_view(['POST'])
def delete(request):
    fetchid=request.data['id']
    try:
        pos=BPPosition.objects.get(pk=fetchid)
        PositionID = pos.PositionID
        
        fetchdata=BPPosition.objects.filter(pk=fetchid).delete()
        if settings.SAP == True:
    
            try:
                r = requests.post(settings.BASEURL+'/Login', data=json.dumps(settings.SAPDB), verify=False)
                token = json.loads(r.text)['SessionId']
                print(token)
                print(settings.BASEURL+'/EmployeePosition('+PositionID+')')
                res = requests.delete(settings.BASEURL+'/EmployeePosition('+PositionID+')', cookies=r.cookies, verify=False)
                print(res.content)
                return Response({"message":"successful","status":"200","data":[]})
            except:
                return Response({"message":"successful","status":"200","data":[]})        
        else:
            return Response({"message":"successful","status":"200","data":[]})
    except:
         return Response({"message":"Id wrong","status":"201","data":[]})

#Position Sync API
@api_view(['GET'])
def sync(request):
    try:   
        try:
            last = BPPosition.objects.last().PositionID
        except:
            last = -10
        
        maxitem = 0
        url = f"/EmployeePosition?$filter=PositionID gt {last}"
        print(url)
        
        while url != "":
            res = settings.CALLAPI('get', url, 'api', '', maxitem)            
            text = res.text.replace(': null', ':""')
            objs = json.loads(text)
            #print(objs)
            
            for obj in objs['value']:                        
                
                if not BPPosition.objects.filter(PositionID=obj['PositionID']).exists():
                    ser = BPPositionSerializer(data=obj)
                    ser.is_valid(raise_exception=True)
                    ser.save()
                    print(obj)
                else:
                    print("Exist: ", obj['PositionID'])
            
            if "odata.nextLink" in objs:
                url = "/"+objs['odata.nextLink']
            else:
                url = ""
                
        return Response({"message":"Success", "status":200,"data":[]})
    except Exception as e:
        print(str(e))
        return Response({"message":"Error", "status":201, "data":[{"Error":str(e)}]})