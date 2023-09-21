import requests, json
from django.shortcuts import render, redirect  
from django.http import JsonResponse, HttpResponse

from Category.models import Category
from Item.models import Tax

from .models import *

from rest_framework.decorators import api_view   
from rest_framework.response import Response
from .serializers import *

from Employee.models import Employee
from Employee.serializers import *

from BusinessPartner.models import *
from BusinessPartner.serializers import *
from Delivery.models import DocumentLines as DeliveryDocumentLines

from pytz import timezone
from datetime import datetime as dt

date = dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d')
yearmonth = dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m')
time = dt.now(timezone("Asia/Kolkata")).strftime('%H:%M %p')

from django.conf import settings

#Order Service Contract
@api_view(['POST'])
def createContract(request):
    try:
        OrderID = request.data['OrderID']
        AMCSalesOrderId = request.data['AMCSalesOrderId']
        CardCode = request.data['CardCode']
        BPName = request.data['BPName']
        ContractType = request.data['ContractType']
        BillAddrId = request.data['BillAddrId']
        BillAddr = request.data['BillAddr']
        ShipAddrId = request.data['ShipAddrId']
        ShipAddr = request.data['ShipAddr']
        U_STATUS = request.data['U_STATUS']
        U_CONTACTPER = request.data['U_CONTACTPER']
        serviceContractsItems = request.data['ServiceContractsItem']

        ServiceContracts(OrderID = OrderID, AMCSalesOrderId = AMCSalesOrderId, CardCode = CardCode, BPName = BPName, ContractType = ContractType, BillAddrId = BillAddrId, BillAddr = BillAddr, ShipAddrId = ShipAddrId, ShipAddr = ShipAddr, U_STATUS = U_STATUS, U_CONTACTPER = U_CONTACTPER).save()
        serviceContractId = ServiceContracts.objects.latest('id').id
        # print(serviceContractId)

        line = 0
        items = []
        ItemSerialNo = ""
        for serviceContractsItem in serviceContractsItems:
            ItemSerialNo = serviceContractsItem['ItemSerialNo']
            ServiceContractsItem(ServiceContractsId = serviceContractId, LineId = line, Frequency = serviceContractsItem['Frequency'], ItemCode = serviceContractsItem['ItemCode'], ItemName = serviceContractsItem['ItemName'], AMCItemCode = serviceContractsItem['AMCItemCode'], AMCItemName = serviceContractsItem['AMCItemName'], ItemSerialNo = serviceContractsItem['ItemSerialNo'], FromDate = serviceContractsItem['FromDate'], Todate = serviceContractsItem['Todate'], ItemAMT = serviceContractsItem['ItemAMT']).save()
            tempItem = {
                "LineId": line,
                "U_BIFRQ": serviceContractsItem['Frequency'],
                "U_ITMCD": serviceContractsItem['ItemCode'],
                "U_ITMNM": serviceContractsItem['ItemName'],
                "U_AMCINVIC": serviceContractsItem['AMCItemCode'],
                "U_AMCINVIN": serviceContractsItem['AMCItemName'],
                "U_SRNO": serviceContractsItem['ItemSerialNo'],
                "U_FRMDT": serviceContractsItem['FromDate'],
                "U_TODT": serviceContractsItem['Todate'],
                "U_AMT": serviceContractsItem['ItemAMT']
            }
            items.append(tempItem)
            line = line+1

        print("<><><><><><><><><><")
        sapDataContext = {
            "U_BPCODE": CardCode,
            "U_BPNAME": BPName,
            "U_CTRTYPE": ContractType,
            "U_BILLID": BillAddrId,
            "U_BILLADD": BillAddr,
            "U_SHIPID": ShipAddrId,
            "U_SHIPADD": ShipAddr,
            "U_STATUS": U_STATUS,
            "U_CONTACTPER": U_CONTACTPER,
            "CIN_MSC_C1Collection": items
        }
        print(sapDataContext)
        print("<><><><><><><><><><")
        # return Response({"message":"Success", "status":200,"data":[]})

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        AMCSalesOrder.objects.filter(pk = AMCSalesOrderId).update(ContractStatus = 'true') #
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        print("ItemSerialNo: ",ItemSerialNo)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if AMCOrderItem.objects.filter(AMCOrdId = AMCSalesOrderId).exists():
            amcItemDetials = AMCOrderItem.objects.filter(AMCOrdId = AMCSalesOrderId)[0]
            if str(ContractType) == "1":
                print("ContractType: ", ContractType)
                DeliveryDocumentLines.objects.filter(OrderId = amcItemDetials.OrderID, SerialNo = ItemSerialNo).update( ExtWarrantyStartDate = amcItemDetials.FromDate, ExtWarrantyDueDate = amcItemDetials.Todate)
            elif str(ContractType) == "2":
                print("ContractType: ", ContractType)
                DeliveryDocumentLines.objects.filter(OrderId = amcItemDetials.OrderID, SerialNo = ItemSerialNo).update( CMCStartDate = amcItemDetials.FromDate, CMCDueDate = amcItemDetials.Todate)
            elif str(ContractType) == "3":
                print("ContractType: ", ContractType)
                DeliveryDocumentLines.objects.filter(OrderId = amcItemDetials.OrderID, SerialNo = ItemSerialNo).update( AMCStartDate = amcItemDetials.FromDate, AMCDueDate = amcItemDetials.Todate)
            else:
                print(ContractType)
        else:
            print("No AMC Order Item")
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        sapdb = settings.SAPSESSION("api")
        # res = requests.post(sapdb['sapurl']+'/MSCONTR', data=json.dumps(sapDataContext), headers={'Authorization': "Bearer "+sapdb['SessionId']+""}, verify=False)
        res = settings.CALLAPI('post', '/MSCONTR', 'api', sapDataContext)
        live = json.loads(res.text)
        print(live)
        print("<><><><><><><><><><")
        if "DocEntry" in live:
            print(live['DocEntry'])
            docEntry = live['DocEntry']
            ServiceContracts.objects.filter(pk = serviceContractId).update(DocEntry = docEntry)
            ServiceContractsItem.objects.filter(ServiceContractsId = serviceContractId).update(DocEntry = docEntry)
            return Response({"message":"Success", "status":200,"data":[]})
        else:
            SAP_MSG = live['error']['message']['value']
            print(SAP_MSG)
            return Response({"message":SAP_MSG,"SAP_error":SAP_MSG, "status":202,"data":[]})
    except Exception as e:
        return Response({"message":str(e), "status":201,"data":[]})


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#list service order
@api_view(["GET"])
def allServiceContactList(request):
    try:
        serviceOrderObjs = ServiceContracts.objects.all().order_by('-id')
        finaldata = showServiceContract(serviceOrderObjs)
        return Response({"message":"Successfull","status":201,"data":finaldata})
    except Exception as e:
        return Response({"message":str(e),"status":201,"data":[]})

