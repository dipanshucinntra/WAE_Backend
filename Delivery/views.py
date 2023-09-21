from enum import Flag
from django.shortcuts import render, redirect  
from django.http import JsonResponse, HttpResponse

from BusinessPartner import *
from Order.models import *
from BusinessPartner.serializers import *
from Category.models import Category
from Employee.serializers import EmployeeSerializer
from .models import *
from Employee.models import Employee

import requests, json
from global_fun import *

from rest_framework.decorators import api_view    
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import JSONParser

from pytz import timezone
from datetime import date, datetime, timedelta

import os
from django.core.files.storage import FileSystemStorage

serverDate = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d')

date = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d')
yearmonth = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m')
time = datetime.now(timezone("Asia/Kolkata")).strftime('%H:%M %p')

print("===datetime===")
print(date, yearmonth, time)

# Create your views here.
@api_view(["POST"])
def delivery(request):
    json_data = request.data    
    if "SalesEmployeeCode" in json_data:
        print("yes")
        
        if json_data['SalesEmployeeCode']!="":
            SalesEmployeeCode = json_data['SalesEmployeeCode']
            SalesEmployeeCode = getAllReportingToIdsSubdep(SalesEmployeeCode, "Sales")
            print(SalesEmployeeCode)

            if json_data['Type'] =="over":
                ord = Delivery.objects.filter(SalesPersonCode__in=SalesEmployeeCode, DocumentStatus="bost_Open", DocDueDate__lt=date)
                allord = showDelivery(ord)
                #print(allord)
            elif json_data['Type'] =="open":
                ord = Delivery.objects.filter(SalesPersonCode__in=SalesEmployeeCode, DocumentStatus="bost_Open", DocDueDate__gte=date)
                allord = showDelivery(ord)
                #print(allord)
            else:
                ord = Delivery.objects.filter(SalesPersonCode__in=SalesEmployeeCode, DocumentStatus="bost_Close")
                allord = showDelivery(ord)
                #print(allord)
			
            #{"SalesEmployeeCode":"2"}
            return Response({"message": "Success","status": 200,"data":allord})
            
            #return Response({"message": "Success","status": 201,"data":[{"emp":SalesEmployeeCode}]})
        else:
            return Response({"message": "Unsuccess","status": 201,"data":[{"error":"SalesEmployeeCode?"}]})
    else:
        return Response({"message": "Unsuccess","status": 201,"data":[{"error":"SalesEmployeeCode?"}]})
	
	
#Quotation All API
@api_view(["POST"])
def all_filter(request):
    json_data = request.data    
    if "SalesPersonCode" in json_data:        
        if json_data['SalesPersonCode']!="":
            SalesPersonID = json_data['SalesPersonCode']
            
            emp_obj = Employee.objects.get(SalesEmployeeCode=SalesPersonID)
            
            if emp_obj.role == 'manager':
                emps = Employee.objects.filter(reportingTo=SalesPersonID)#.values('id', 'SalesEmployeeCode')
                SalesPersonID=[SalesPersonID]
                for emp in emps:
                    SalesPersonID.append(emp.SalesEmployeeCode)
                
            elif emp_obj.role == 'admin':
                emps = Employee.objects.filter(SalesEmployeeCode__gt=0)
                SalesPersonID=[]
                for emp in emps:
                    SalesPersonID.append(emp.SalesEmployeeCode)
            else:
                SalesPersonID = [json_data['SalesPersonCode']]
            
            print(SalesPersonID)
            
            for ke in json_data.keys():
                if ke =='U_FAV' :
                    print("yes filter")
                    if json_data['U_FAV'] !='':
                        quot_obj = Quotation.objects.filter(SalesPersonCode__in=SalesPersonID, U_FAV=json_data['U_FAV']).order_by("-id")
                        if len(quot_obj) ==0:
                            return Response({"message": "Not Available","status": 201,"data":[]})
                        else:
                            allqt = QuotationShow(quot_obj)
                            return Response({"message": "Success","status": 200,"data":allqt})                
                else:
                    print("no filter")
                    quot_obj = Delivery.objects.filter(SalesPersonCode__in=SalesPersonID).order_by("-id")
                    allqt = showDelivery(quot_obj)
                        
                    return Response({"message": "Success","status": 200,"data":allqt})
            
        else:
            return Response({"message": "Unsuccess","status": 201,"data":[{"error":"SalesPersonCode?"}]})
    else:
        print("no")
        return Response({"message": "Unsuccess","status": 201,"data":[{"error":"SalesPersonCode?"}]})


