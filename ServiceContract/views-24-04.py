from django.shortcuts import render, redirect  
from django.http import JsonResponse, HttpResponse
import requests, json

from django.contrib import messages

from rest_framework.decorators import api_view    
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from Attachment.models import Attachment
from Attachment.serializers import AttachmentSerializer
import os
from django.core.files.storage import FileSystemStorage
from ServiceContract.models import ServiceContract
from ServiceContract.serializers import ServiceContractSerializer
from Employee.models import *
from BusinessPartner.models import BPEmployee
from BusinessPartner.serializers import BPEmployeeSerializer

from Tickets.models import *
from Tickets import views as Tick

from Invoice.models import Invoice
from Invoice.serializers import InvoiceSerializer
# Create your views here.  

#ServiceContract Create API
@api_view(['POST'])
def create(request):
    try:    
        res = ServiceContract_add(request)    
        if type(res) == int:
            return Response({"message":"successful","status":200,"data":[{"id":res}]})        
        else:
            return Response({"message":"Error","status":201,"data":[{"Error":str(res)}]})
    except Exception as e:
        return Response({"message":"Error","status":201,"data":[{"Error":str(e)}]})


def ServiceContract_add(request):
        try:
            request.data['ServiceContractsItem'] = json.dumps(request.data['ServiceContractsItem'])            
            model = ServiceContract(**request.data)
            model.full_clean()
            model.save()
            req = ServiceContract.objects.latest('id')
            tkt = Tick.sc_ticket(request, {"Type":"Maintenance", "SubType":"Other"})
            if type(tkt) == int:			
               return req.id
            else:
                ServiceContract.objects.filter(pk=req.id).delete()
                return str(tkt)			
        except Exception as e:
            return str(e)

def ss():
    try:
        OrderID = request.data['OrderID']
        ProjectID = request.data['ProjectID']
        MNo = request.data['MNo']
        ProductSerialNo = request.data['ProductSerialNo']
        ProductCate = request.data['ProductCate']
        ServiceContractID = request.data['ServiceContractID']
        ServiceContractType = request.data['ServiceContractType']
        ContractPersoneName = request.data['ContractPersoneName']
        ContractPersoneNumber = request.data['ContractPersoneNumber']
        Frequency = request.data['Frequency']
        FromDate = request.data['FromDate']
        ToDate = request.data['ToDate']
        CheckList = request.data['CheckList']
        CardCode = request.data['CardCode']
        BPName = request.data['BPName']
        Remarks = request.data['Remarks']
        ServiceContractOwner = request.data['ServiceContractOwner']
        SiteEngineerAssigned = request.data['SiteEngineerAssigned']
        ContractType = request.data['ContractType']
        Status = request.data['Status']
        ServiceContractsItem = json.dumps(request.data['ServiceContractsItem'])
        
        #Attach = request.data['Attach']  
        
        model = ServiceContract(OrderID=OrderID, ProjectID=ProjectID, MNo=MNo, ProductSerialNo=ProductSerialNo, ProductCate=ProductCate, ServiceContractID=ServiceContractID, ServiceContractType=ServiceContractType, ContractPersoneName=ContractPersoneName, ContractPersoneNumber=ContractPersoneNumber, Frequency=Frequency, FromDate=FromDate, ToDate=ToDate, CheckList=CheckList, CardCode=CardCode, BPName=BPName, Remarks=Remarks, ServiceContractOwner=ServiceContractOwner, SiteEngineerAssigned=SiteEngineerAssigned, ContractType=ContractType, Status=Status, ServiceContractsItem=ServiceContractsItem)
        
        model.save()
        
        ServiceContractID = ServiceContract.objects.latest('id')
        
        """
        for File in request.FILES.getlist('Attach'):
            attachmentsImage_url = ""
            target ='./bridge/static/image/ServiceContract'
            os.makedirs(target, exist_ok=True)
            fss = FileSystemStorage()
            file = fss.save(target+"/"+File.name, File)
            productImage_url = fss.url(file)
            attachmentsImage_url = productImage_url.replace('/bridge', '')
            
            print(attachmentsImage_url)

            att=Attachment(File=attachmentsImage_url, LinkType="ServiceContract", LinkID=ServiceContractID.id, CreateDate=model.updateDate, CreateTime=model.updateTime)
        
            att.save()
        """
        return ServiceContractID.id
    except Exception as e:
        return str(e)
        
#ServiceContract All API
@api_view(["GET"])
def all(request):
    try:
        servicecontract_obj = ServiceContract.objects.all().order_by("-id")
        result = ServiceContractSerializer(servicecontract_obj, many=True)
        #result = showServiceContract(servicecontract_obj)
        return Response({"message": "Success","status": 200,"data":result.data})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})

#ServiceContract One API
@api_view(["POST"])
def one(request):
    try:
        id = request.data['id']
        if ServiceContract.objects.filter(pk=id).exists():
            Objs = ServiceContract.objects.filter(pk=id)
            #result = showServiceContract(Objs)
            result = ServiceContractSerializer(Objs, many=True)
            return Response({"message": "Success","status": 200,"data":result.data})
        else:
            return Response({"message": "Id Doesn't Exist", "status": 201, "data": []})
    except Exception as e:
        return Response({"message": str(e), "status": 201, "data": []})