#list service order
@api_view(["POST"])
def orderWiseServiceContactList(request):
    # try:
        AMCSalesOrderId = request.data['AMCSalesOrderId']
        serviceOrderObjs = ServiceContracts.objects.filter(AMCSalesOrderId = AMCSalesOrderId)
        finaldata = showServiceContract(serviceOrderObjs)
        return Response({"message":"Successfull","status":201,"data":finaldata})
    # except Exception as e:
    #     return Response({"message":str(e),"status":201,"data":[]})


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def showServiceContract(objs):
    allContract = []
    for obj in objs:
        serviceContractsId = obj.id
        CardCode = obj.CardCode
        amcObj = ServiceContractsSerializer(obj)
        finalData = json.loads(json.dumps(amcObj.data))

        # if CardCode != "" and BusinessPartner.objects.filter(CardCode = CardCode).exists():
        if BusinessPartner.objects.filter(CardCode = CardCode).exists():
            bpObj = BusinessPartner.objects.filter(CardCode = CardCode).values('id', 'CardCode', 'CardName')
            bpJson = BusinessPartnerSerializer(bpObj, many=True)
            finalBP = json.loads(json.dumps(bpJson.data))

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            if BPAddresses.objects.filter(BPCode = CardCode).exists():
                bpAddr = BPAddresses.objects.filter(BPCode = CardCode)
                bpAddrJson = BPAddressesSerializer(bpAddr, many=True)
                finalBP[0]['BPAddresses'] = bpAddrJson.data
            else:
                finalBP[0]['BPAddresses'] = []

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            if BPEmployee.objects.filter(CardCode = CardCode).exists():
                bpEmp = BPEmployee.objects.filter(CardCode = CardCode)
                bpEmpJson = BPEmployeeSerializer(bpEmp, many=True)
                finalBP[0]['BPEmployee'] = bpEmpJson.data
            else:
                finalBP[0]['BPEmployee'] = []
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            finalData['BusinessPartner'] = finalBP
        else:
            finalData['BusinessPartner'] = []

        if ServiceContractsItem.objects.filter(ServiceContractsId = serviceContractsId).exists():
            ItemsObj = ServiceContractsItem.objects.filter(ServiceContractsId = serviceContractsId)
            ItemsJson = ServiceContractsItemSerializer(ItemsObj, many=True)
            finalData['ServiceContractsItem'] = ItemsJson.data
        allContract.append(finalData)
    return allContract