from django.shortcuts import render, redirect  
from django.http import JsonResponse, HttpResponse

from Category.models import Category
from Item.models import Tax

from Delivery.models import DocumentLines as DeliveryDocumentLines

from .models import *
from Employee.models import Employee
from Employee import views as EmpView
from BusinessPartner.models import *
from Opportunity.models import *
from Lead.models import Lead
import requests, json

from rest_framework.decorators import api_view    
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import JSONParser

from BusinessPartner.serializers import *
from Employee.serializers import *

from pytz import timezone
from datetime import datetime as dt

date = dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d')
yearmonth = dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m')
time = dt.now(timezone("Asia/Kolkata")).strftime('%H:%M %p')

from django.conf import settings

from global_fun import *

#added by millan on 28-09-2022
from Attachment.models import Attachment
from Attachment.serializers import AttachmentSerializer
import os
from django.core.files.storage import FileSystemStorage
#added by millan on 28-09-2022

# Create your views here.  

#Order Create API
@api_view(['POST'])
def createServiceOrder(request):
    local_order_id = 0
    try:
        TaxDate = request.data['TaxDate']
        DocDueDate = request.data['DocDueDate']
        ContactPersonCode = request.data['ContactPersonCode']
        DiscountPercent = request.data['DiscountPercent']
        DocDate = request.data['DocDate']
        CardCode = request.data['CardCode']
        CardName = request.data['CardName']
        Comments = request.data['Comments']
        SalesPersonCode = request.data['SalesPersonCode']
        CreateDate = request.data['CreateDate']
        CreateTime = request.data['CreateTime']
        UpdateDate = request.data['UpdateDate']
        UpdateTime = request.data['UpdateTime']
        
        PaymentGroupCode = request.data['PaymentGroupCode']
        BPLID = request.data['BPLID']
        U_Term_Condition = request.data['U_Term_Condition']
        U_TermInterestRate = request.data['U_TermInterestRate']
        U_TermPaymentTerm = request.data['U_TermPaymentTerm']
        U_TermDueDate = request.data['U_TermDueDate']
        
        U_QUOTNM = request.data['U_QUOTNM']
        U_QUOTID = request.data['U_QUOTID']    
        
        U_OPPID = request.data['U_OPPID']
        U_OPPRNM = request.data['U_OPPRNM']
        
        U_LEADID = request.data['U_LEADID']
        U_LEADNM = request.data['U_LEADNM']

        PoNo     = request.data['PoNo']
        PoDate   = request.data['PoDate']
        PoAmt    = request.data['PoAmt']
        PRID     = request.data['PRID']

        ShippingAndHandling  = request.data['ShippingAndHandling']
        TermsAndConditions   = request.data['TermsAndConditions']
        # lines = request.data['DocumentLines']
        
        #added by millan on 28-09-2022
        Attach = request.data['Attach']
        Caption = request.data['Caption']
        #added by millan on 28-09-2022
        
        lines = json.loads(request.data['DocumentLines'])
        print('----------------DocumentLines-----------------')
        print(lines)
        
        DocTotal=0
        for line in lines:
            DocTotal = float(DocTotal) + float(line['Quantity']) * float(line['UnitPrice'])
        print(DocTotal)
        
        model=Order(TaxDate = TaxDate, DocDueDate = DocDueDate, ContactPersonCode = ContactPersonCode, DiscountPercent = DiscountPercent, DocDate = DocDate, CardCode = CardCode, CardName = CardName, Comments = Comments, SalesPersonCode = SalesPersonCode, DocumentStatus="bost_Open", CancelStatus="csNo", DocTotal = DocTotal, CreateDate = CreateDate, CreateTime = CreateTime, UpdateDate = UpdateDate, UpdateTime = UpdateTime, PaymentGroupCode=PaymentGroupCode, BPLID=BPLID,U_Term_Condition=U_Term_Condition, U_TermInterestRate=U_TermInterestRate, U_TermPaymentTerm=U_TermPaymentTerm, U_TermDueDate=U_TermDueDate, U_OPPID=U_OPPID, U_OPPRNM=U_OPPRNM, U_QUOTNM=U_QUOTNM, U_QUOTID=U_QUOTID, U_LEADID=U_LEADID, U_LEADNM=U_LEADNM, PoNo = PoNo, PoAmt = PoAmt, PoDate = PoDate, PRID = PRID, ShippingAndHandling = ShippingAndHandling,TermsAndConditions = TermsAndConditions)
        
        model.save()
        
        qt = Order.objects.latest('id')
        local_order_id = qt.id

        #added by millan on 28-09-2022
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

            att=Attachment(File=attachmentsImage_url, Caption=Caption, LinkType="Order", LinkID=qt.id, CreateDate=CreateDate, CreateTime=CreateTime, UpdateDate=UpdateDate, UpdateTime=UpdateTime)
            
            att.save()
        
        try:
            addr = json.loads(request.data['AddressExtension'])
            model_add = AddressExtension(OrderID = qt.id, BillToBuilding = addr['BillToBuilding'], ShipToState = addr['ShipToState'], BillToCity = addr['BillToCity'], ShipToCountry = addr['ShipToCountry'], BillToZipCode = addr['BillToZipCode'], ShipToStreet = addr['ShipToStreet'], BillToState = addr['BillToState'], ShipToZipCode = addr['ShipToZipCode'], BillToStreet = addr['BillToStreet'], ShipToBuilding = addr['ShipToBuilding'], ShipToCity = addr['ShipToCity'], BillToCountry = addr['BillToCountry'], U_SCOUNTRY = addr['U_SCOUNTRY'], U_SSTATE = addr['U_SSTATE'], U_SHPTYPB = addr['U_SHPTYPB'], U_BSTATE = addr['U_BSTATE'], U_BCOUNTRY = addr['U_BCOUNTRY'], U_SHPTYPS = addr['U_SHPTYPS'])
            model_add.save()
        except Exception as e:
            Order.objects.filter(pk=qt.id).delete()
            return Response({"message":str(e),"status":201,"data":[]})

        try:
            LineNum = 0
            for line in lines:
                # if len(line['ReferenceItem']) != 0:
                #     ReferenceItemCode = line['ReferenceItem'][0]['ItemCode']
                # else:
                #     ReferenceItemCode = ""
                ReferenceItemCode = line['ReferenceItem']
                
                model_lines = DocumentLines(LineNum = LineNum, OrderID = qt.id, Quantity = line['Quantity'], UnitPrice = line['UnitPrice'], DiscountPercent = line['DiscountPercent'], ItemCode = line['ItemCode'], ItemDescription = line['ItemDescription'], TaxCode = line['TaxCode'], U_FGITEM = line['U_FGITEM'], CostingCode2 = line['CostingCode2'], ProjectCode = line['ProjectCode'], FreeText = line['FreeText'], Frequency = line['Frequency'], StartDate = line['StartDate'], EndDate = line['EndDate'], ReferenceItem = ReferenceItemCode)
                model_lines.save()
                LineNum=LineNum+1
        except Exception as e:
            DocumentLines.objects.filter(OrderID=qt.id).delete()
            AddressExtension.objects.filter(OrderID=qt.id).delete()
            Order.objects.filter(pk=qt.id).delete()
            return Response({"message":str(e),"status":201,"data":[]})
        
        qt_data = {
            "TaxDate": request.data['TaxDate'],
            "DocDueDate": request.data['DocDueDate'],
            "ContactPersonCode": request.data['ContactPersonCode'],
            "DiscountPercent": request.data['DiscountPercent'],
            "DocDate": request.data['DocDate'],
            "CardCode": request.data['CardCode'],
            "CardName": request.data['CardName'],
            "Comments": request.data['Comments'],
            "SalesPersonCode": request.data['SalesPersonCode'],
            "BPL_IDAssignedToInvoice": request.data['BPLID'],
            "PaymentGroupCode":request.data['PaymentGroupCode'],
            "U_PORTAL_NO":qt.id,
            "U_PRID": PRID,
            "NumAtCard": PoNo,
            "TaxDate": PoDate,
            "AddressExtension": {
                "BillToBuilding": addr['BillToBuilding'],
                "ShipToState": addr['ShipToState'],
                "BillToCity": addr['BillToCity'],
                "ShipToCountry": addr['ShipToCountry'],
                "BillToZipCode": addr['BillToZipCode'],
                "ShipToStreet": addr['ShipToStreet'],
                "BillToState": addr['BillToState'],
                "ShipToZipCode": addr['ShipToZipCode'],
                "BillToStreet": addr['BillToStreet'],
                "ShipToBuilding": addr['ShipToBuilding'],
                "ShipToCity": addr['ShipToCity'],
                "BillToCountry": addr['BillToCountry']
            },
            "DocumentLines": lines
        }
        
        
        #res = settings.CALLAPI('post', '/Orders', 'api', qt_data)
        #live = json.loads(res.text)
        
        fetchid = qt.id
        
        #---- stop SAP -----
        model = Order.objects.get(pk = fetchid)
        #model.DocEntry = live['DocEntry']
        model.DocEntry = qt.id
        model.save()
        if int(U_LEADID) !=0:
            leadObj = Lead.objects.get(pk=U_LEADID)
            leadObj.ODStatus=1
            leadObj.save()
        if U_OPPID !="":
            oppObj = Opportunity.objects.get(pk=U_OPPID)
            oppObj.ODStatus=1
            oppObj.save()
        
        report_SalesEmployeeCode = SalesPersonCode
        if Employee.objects.filter(SalesEmployeeCode=SalesPersonCode).exists():
            emp_obj =  Employee.objects.filter(SalesEmployeeCode=SalesPersonCode)
            report_obj = Employee.objects.get(SalesEmployeeCode=emp_obj[0].reportingTo)
            report_SalesEmployeeCode = report_obj.SalesEmployeeCode
        
        level = tree(SalesPersonCode) 
        print("Level: "+level)
        max = 5
        if AppSlave.objects.filter(Level=level).exists():
            slave_obj =  AppSlave.objects.filter(Level=level)
            min = slave_obj[0].Min
            max = slave_obj[0].Max


        if float(DiscountPercent) <=max:
            model.APPROVEID_id = SalesPersonCode
            model.FinalStatus = "Approved"
            if int(level) == 1:
                model.OrdLevel1_id = SalesPersonCode
                model.OrdLevel1Status = "Approved"
            elif int(level) == 2:
                model.OrdLevel2_id = SalesPersonCode
                model.OrdLevel2Status = "Approved"
            elif int(level) == 3:
                model.OrdLevel3_id = SalesPersonCode
                model.OrdLevel3Status = "Approved"
                
            model.save()
        else:
            model.FinalStatus = "Pending"

            if int(level) == 2:
                model.OrdLevel2_id = SalesPersonCode
                model.OrdLevel2Status = "Approved"
                model.OrdLevel1_id = report_obj[0].SalesEmployeeCode
                model.OrdLevel1Status = "Pending"
            elif int(level) == 3:
                model.OrdLevel3_id = SalesPersonCode
                model.OrdLevel3Status = "Approved"
                model.OrdLevel2_id = report_obj[0].SalesEmployeeCode
                model.OrdOrdLevel2Status = "Pending"
            elif int(level) == 4:
                model.OrdLevel3_id = report_obj[0].SalesEmployeeCode
                model.OrdLevel3Status = "Pending"
            model.save()
            
        
        return Response({"message":"successful","status":200,"data":[{"qt_Id":qt.id, "DocEntry":qt.id}]})        
        
        
        if "DocEntry" in live:
            print(live['DocEntry'])
            docEntry = live['DocEntry']

            documentLines = live['DocumentLines']
            # print(documentLines)
            for docline in documentLines:
                LineNum = docline['LineNum']
                TaxCode = docline['TaxCode']
                TaxRate = docline['TaxPercentagePerRow']

                if DocumentLines.objects.filter(OrderID = fetchid, LineNum = LineNum).exists():
                    DocumentLines.objects.filter(OrderID = fetchid, LineNum = LineNum).update(TaxCode = TaxCode, TaxRate = TaxRate)

            # print("==================================================")
            # print("=====================  AMC Order  ================")
            # print("==================================================")
            # lineNum = 0
            for line in lines:

                if line['IsService'] == "true":
                    print('in if')
                    referenceItems = line['ReferenceItem'][0]

                    lineNum = 0
                    if DocumentLines.objects.filter(OrderID = qt.id, ItemCode = referenceItems['ItemCode']).exists():
                        tempOBJ = DocumentLines.objects.get(OrderID = qt.id, ItemCode = referenceItems['ItemCode'])
                        lineNum = tempOBJ.LineNum
                    AMCSalesOrder(OrderID = fetchid, LineNum = lineNum, ItemCode = referenceItems['ItemCode'], ItemName = referenceItems['ItemDescription'], Frequency = line['Frequency'], CardCode = CardCode).save()
                    amcordId = AMCSalesOrder.objects.latest('id').id
                    AMCOrderItem(AMCOrdId = amcordId, OrderID = fetchid, LineNum = 0, ItemCode = line['ItemCode'], ItemName = line['ItemDescription'], FromDate = line['StartDate'], Todate = line['EndDate'], UnitPrice = line['UnitPrice'] ).save()

                    amcOrderContext = {
                        "U_ITMCD": referenceItems['ItemCode'],
                        "U_ITMNM": referenceItems['ItemDescription'],
                        "U_NOOFBILL": line['Frequency'],
                        "U_SLNUM": "", #"DocNum"
                        "U_SLENT": docEntry, #"DocEntry"
                        "U_Line": lineNum,
                        "U_EXWRSTDT": "",
                        "U_EXWREDDT": "",
                        "U_EXWRAMT": "",
                        "CIN_ORDR_C1Collection": [
                            {
                                "U_ITMCD": line['ItemCode'],
                                "U_ITMNM": line['ItemDescription'],
                                "U_FRMDT": line['StartDate'],
                                "U_TODT": line['EndDate'],
                                "U_AMT": line['UnitPrice']
                            }
                        ]
                    }
                    # print("----------------------------------------")
                    # print("--------- amcOrderContext --------------")
                    # print("----------------------------------------")
                    # print(amcOrderContext)
                    # amcSlOrdRes = requests.post(sapdb['sapurl']+'/ORDER', data=json.dumps(amcOrderContext), headers={'Authorization': "Bearer "+sapdb['SessionId']+""}, verify=False)
                    # print('sap response', amcSlOrdRes)
                    res = settings.CALLAPI('post', '/ORDER', 'api', amcOrderContext)
                    amcSlOrdResData = json.loads(res.text)
                    AMCSalesOrder.objects.filter(pk = amcordId).update(DocEntry = amcSlOrdResData['DocEntry'])
                else:
                    print('in else')
                # lineNum = lineNum+1
            
            model = Order.objects.get(pk = fetchid)
            model.DocEntry = live['DocEntry']
            model.save()
            if int(U_LEADID) !=0:
                leadObj = Lead.objects.get(pk=U_LEADID)
                leadObj.ODStatus=1
                leadObj.save()
            if U_OPPID !="":
                oppObj = Opportunity.objects.get(pk=U_OPPID)
                oppObj.ODStatus=1
                oppObj.save()
            
            report_SalesEmployeeCode = SalesPersonCode
            if Employee.objects.filter(SalesEmployeeCode=SalesPersonCode).exists():
                emp_obj =  Employee.objects.filter(SalesEmployeeCode=SalesPersonCode)
                report_obj = Employee.objects.get(SalesEmployeeCode=emp_obj[0].reportingTo)
                report_SalesEmployeeCode = report_obj.SalesEmployeeCode
            
            level = tree(SalesPersonCode) 
            print("Level: "+level)
            max = 5
            if AppSlave.objects.filter(Level=level).exists():
                slave_obj =  AppSlave.objects.filter(Level=level)
                min = slave_obj[0].Min
                max = slave_obj[0].Max


            if float(DiscountPercent) <=max:
                model.APPROVEID_id = SalesPersonCode
                model.FinalStatus = "Approved"
                if int(level) == 1:
                    model.OrdLevel1_id = SalesPersonCode
                    model.OrdLevel1Status = "Approved"
                elif int(level) == 2:
                    model.OrdLevel2_id = SalesPersonCode
                    model.OrdLevel2Status = "Approved"
                elif int(level) == 3:
                    model.OrdLevel3_id = SalesPersonCode
                    model.OrdLevel3Status = "Approved"
                    
                model.save()
            else:
                model.FinalStatus = "Pending"

                if int(level) == 2:
                    model.OrdLevel2_id = SalesPersonCode
                    model.OrdLevel2Status = "Approved"
                    model.OrdLevel1_id = report_obj[0].SalesEmployeeCode
                    model.OrdLevel1Status = "Pending"
                elif int(level) == 3:
                    model.OrdLevel3_id = SalesPersonCode
                    model.OrdLevel3Status = "Approved"
                    model.OrdLevel2_id = report_obj[0].SalesEmployeeCode
                    model.OrdOrdLevel2Status = "Pending"
                elif int(level) == 4:
                    model.OrdLevel3_id = report_obj[0].SalesEmployeeCode
                    model.OrdLevel3Status = "Pending"
                model.save()
                
            
            return Response({"message":"successful","status":200,"data":[{"qt_Id":qt.id, "DocEntry":live['DocEntry']}]})
        else:
            SAP_MSG = live['error']['message']['value']
            print(SAP_MSG)
            Order.objects.filter(id=qt.id).delete()
            allline = DocumentLines.objects.filter(OrderID=qt.id)
            for dcline in allline:
                dcline.delete()
                
            alladd = AddressExtension.objects.filter(OrderID=qt.id)
            for ad in alladd:
                ad.delete()
            return Response({"message":SAP_MSG,"SAP_error":SAP_MSG, "status":202,"data":[]})
    except Exception as e:
        if Order.objects.filter(pk=local_order_id).exists():
            if AddressExtension.objects.filter(OrderID=local_order_id).exists():
                AddressExtension.objects.filter(OrderID=local_order_id).delete()
            if DocumentLines.objects.filter(OrderID=local_order_id).exists():    
                DocumentLines.objects.filter(OrderID=local_order_id).delete()
            Order.objects.filter(pk=local_order_id).delete()
        return Response({"message":str(e), "status":201,"data":[]})