#Delivery All API
@api_view(["POST"])
def all(request):
    try:
        PageNo = request.data['PageNo']
        MaxItem = 30
        endWith = (PageNo * MaxItem)
        startWith = (endWith - MaxItem)
        # [startWith:endWith]

        Deliverys_obj = Delivery.objects.all().order_by("-id")[startWith:endWith]
        allqt = showDelivery(Deliverys_obj)
        return Response({"message": "Success","status": 200,"data":allqt})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})

#Delivery One API
@api_view(["POST"])
def one(request):
    id=request.data['id']
    
    Deliverys_obj = Delivery.objects.filter(id=id)
    
    allqt = showDelivery(Deliverys_obj)
    return Response({"message": "Success","status": 200,"data":allqt})


#Delivery delete
@api_view(['POST'])
def delete(request):
    fetchid=request.data['id']
    try:
        emp=Delivery.objects.get(pk=fetchid)
        SalesDeliveryCode = emp.SalesDeliveryCode
        
        fetchdata=Delivery.objects.filter(pk=fetchid).delete()
        
        with open("../bridge/bridge/db.json") as f:
            db = f.read()
        print(db)
        data = json.loads(db)
        print(data)
        
        return Response({"message":"successful","status":"200","data":[]})        
    except:
         return Response({"message":"Id wrong","status":"201","data":[]})


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Delivery One API
@api_view(["GET"])
def bp_list(request):
    try:
        allbp = []
        bpList = Delivery.objects.values_list('CardCode', flat=True).distinct()
        print(bpList)
        bpObj = BusinessPartner.objects.filter(CardCode__in = bpList)
        # bpJson = BusinessPartnerSerializer(bpObj, many=True)
        for bp in bpObj:
            
            # Business Partner details obj
            bp_json = BusinessPartnerSerializer(bp)
            bpFinalObj = json.loads(json.dumps(bp_json.data))

            # Business Partner Employee obj
            cont = BPEmployee.objects.filter(CardCode=bp.CardCode)
            cont_json = BPEmployeeSerializer(cont, many=True)
            bpFinalObj['ContactEmployees'] = json.loads(json.dumps(cont_json.data))

            # Business Partner contact person obj
            if len(cont) > 0:
                ContactPerson = cont[0].FirstName
                print(ContactPerson)
            else:
                ContactPerson = ""
                print(ContactPerson)
            
            bpFinalObj['ContactPerson'] = ContactPerson
            
            # BusinessPartner address obj
            bpaddr = BPAddresses.objects.filter(BPCode=bp.CardCode)
            bpaddr_json = BPAddressesSerializer(bpaddr, many=True)
            jss0 = json.loads(json.dumps(bpaddr_json.data))

            bpFinalObj['BPAddresses'] = jss0
                
            allbp.append(bpFinalObj)
                
        return Response({"message": "Success","status": 200,"data":allbp})
    except Exception as e:
        return Response({"message": "Error","status": 201,"data":[str(e)]})
      
      


#Delivery One API
@api_view(["GET"])
def bp_contact_person_list(request):
    try:
        allbp = []
        bpList = Delivery.objects.values_list('CardCode', flat=True).distinct()
        print(bpList)
        bpEmpObj = BPEmployee.objects.filter(CardCode__in = bpList)
        # bpEmpJson = BPEmployeeSerializer(bpEmpObj, many=True)
        for obj in bpEmpObj:
            CardCode = obj.CardCode
            bpEmpJson = BPEmployeeSerializer(obj)
            bpEmpData = json.loads(json.dumps(bpEmpJson.data))
            if BusinessPartner.objects.filter(CardCode = CardCode).exists():
                bpEmpData['CardName'] = BusinessPartner.objects.filter(CardCode = CardCode).values_list('CardName', flat=True)[0]
            else:
                bpEmpData['CardName'] = ""

            allbp.append(bpEmpData)
        return Response({"message": "Success","status": 200,"data":allbp})
    except Exception as e:
        return Response({"message": "Error","status": 201,"data":[str(e)]})