#ServiceContract Data for all servicecontracts and one servicecontract
def showServiceContract(objs):
    allServiceContract = [];
    for obj in objs:
        ojson = ServiceContractSerializer(obj)
        finalData = json.loads(json.dumps(ojson.data))
            
        if Employee.objects.filter(SalesEmployeeCode = obj.ServiceContractOwner).exists():
            ow_name = Employee.objects.get(SalesEmployeeCode = obj.ServiceContractOwner).SalesEmployeeName
            finalData['ServiceContractOwnerName'] = ow_name  
        else:
            finalData['ServiceContractOwnerName'] = ""

        if Employee.objects.filter(SalesEmployeeCode = obj.SiteEngineerAssigned).exists():
            as_name = Employee.objects.get(SalesEmployeeCode = obj.SiteEngineerAssigned).SalesEmployeeName
            finalData['SiteEngineerAssignedName'] = as_name  
        else:
            finalData['SiteEngineerAssignedName'] = ""
            
        #chk_ids = ",".join(map(str, obj.CheckList))
            
        """
        if Attachment.objects.filter(LinkID = obj.id, LinkType="ServiceContract").exists():
            Attach_dls = Attachment.objects.filter(LinkID = obj.id, LinkType="ServiceContract")
            Attach_json = AttachmentSerializer(Attach_dls, many=True)
            finalData['Attach'] = Attach_json.data
        else:
            finalData['Attach'] = []
        """
        allServiceContract.append(finalData)
    return allServiceContract

@api_view(['PUT'])
def update(request):
    id=request.data['id']
    fetchid=ServiceContract.objects.get(pk=id)
    request.data['ServiceContractsItem'] = json.dumps(request.data['ServiceContractsItem'])
    
    if request.method=='PUT':
        req=ServiceContractSerializer(fetchid,data=request.data)
        if req.is_valid():
            req.save()
            return Response({"message":"success", "status":"200", "data":[]})
        return Response(req.errors,status=status.HTTP_400_BAD_REQUEST)

#ServiceContract Update API
@api_view(['POST'])
def update_old(request):
    try:
        fetchid = request.data['id']
        model = ServiceContract.objects.get(pk = fetchid)
        model.InvoiceNo = request.data['InvoiceNo']
        model.TransactId = request.data['TransactId']
        model.TotalAmt = request.data['TotalAmt']
        model.TransactMod = request.data['TransactMod'] 
        model.DueAmount = request.data['DueAmount']
        model.ServiceContractDate = request.data['ServiceContractDate']
        model.ReceivedAmount = request.data['ReceivedAmount'] 
        model.Remarks = request.data['Remarks']
        model.updateDate = request.data['updateDate']
        model.updateTime = request.data['updateTime']
        model.updatedBy = request.data['updatedBy']
        model.CardCode = request.data['CardCode']
        
        Attach = request.data['Attach']  
        for File in request.FILES.getlist('Attach'):
            attachmentsImage_url = ""
            target ='./bridge/static/image/ServiceContract'
            os.makedirs(target, exist_ok=True)
            fss = FileSystemStorage()
            file = fss.save(target+"/"+File.name, File)
            productImage_url = fss.url(file)
            attachmentsImage_url = productImage_url.replace('/bridge', '')
            
            print(attachmentsImage_url)

            att=Attachment(File=attachmentsImage_url, LinkType="ServiceContract", LinkID=fetchid, CreateDate=model.updateDate, CreateTime=model.updateTime)
        
            att.save()

        model.save()

        return Response({"message":"successful","status":200,"data":[]})
    except:
        return Response({"message":"ID Wrong","status":201,"data":[]})
    
#ServiceContract delete for multiple "id":[4,5]
@api_view(['POST'])
def delete(request):
    try:
        fetchids= request.data['id']
        for ids in fetchids:
            if ServiceContract.objects.filter(pk=ids).exists():
                ServiceContract.objects.filter(pk=ids).delete()
            else:
                return Response({"message":"Id Doesn't Exist","status":"405","data":[]}) 
        return Response({"message":"successful","status":"200","data":[]})   
    except Exception as e:
        return Response({"message":"Id wrong","status":"201","data":[{"Error":str(e)}]})

#ServiceContract Image Delete API
@api_view(['POST'])
def servicecontract_img_delete(request):
    pay_id= request.data['id']
    
    image_id = request.data['image_id']
    
    try:
        if Attachment.objects.filter(pk=image_id , LinkID=pay_id).exists():
            Attachment.objects.filter(pk=image_id, LinkID=pay_id).delete()
            
            return Response({"message":"successful","status":"200","data":[]})        
        else:
            return Response({"message":"Id Not Found","status":"201","data":[]})        
    except:
        return Response({"message":"Id wrong","status":"201","data":[]})

