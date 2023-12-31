from django.conf import settings
from django.shortcuts import render, redirect  
from django.http import JsonResponse, HttpResponse
from .forms import BPDepartment
from .models import BPDepartment
import requests, json

from django.contrib import messages

from rest_framework.decorators import api_view    
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import BPDepartmentSerializer
from rest_framework.parsers import JSONParser
# Create your views here.  

#BPDepartment Create API
@api_view(['POST'])
def create(request):
    
    Name = request.data['Name']
    Description = request.data['Description']

    model = BPDepartment(Name=Name, Description=Description)

    model.save()    
    dep = BPDepartment.objects.latest('id')
    fetchid = dep.id


    if settings.SAP == True:
        r = requests.post(settings.BASEURL+'/Login', data=json.dumps(settings.SAPDB), verify=False)
        token = json.loads(r.text)['SessionId']
        print(token)

        dep_data = {
                    "Name": request.data['Name'],
                    "Description": request.data['Description']
                    }

        res = requests.post(settings.BASEURL+'/Departments', data=json.dumps(dep_data), cookies=r.cookies, verify=False)

        live = json.loads(res.text)

        

        if "Code" in live:
            print(live['Code'])
            
            model = BPDepartment.objects.get(pk = fetchid)
            model.Code = live['Code']
            model.save()
            
            return Response({"message":"successful","status":200,"data":[{"id":dep.id, "Code":live['Code']}]})
        else:
            SAP_MSG = live['error']['message']['value']
            print(SAP_MSG)
            if "already exists" in SAP_MSG:
                fetchdata=BPDepartment.objects.filter(pk=fetchid).delete()
                return Response({"message":"Not created","SAP_error":SAP_MSG, "status":202,"data":[]})
            else:
                return Response({"message":"Partely successful","SAP_error":SAP_MSG, "status":202,"data":[]})
    else:
        model = BPDepartment.objects.get(pk = fetchid)
        model.Code = fetchid
        model.save()
        return Response({"message":"successful","status":200,"data":[{"id":dep.id, "Code":fetchid}]})

#BPDepartment All API
@api_view(["GET"])
def all(request):    
    bpdepartment_obj = BPDepartment.objects.all() 
    bpdepartment_json = BPDepartmentSerializer(bpdepartment_obj, many=True)
    return Response({"message": "Success","status": 200,"data":bpdepartment_json.data})


#BPDepartment One API
@api_view(["POST"])
def one(request):
    id=request.data['id']
    bpdepartment_obj = BPDepartment.objects.get(id=id)
    bpdepartment_json = BPDepartmentSerializer(bpdepartment_obj)
    return Response({"message": "Success","status": 200,"data":[bpdepartment_json.data]})

#BPDepartment Update API
@api_view(['POST'])
def update(request):
    fetchid = request.data['id']
    try:
        model = BPDepartment.objects.get(pk = fetchid)
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
            
            dep_data = {
                'Name':request.data['Name'],
                'Description':request.data['Description']
            }
            
            print(dep_data)
            

            print(settings.BASEURL+'/Departments('+model.Code+')');
        
            res = requests.patch(settings.BASEURL+'/Departments('+model.Code+')', data=json.dumps(dep_data), cookies=r.cookies, verify=False)
            
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


#BPDepartment delete
@api_view(['POST'])
def delete(request):
    fetchid=request.data['id']
    try:
        dep=BPDepartment.objects.get(pk=fetchid)
        Code = dep.Code
        
        fetchdata=BPDepartment.objects.filter(pk=fetchid).delete()
        if settings.SAP == True:            
            try:
                r = requests.post(settings.BASEURL+'/Login', data=json.dumps(settings.SAPDB), verify=False)
                token = json.loads(r.text)['SessionId']
                print(token)
                print(settings.BASEURL+'/Departments('+Code+')')
                res = requests.delete(settings.BASEURL+'/Departments('+Code+')', cookies=r.cookies, verify=False)
                print(res.content)
                return Response({"message":"successful","status":"200","data":[]})
            except:
                return Response({"message":"successful","status":"200","data":[]})
        else:
            return Response({"message":"successful","status":"200","data":[]})
    except:
         return Response({"message":"Id wrong","status":"201","data":[]})


#Department Sync API
@api_view(['GET'])
def sync(request):
    try:   
        try:
            last = BPDepartment.objects.last().Code
        except:
            last = -10
        
        maxitem = 0
        url = f"/Departments?$filter=Code gt {last}"
        print(url)
        
        while url != "":
            res = settings.CALLAPI('get', url, 'api', '', maxitem)            
            text = res.text.replace(': null', ':""')
            objs = json.loads(text)
            #print(objs)
            
            for obj in objs['value']:                        
                
                if not BPDepartment.objects.filter(Code=obj['Code']).exists():
                    ser = BPDepartmentSerializer(data=obj)
                    ser.is_valid(raise_exception=True)
                    ser.save()
                    print(obj)
                else:
                    print("Exist: ", obj['Code'])
            
            if "odata.nextLink" in objs:
                url = "/"+objs['odata.nextLink']
            else:
                url = ""
                
        return Response({"message":"Success", "status":200,"data":[]})
    except Exception as e:
        print(str(e))
        return Response({"message":"Error", "status":201, "data":[{"Error":str(e)}]})