#Delivery One API
@api_view(["POST"])
def bp_wise_delivery(request):
    try:
        CardCode = request.data['CardCode']
        if BusinessPartner.objects.filter(CardCode = CardCode).exists():
            invoice_obj = Delivery.objects.filter(CardCode = CardCode)
            result = showDelivery(invoice_obj)
            return Response({"message": "Success","status": 200,"data":result})
        else:
            return Response({"message": "Error","status": 201,"data":['BP not exists']})
    except Exception as e:
        return Response({"message": "Error","status": 201,"data":[str(e)]})


#Delivery One API
@api_view(["POST"])
def bp_wise_delivery_items(request):
    try:
        CardCode = request.data['CardCode']
        if BusinessPartner.objects.filter(CardCode = CardCode).exists():
            deliveryIds = Delivery.objects.filter(CardCode = CardCode).values_list('id')
            itemObj = DocumentLines.objects.filter(DeliveryId__in = deliveryIds)
            itemJson = DocumentLinesSerializer(itemObj, many=True)

            return Response({"message": "Success","status": 200,"data":itemJson.data})
        else:
            return Response({"message": "Error","status": 201,"data":['BP not exists']})
    except Exception as e:
        return Response({"message": "Error","status": 201,"data":[str(e)]})


#Delivery One API
@api_view(["POST"])
def itemdetails_by_serialno(request):
    try:
        SerialNo = request.data['SerialNo']
        if DocumentLines.objects.filter(SerialNo = SerialNo).exists():
            itme_obj = DocumentLines.objects.filter(SerialNo = SerialNo)
            item_json = DocumentLinesSerializer(itme_obj, many=True)
            itmData = json.loads(json.dumps(item_json.data))
            DeliveryId = itmData[0]['DeliveryId']
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            ItemCategory = itmData[0]['ItemCategory']
            if Category.objects.filter(Number = ItemCategory).exists():
                catObj = Category.objects.get(Number = ItemCategory)
                itmData[0]['ItemCategoryName'] = catObj.GroupName
            else:
                itmData[0]['ItemCategoryName'] = ""

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            if Delivery.objects.filter(pk = DeliveryId).exists():
                deliveryObj = Delivery.objects.get(pk = DeliveryId)
                deliveryJson = DeliverySerializer(deliveryObj)
                itmData[0]['DeliveryId'] = deliveryJson.data

                CardCode = deliveryObj.CardCode
                if BusinessPartner.objects.filter(CardCode = CardCode).exists():
                    print('in if')
                    bpObj = BusinessPartner.objects.get(CardCode = CardCode)
                    bpjson = BusinessPartnerSerializer(bpObj)
                    print(bpjson.data)
                    itmData[0]['BusinessPartner'] = bpjson.data
                else:
                    print('in else')
                    itmData[0]['BusinessPartner'] = {}
            else:
                itmData[0]['BusinessPartner'] = {}
            
            print(itmData)
            return Response({"message": "Success","status": 200,"data":[itmData[0]]})
        else:
            return Response({"message": "Item not exists","status": 201,"data":[]})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})


#Delivery One API
@api_view(["GET"])
def allDeliveryItems(request):
    try:
        itemObj = DocumentLines.objects.all().order_by('-id')
        itemJson = DocumentLinesSerializer(itemObj, many=True)
        return Response({"message": "Success","status": 200,"data":itemJson.data})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@api_view(['POST'])