@api_view(['POST'])
def createAmcOrder(request):
    local_amc_order_id = 0
    try:
        CardCode = request.data['CardCode']
        # ItemId = request.data['ItemId']
        SerialNo = request.data['SerialNo']
        
        if DeliveryDocumentLines.objects.filter(SerialNo = SerialNo).exists():
            print('ok')
        else:
            return Response({"message":"Invalid SerialNo", "status":201,"data":[]})
            # itemObj = DocumentLines.objects.get(pk = ItemId)
            # OrderId = itemObj.OrderID
            # lineNum = itemObj.lineNum


        # lines = json.loads(request.data['DocumentLines'])
        lines = request.data['DocumentLines']
        # print('----------------DocumentLines-----------------')
        
        # print("==================================================")
        # print("=====================  AMC Order  ================")
        # print("==================================================")
        sapdb = settings.SAPSESSION("api")
        # lineNum = 0
        OrderId = 0
        amcordId = 0
        for line in lines:

            if line['IsService'] == "true":
                print('in if')

                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                # referenceItems = line['ReferenceItem']
                referenceItems = DeliveryDocumentLines.objects.get(SerialNo = SerialNo) # getting data form delivery items table
                OrderId = referenceItems.OrderId

                referenceOrder = Order.objects.get(pk = OrderId)
                lineNum = referenceItems.LineNum
                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                AMCSalesOrder(OrderID = OrderId, LineNum = lineNum, ItemCode = referenceItems.ItemCode, ItemName = referenceItems.ItemDescription, Frequency = line['Frequency'], CardCode = CardCode, ItemSerialNo = SerialNo).save()
                amcordId = AMCSalesOrder.objects.latest('id').id
                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                AMCOrderItem(AMCOrdId = amcordId, OrderID = OrderId, LineNum = 0, ItemCode = line['ItemCode'], ItemName = line['ItemDescription'], FromDate = line['StartDate'], Todate = line['EndDate'], UnitPrice = line['UnitPrice'] ).save()
                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

                amcOrderContext = {
                    "U_ITMCD": referenceItems.ItemCode,
                    "U_ITMNM": referenceItems.ItemDescription,
                    "U_NOOFBILL": line['Frequency'],
                    "U_SLNUM": "", #"DocNum"
                    "U_SLENT": referenceOrder.DocEntry, #"DocEntry"
                    "U_Line": lineNum,
                    "U_EXWRSTDT": "",
                    "U_EXWREDDT": "",
                    "U_EXWRAMT": "",
                    "CIN_ORDR_C1Collection": [
                        {
                            "U_ITMCD": line['ItemCode'],
                            "U_ITMNM": line['ItemDescription'],
                            "U_FRMDT": line['StartDate'],
                            "U_TODT": line['EndDate'],
                            "U_AMT": line['UnitPrice']
                        }
                    ]
                }
                # print("----------------------------------------")
                # print("--------- amcOrderContext --------------")
                # print("----------------------------------------")
                # print(amcOrderContext)
                # amcSlOrdRes = requests.post(sapdb['sapurl']+'/ORDER', data=json.dumps(amcOrderContext), headers={'Authorization': "Bearer "+sapdb['SessionId']+""}, verify=False)
                # amcSlOrdResData = json.loads(amcSlOrdRes.text)
                res = settings.CALLAPI('post', '/ORDER', 'api', amcOrderContext)
                amcSlOrdResData = json.loads(res.text)
                AMCSalesOrder.objects.filter(pk = amcordId).update(DocEntry = amcSlOrdResData['DocEntry'])
            else:
                print('in else')
                return Response({"message":"Please select service item", "status":201,"data":[]})

        return Response({"message":"successful","status":200,"data":[{"OrderId":OrderId, "AMCOrderId":amcordId}]})
    except Exception as e:
        return Response({"message":str(e), "status":201,"data":[]})


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@api_view(["POST"])
def all_filter_for_service(request):
    try: 
        SalesPersonID = request.data['SalesPersonCode']  
        if Employee.objects.filter(SalesEmployeeCode=SalesPersonID).exists():
            empids = EmpView.GetTeam(SalesPersonID,"Operation")            
            print(empids)
            quot_obj = Order.objects.filter(SalesPersonCode__in=empids).order_by("-id")
            print(quot_obj)
            allqt = OrderShow(quot_obj)
                
            return Response({"message": "Success","status": 200,"data":allqt})
        else:
            return Response({"message": "Unsuccess","status": 201,"data":[{"error":"SalesPersonCode invalid"}]})
    except Exception as e:
            return Response({"message": str(e), "status": 201, "data":[]})

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