def delivery_attachments_upload(request):
    try:
        fileIds = []
        DeliveryId = request.data['DeliveryId']
        if Delivery.objects.filter(pk = DeliveryId).exists():
            attechmentsImage_url = "" 
            if len(request.FILES.getlist('File')) != 0:
                # print("in attch")
                for Attachment in request.FILES.getlist('File'):
                    # print('in loop')
                    target ='./bridge/static/image/Delivery-Attachment'
                    os.makedirs(target, exist_ok=True)
                    fss = FileSystemStorage()
                    file = fss.save(target+"/"+Attachment.name, Attachment)
                    productImage_url = fss.url(file)
                    attechmentsImage_url = productImage_url.replace('/bridge', '')
                    print(attechmentsImage_url)

                    DeliveryAttachments( DeliveryId = DeliveryId, File = attechmentsImage_url).save()
                    attchId = DeliveryAttachments.objects.latest('-id')
                    fileIds.append(attchId.id)
        else:
            return Response({"message":"Wrong Quotation Id","status":201 ,"data":[]})
        return Response({"message":"Successfull","status":200 ,"data":[{'AttachmentsIds': fileIds}]})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@api_view(['POST'])
def delivery_attachments_delete(request):
    try:
        AttchementIds = request.data['AttchementIds']
        if len(AttchementIds) != 0:
            for id in AttchementIds:
                print('in loop', id)
                if DeliveryAttachments.objects.filter(pk = id).exists():
                    fileObj = DeliveryAttachments.objects.get(pk = id)
                    fileObj.delete()
        else:
            return Response({"message":"Empty Attchements Ids","status":201 ,"data":[]})

        return Response({"message":"Successfull","status":200 ,"data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})


def showDelivery(objs):
    allDelivery = []
    for obj in objs:
        BpEmpId = obj.ContactPersonCode
        SalesPersonCode = obj.SalesPersonCode
        DeliveryId = obj.id
        deliveryJson = DeliverySerializer(obj)
        finalDeliveryData = json.loads(json.dumps(deliveryJson.data))
        
        if BpEmpId != "":
            cpcTypeObj = BPEmployee.objects.filter(InternalCode = BpEmpId).values("id", "FirstName", "E_Mail", "MobilePhone", "CountryCode")
            cpcTypejson = BPEmployeeSerializer(cpcTypeObj, many = True)
            finalDeliveryData['ContactPersonCode']=json.loads(json.dumps(cpcTypejson.data))
        else:
            finalDeliveryData['ContactPersonCode'] = []
            
        if SalesPersonCode != "":
            empObj = Employee.objects.filter(SalesEmployeeCode = SalesPersonCode).values("id", "SalesEmployeeCode", "SalesEmployeeName")
            empjson = EmployeeSerializer(empObj, many=True)
            finalDeliveryData['SalesPersonCode'] = json.loads(json.dumps(empjson.data))
        else:
            finalDeliveryData['SalesPersonCode'] = []
            
        if DeliveryId != "":
                
            linesobj = DocumentLines.objects.filter(DeliveryId = DeliveryId)
            # lines_json = DocumentLinesSerializer(linesobj, many=True)
            itemsData = []

            if DeliveryAttachments.objects.filter(DeliveryId = DeliveryId).exists():
                deliveryAttch = DeliveryAttachments.objects.filter(DeliveryId = DeliveryId)
                deliveryAttchJson = DeliveryAttachmentsSerializer(deliveryAttch, many=True)
                print(deliveryAttchJson.data)
                finalDeliveryData["DeliveryAttachments"]= deliveryAttchJson.data
            else:
                finalDeliveryData["DeliveryAttachments"]= []

            for itemObj in linesobj:
                ItemCategory = itemObj.ItemCategory
                itemjson = DocumentLinesSerializer(itemObj)
                tempItemObj = json.loads(json.dumps(itemjson.data))

                WarrantyStartDate = itemObj.WarrantyStartDate
                WarrantyDueDate = itemObj.WarrantyDueDate
                ExtWarrantyStartDate = itemObj.ExtWarrantyStartDate
                ExtWarrantyDueDate = itemObj.ExtWarrantyDueDate
                AMCStartDate = itemObj.AMCStartDate
                AMCDueDate = itemObj.AMCDueDate
                CMCStartDate = itemObj.CMCStartDate
                CMCDueDate = itemObj.CMCDueDate
                
                currentDate = (datetime.strptime(str(serverDate), '%Y-%m-%d')).date()

                print("------- Warranty ----------")
                warrantyStatus = "Warranty Expired"
                warrantyEndDate = ""
                if WarrantyStartDate != "":
                    if WarrantyStartDate != "None":
                        WarrantyStartDate = (datetime.strptime(str(WarrantyStartDate), '%Y-%m-%d')).date()
                        WarrantyDueDate = (datetime.strptime(str(WarrantyDueDate), '%Y-%m-%d')).date()
                        if currentDate >= WarrantyStartDate and currentDate <= WarrantyDueDate:
                            warrantyStatus = "Under Manufacturing  Warranty"
                            print(warrantyStatus)
                            warrantyEndDate = WarrantyDueDate
                
                # %Y-%m-%d %H:%M:%S
                if ExtWarrantyStartDate != "":
                    if ExtWarrantyStartDate != "None":
                        ExtWarrantyStartDate = (datetime.strptime(str(ExtWarrantyStartDate), '%Y-%m-%d')).date()
                        ExtWarrantyDueDate = (datetime.strptime(str(ExtWarrantyDueDate), '%Y-%m-%d')).date()
                        if currentDate >= ExtWarrantyStartDate and currentDate <= ExtWarrantyDueDate:
                            warrantyStatus = "Under Extended  Warranty"
                            print(warrantyStatus)
                            warrantyEndDate = ExtWarrantyDueDate
                
                if AMCStartDate != "":
                    if AMCStartDate != "None":
                        AMCStartDate = (datetime.strptime(str(AMCStartDate), '%Y-%m-%d')).date()
                        AMCDueDate = (datetime.strptime(str(AMCDueDate), '%Y-%m-%d')).date()
                        # print(f"AMCStartDate: {AMCStartDate}, AMCDueDate: {AMCDueDate}")
                        if currentDate >= AMCStartDate and currentDate <= AMCDueDate:
                            warrantyStatus = "Under AMC  Warranty"
                            print(warrantyStatus)
                            warrantyEndDate = AMCDueDate
                
                if CMCStartDate != "":
                    if CMCStartDate != "None":
                        CMCStartDate = (datetime.strptime(str(CMCStartDate), '%Y-%m-%d')).date()
                        CMCDueDate = (datetime.strptime(str(CMCDueDate), '%Y-%m-%d')).date()
                        # print(f"CMCStartDate: {CMCStartDate}, CMCDueDate: {CMCDueDate}")
                        if currentDate >= CMCStartDate and currentDate <= CMCDueDate:
                            warrantyStatus = "Under CMC  Warranty"
                            print(warrantyStatus)
                            warrantyEndDate = CMCDueDate
                
                tempItemObj['WarrantyStatus'] = warrantyStatus
                tempItemObj['WarrantyEndDate'] = warrantyEndDate

                if Category.objects.filter(Number = ItemCategory).exists():
                    catObj = Category.objects.get(Number = ItemCategory)
                    tempItemObj['ItemCategoryName'] = catObj.GroupName
                else:
                    tempItemObj['ItemCategoryName'] = ""
                
                itemsData.append(tempItemObj)
            
            if AddressExtension.objects.filter(DeliveryId = DeliveryId).exists():
                addrObj = AddressExtension.objects.filter(DeliveryId = DeliveryId)[0]
                addrjson = AddressExtensionSerializer(addrObj)
                finalDeliveryData['AddressExtension'] = json.loads(json.dumps(addrjson.data))
            else:
                finalDeliveryData['AddressExtension'] = []

            finalDeliveryData['DocumentLines'] = itemsData
        else:
            finalDeliveryData['AddressExtension'] = {}
            finalDeliveryData['DocumentLines'] = []
        
        allDelivery.append(finalDeliveryData)
    return allDelivery