def OrderShow(Orders_obj):
    allqt = [];
    for qt in Orders_obj:

        order_obj = OrderSerializer(qt)
        finalOrder = json.loads(json.dumps(order_obj.data))

        qtaddr = AddressExtension.objects.filter(OrderID=qt.id)
        qtaddr_json = AddressExtensionSerializer(qtaddr, many=True)
        
        jss_ = json.loads(json.dumps(qtaddr_json.data))
        for j in jss_:
            jss0=j
            finalOrder['AddressExtension'] = jss0
        
        lines = DocumentLines.objects.filter(OrderID=qt.id)
        print(lines)
        # lines_json = DocumentLinesSerializer(lines, many=True)
        # jss1 = json.loads(json.dumps(lines_json.data))
        # finalOrder['DocumentLines'] = jss1
        allLines = []
        for line in lines:
            print('-- in lines --')
            print(line.id)
            referenceItemid = line.ReferenceItem
            lineObj = DocumentLinesSerializer(line)
            linejson = json.loads(json.dumps(lineObj.data))
            cateObj = Category.objects.get(Number = line.ProjectCode)
            linejson['CategoryName'] = cateObj.GroupName
            linejson['IsService'] = cateObj.IsService

            # if referenceItemid != "":
            #     tempobj = DocumentLines.objects.filter(OrderID = qt.id, ItemCode = referenceItemid)
            #     tempjson = DocumentLinesSerializer(tempobj, many=True)
            #     linejson['ReferenceItem'] = tempjson.data
            # else:
            #     linejson['ReferenceItem'] = []
            
            allLines.append(linejson)
            print(linejson)

        finalOrder["DocumentLines"]= allLines

        cont = BPEmployee.objects.filter(InternalCode=qt.ContactPersonCode).values("InternalCode","FirstName")
        cont_json = BPEmployeeSerializer(cont, many=True)
        cont_all = json.loads(json.dumps(cont_json.data))
        # print(cont_all)
        if len(cont) > 0:
            #ContactPerson = cont[0].FirstName
            ContactPerson = cont_json.data
            print(ContactPerson)
        else:
            ContactPerson = []
            print(ContactPerson)

        #sobj = Employee.objects.filter(SalesEmployeeCode=qt.SalesPersonCode).values("SalesEmployeeCode","SalesEmployeeName")
        sobj = Employee.objects.filter(SalesEmployeeCode=qt.SalesPersonCode)
        sobj_json = EmployeeSerializer(sobj, many=True)
        sobj_all = json.loads(json.dumps(sobj_json.data))
        SalesPerson = sobj_json.data

        #added by millan on 28-09-2022
        try:
            if Attachment.objects.filter(LinkID = qt.id, LinkType="Order").exists():
                attachment_dls = Attachment.objects.filter(LinkID = qt.id, LinkType="Order")
                attachment_json = AttachmentSerializer(attachment_dls, many=True)
                finalOrder['Attach'] = attachment_json.data
            else:
                finalOrder['Attach'] = []
        except Exception as e:
            return Response({"message": str(e),"status": 201,"data":[]})
        #added by millan on 28-09-2022
        
        #added by millan on 16-11-2022 for showing business partner email based on card code
        if qt.CardCode != "":
            if BusinessPartner.objects.filter(CardCode = qt.CardCode).exists():
                bpemail_dls = BusinessPartner.objects.filter(CardCode = qt.CardCode).values_list('EmailAddress',flat=True)
                finalOrder['BPEmail'] = bpemail_dls[0]
            else:
                finalOrder['BPEmail'] = []
        else:
            finalOrder['BPEmail'] = []
        #added by millan on 16-11-2022 for showing business partner email based on card code
        
        finalOrder['ContactPersonCode'] = ContactPerson
        finalOrder['SalesPersonCode'] = SalesPerson
        
        allqt.append(finalOrder)
        
    return allqt

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def showServiceOrder(objs):
    allOrder = []
    for obj in objs:
        amcOrderId = obj.id
        CardCode = obj.CardCode
        amcObj = AMCSalesOrderSerializer(obj)
        finalData = json.loads(json.dumps(amcObj.data))

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

        if AMCOrderItem.objects.filter(AMCOrdId = amcOrderId).exists():
            amcItemsObj = AMCOrderItem.objects.filter(AMCOrdId = amcOrderId)
            amcItemsJson = AMCOrderItemSerializer(amcItemsObj, many=True)
            finalData['AMCOrderItem'] = amcItemsJson.data
        allOrder.append(finalData)
    return allOrder