#from ctypes.wintypes import PINT
from django.shortcuts import render, redirect  
from django.http import JsonResponse, HttpResponse

from Category.models import Category
from Item.models import Tax
from .models import *
from Employee.models import Employee
from BusinessPartner.models import *
from Opportunity.models import *
from Lead.models import Lead
import requests, json
from global_fun import *

from rest_framework.decorators import api_view    
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import JSONParser

from BusinessPartner.serializers import *
from Employee.serializers import *

from django.conf import settings
# Create your views here.  

#TenderQuotation Create API
@api_view(['POST'])
def create(request):
    try:
        TaxDate = request.data['TaxDate']
        DocDueDate = request.data['DocDueDate']
        DocDate = request.data['DocDate']
        ContactPersonCode = request.data['ContactPersonCode']
        DiscountPercent = request.data['DiscountPercent']
        CardCode = request.data['CardCode']
        CardName = request.data['CardName']
        Comments = request.data['Comments']
        SalesPersonCode = request.data['SalesPersonCode']
        U_OPPID = request.data['U_OPPID']
        U_TENDERID = request.data['U_TENDERID']
        U_OPPRNM = request.data['U_OPPRNM']
        U_QUOTNM = request.data['U_QUOTNM']
        U_PREQUOTATION = request.data['U_PREQUOTATION']
        U_PREQTNM = request.data['U_PREQTNM']
        U_LEADID = request.data['U_LEADID']
        U_LEADNM = request.data['U_LEADNM']        
        PaymentGroupCode = request.data['PaymentGroupCode']
        BPLID = request.data['BPLID']
        U_Term_Condition = request.data['U_Term_Condition']
        U_TermInterestRate = request.data['U_TermInterestRate']
        U_TermPaymentTerm = request.data['U_TermPaymentTerm']
        U_TermDueDate = request.data['U_TermDueDate']
        CreateDate = request.data['CreateDate']
        CreateTime = request.data['CreateTime']
        UpdateDate = request.data['UpdateDate']
        UpdateTime = request.data['UpdateTime']

        PoNo     = request.data['PoNo']
        PoDate   = request.data['PoDate']
        PoAmt    = request.data['PoAmt']
        PRID     = request.data['PRID']

        ShippingAndHandling  = request.data['ShippingAndHandling']
        TermsAndConditions   = request.data['TermsAndConditions']
        
        lines = request.data['DocumentLines']

        DocTotal=0
        for line in lines:
            DocTotal = float(DocTotal) + float(line['Quantity']) * float(line['UnitPrice'])
        print(DocTotal)


        model=TenderQuotation(TaxDate = TaxDate, DocDueDate = DocDueDate, ContactPersonCode = ContactPersonCode, DiscountPercent = DiscountPercent, DocDate = DocDate, CardCode = CardCode, CardName = CardName, Comments = Comments, SalesPersonCode = SalesPersonCode, DocumentStatus="bost_Open", CancelStatus="csNo", DocTotal = DocTotal, U_OPPID=U_OPPID, U_TENDERID=U_TENDERID, U_OPPRNM=U_OPPRNM, U_QUOTNM=U_QUOTNM, U_PREQUOTATION=U_PREQUOTATION, U_PREQTNM=U_PREQTNM, U_FAV='N', CreateDate = CreateDate, CreateTime = CreateTime, UpdateDate = UpdateDate, UpdateTime = UpdateTime, PaymentGroupCode=PaymentGroupCode, BPLID=BPLID, U_Term_Condition=U_Term_Condition, U_TermInterestRate=U_TermInterestRate, U_TermPaymentTerm=U_TermPaymentTerm, U_TermDueDate=U_TermDueDate, U_LEADID=U_LEADID, U_LEADNM=U_LEADNM, PoNo = PoNo, PoAmt = PoAmt, PoDate = PoDate, PRID = PRID, ShippingAndHandling = ShippingAndHandling,TermsAndConditions = TermsAndConditions)
        
        model.save()

        qt = TenderQuotation.objects.latest('id')
        
        addr = request.data['AddressExtension']
        
        model_add = AddressExtension(TenderQuotationID = qt.id, BillToBuilding = addr['BillToBuilding'], ShipToState = addr['ShipToState'], BillToCity = addr['BillToCity'], ShipToCountry = addr['ShipToCountry'], BillToZipCode = addr['BillToZipCode'], ShipToStreet = addr['ShipToStreet'], BillToState = addr['BillToState'], ShipToZipCode = addr['ShipToZipCode'], BillToStreet = addr['BillToStreet'], ShipToBuilding = addr['ShipToBuilding'], ShipToCity = addr['ShipToCity'], BillToCountry = addr['BillToCountry'], U_SCOUNTRY = addr['U_SCOUNTRY'], U_SSTATE = addr['U_SSTATE'], U_SHPTYPB = addr['U_SHPTYPB'], U_BSTATE = addr['U_BSTATE'], U_BCOUNTRY = addr['U_BCOUNTRY'], U_SHPTYPS = addr['U_SHPTYPS'])
        
        model_add.save()
        
        LineNum = 0
        #TaxCode = line['TaxCode'], 
        for line in lines:
            if len(line['ReferenceItem']) != 0:
                ReferenceItemCode = line['ReferenceItem'][0]['ItemCode']
            else:
                ReferenceItemCode = ""
                
            model_lines = DocumentLines(LineNum = LineNum, TenderQuotationID = qt.id, Quantity = line['Quantity'], UnitPrice = line['UnitPrice'], DiscountPercent = line['DiscountPercent'], ItemCode = line['ItemCode'], ItemDescription = line['ItemDescription'], U_FGITEM = line['U_FGITEM'], CostingCode2 = line['CostingCode2'], ProjectCode = line['ProjectCode'], FreeText = line['FreeText'], Frequency = line['Frequency'], StartDate = line['StartDate'], EndDate = line['EndDate'], ReferenceItem = ReferenceItemCode, ItemType = line['ItemType'])
            model_lines.save()
            LineNum=LineNum+1
        
        return Response({"message":"successful","status":200,"data":[{"qt_Id":qt.id}]})

        # with open("../bridge/bridge/db.json") as f:
        #     db = f.read()
        #     data = json.loads(db)
        
        # r = requests.post('http://157.241.48.182:50001/b1s/v1/Login', data=json.dumps(data), verify=False)
        # token = json.loads(r.text)['SessionId']
        # print(token)
        
        qt_data = {
            "TaxDate": request.data['TaxDate'],
            "DocDueDate": request.data['DocDueDate'],
            "DocDate": request.data['DocDate'],
            "ContactPersonCode": request.data['ContactPersonCode'],
            "DiscountPercent": request.data['DiscountPercent'],
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
                "BillToBuilding": request.data['AddressExtension']['BillToBuilding'],
                "ShipToState": request.data['AddressExtension']['ShipToState'],
                "BillToCity": request.data['AddressExtension']['BillToCity'],
                "ShipToCountry": request.data['AddressExtension']['ShipToCountry'],
                "BillToZipCode": request.data['AddressExtension']['BillToZipCode'],
                "ShipToStreet": request.data['AddressExtension']['ShipToStreet'],
                "BillToState": request.data['AddressExtension']['BillToState'],
                "ShipToZipCode": request.data['AddressExtension']['ShipToZipCode'],
                "BillToStreet": request.data['AddressExtension']['BillToStreet'],
                "ShipToBuilding": request.data['AddressExtension']['ShipToBuilding'],
                "ShipToCity": request.data['AddressExtension']['ShipToCity'],
                "BillToCountry": request.data['AddressExtension']['BillToCountry']
            },
            "DocumentLines": lines
        }
        
        # print(qt_data)
        # print(json.dumps(qt_data))

        # res = requests.post('http://157.241.48.182:50001/b1s/v1/TenderQuotations', data=json.dumps(qt_data), cookies=r.cookies, verify=False)
        
        sapdb = settings.SAPSESSION("api")
        
        res = requests.post(sapdb['sapurl']+'/TenderQuotations', data=json.dumps(qt_data), headers={'Authorization': "Bearer "+sapdb['SessionId']+""}, verify=False)
        
        live = json.loads(res.text)
        
        print('-------- response --------')
        # print(live)
        fetchid = qt.id
        
        if "DocEntry" in live:
            print(live['DocEntry'])

            documentLines = live['DocumentLines']
            # print(documentLines)
            for docline in documentLines:
                LineNum = docline['LineNum']
                TaxCode = docline['TaxCode']
                TaxRate = docline['TaxPercentagePerRow']

                if DocumentLines.objects.filter(TenderQuotationID = fetchid, LineNum = LineNum).exists():
                    DocumentLines.objects.filter(TenderQuotationID = fetchid, LineNum = LineNum).update(TaxCode = TaxCode, TaxRate = TaxRate)

                print('------ SAP docline update--------')
                # print('data', LineNum,TaxCode, TaxRate)
                # print('data', TaxCode, TaxRate)
            
            model = TenderQuotation.objects.get(pk = fetchid)
            model.DocEntry = live['DocEntry']
            model.save()
            if int(U_LEADID) !=0:
                leadObj = Lead.objects.get(pk=U_LEADID)
                leadObj.QTStatus=1
                leadObj.save()
            if U_OPPID !="":
                oppObj = Opportunity.objects.get(pk=U_OPPID)
                oppObj.QTStatus=1
                oppObj.save()
            
            emp_obj =  Employee.objects.filter(SalesEmployeeCode=SalesPersonCode)
            report_obj = Employee.objects.filter(SalesEmployeeCode=emp_obj[0].reportingTo)

            level = tree(SalesPersonCode) 
            print("Level: "+level)
            slave_obj =  AppSlave.objects.filter(Level=level)
            # min = slave_obj[0].Min
            # max = slave_obj[0].Max
            discountPercentage = 5
            print('-----------appslave----------')
            if len(slave_obj) != 0:
                print(slave_obj[0].Max)
                discountPercentage = slave_obj[0].Max

            # if float(DiscountPercent) <=max:
            if float(DiscountPercent) <= discountPercentage:
                model.APPROVEID_id = SalesPersonCode
                model.FinalStatus = "Approved"
                if int(level) == 1:
                    model.Level1_id = SalesPersonCode
                    model.Level1Status = "Approved"
                elif int(level) == 2:
                    model.Level2_id = SalesPersonCode
                    model.Level2Status = "Approved"
                elif int(level) == 3:
                    model.Level3_id = SalesPersonCode
                    model.Level3Status = "Approved"
                    
                model.save()
            else:
                model.FinalStatus = "Pending"

                if int(level) == 2:
                    model.Level2_id = SalesPersonCode
                    model.Level2Status = "Approved"
                    model.Level1_id = report_obj[0].SalesEmployeeCode
                    model.Level1Status = "Pending"
                elif int(level) == 3:
                    model.Level3_id = SalesPersonCode
                    model.Level3Status = "Approved"
                    model.Level2_id = report_obj[0].SalesEmployeeCode
                    model.Level2Status = "Pending"
                elif int(level) == 4:
                    model.Level3_id = report_obj[0].SalesEmployeeCode
                    model.Level3Status = "Pending"
                model.save()
            
            return Response({"message":"successful","status":200,"data":[{"qt_Id":qt.id, "DocEntry":live['DocEntry']}]})
        else:
            SAP_MSG = live['error']['message']['value']
            print(SAP_MSG)
            TenderQuotation.objects.filter(id=qt.id).delete()
            allline = DocumentLines.objects.filter(TenderQuotationID=qt.id)
            for dcline in allline:
                dcline.delete()
                
            alladd = AddressExtension.objects.filter(TenderQuotationID=qt.id)
            for ad in alladd:
                ad.delete()
            return Response({"message":SAP_MSG,"SAP_error":SAP_MSG, "status":202,"data":[]})
    except Exception as e:
        return Response({"message":str(e), "status":202,"data":[]})


#TenderQuotation Fav Update API
@api_view(['POST'])
def fav(request):
    fetchid = request.data['id']
    model = TenderQuotation.objects.get(pk = fetchid)
    model.U_FAV  = request.data['U_FAV']
    model.save()
    return Response({"message":"successful","status":200, "data":[]})

#TenderQuotation Update API
@api_view(['POST'])
def approve(request):
    SalesEmployeeCode = request.data['SalesEmployeeCode']
    qtid = request.data['id']
    FinalStatus = request.data['FinalStatus']
    Remarks = request.data['Remarks']
    #SalesEmployeeCode=2 #salesman
    #SalesEmployeeCode=1 #manager
    #SalesEmployeeCode=38 #admin
    try:
        # UPDATE `quotation_quotation` SET `APPROVEID_id`= NULL, `FinalStatus`="", `Level3_id` = NULL, `Level2_id` = NULL, `Level1_id` = NULL, `Level3Status` = "", `Level2Status` = "", `Level1Status` = "" WHERE `quotation_quotation`.`id` = 30;
        level = tree(SalesEmployeeCode) 
        print("Level: "+level)
        slave_obj =  AppSlave.objects.filter(Level=level)
        min = slave_obj[0].Min
        max = slave_obj[0].Max

        print(str(min)+"-"+str(max))

        qt =  TenderQuotation.objects.get(pk=qtid)
        dis=qt.DiscountPercent
        print(str(dis)+"%")
        #FinalStatus = "Approved"
        #FinalStatus = "Rejected"

        #if dis >= float(min) and dis <= float(max):
        if dis <= float(max):
            print("appr")
            print('"ApprovedID":'+str(SalesEmployeeCode)+'')
            qt.APPROVEID_id = SalesEmployeeCode
            qt.FinalStatus = FinalStatus

            if int(level) == 1:
                qt.Level1_id =SalesEmployeeCode
                qt.Level1Status = FinalStatus
            elif int(level) == 2:
                qt.Level2_id =SalesEmployeeCode
                qt.Level2Status = FinalStatus
            elif int(level) == 3:
                qt.Level3_id =SalesEmployeeCode
                qt.Level3Status = FinalStatus
            
            qt.save()

            print('"FinalStatus":'+FinalStatus)
        else:
            #print("send for appr")
            #SELECT * FROM `quotation_appslave` WHERE Min <= 11 and Max >=11;
            slave_obj =  AppSlave.objects.filter(Min__lte=dis, Max__gte=dis)
            #print(slave_obj)
            
            emp_obj =  Employee.objects.filter(SalesEmployeeCode=SalesEmployeeCode)
            report_obj = Employee.objects.filter(SalesEmployeeCode=emp_obj[0].reportingTo)
            #print("Send to Level "+str(slave_obj[0].Level))
            #print("Send to Level "+emp_obj1[0].role)
            print("_____")
            print("Send for Approve -- Role:--" + report_obj[0].role+ "; SalesEmployeeCode:-- "+report_obj[0].SalesEmployeeCode)    
            print("Send for Final -- Level "+str(slave_obj[0].Level))
            print("_____")
            print('"ApprovedID":null')
            print('"FinalStatus":"Pending"')
            if FinalStatus == "Rejected":        
                qt.APPROVEID_id = SalesEmployeeCode
                qt.FinalStatus = FinalStatus
            else:
                qt.FinalStatus = "Pending"

            if int(level) == 1:
                qt.Level1_id =SalesEmployeeCode
                qt.Level1Status = FinalStatus
            elif int(level) == 2:
                qt.Level2_id =SalesEmployeeCode
                qt.Level2Status = FinalStatus
                qt.Level1_id = report_obj[0].SalesEmployeeCode
                qt.Level1Status = "Pending"
            elif int(level) == 3:
                qt.Level3_id =SalesEmployeeCode
                qt.Level3Status = FinalStatus
                qt.Level2_id = report_obj[0].SalesEmployeeCode
                qt.Level2Status = "Pending"
            qt.save()
            print("_____")
        
        return Response({"message":"Success","status":200,"data":[]})

    except Exception as e:
        return Response({"message":str(e),"status":201,"data":[{"Error":str(e)}]})

#TenderQuotation pending for approval
@api_view(["POST"])
def pending(request):
    SalesEmployeeCode = request.data['SalesEmployeeCode']
    level = tree(SalesEmployeeCode)
    print(level)
    if int(level) == 3:
        quot_obj = TenderQuotation.objects.filter(Level3_id=SalesEmployeeCode,Level3Status="Pending").order_by("-id")
    elif int(level) == 2:
        quot_obj = TenderQuotation.objects.filter(Level2_id=SalesEmployeeCode,Level2Status="Pending").order_by("-id")
    elif int(level) == 1:
        quot_obj = TenderQuotation.objects.filter(Level1_id=SalesEmployeeCode,Level1Status="Pending").order_by("-id")
    print(quot_obj)

    allqt = TenderQuotationShow(quot_obj)                        
    return Response({"message": "Success","status": 200,"data":allqt})

#Rejected TenderQuotations list
@api_view(["POST"])
def rejected(request):
    try:
        SalesEmployeeCode = request.data['SalesEmployeeCode']
        level = tree(SalesEmployeeCode)
        print(level)
        if int(level) == 3:
            quot_obj = TenderQuotation.objects.filter(Level3_id=SalesEmployeeCode,Level3Status="Rejected").order_by("-id")
        elif int(level) == 2:
            quot_obj = TenderQuotation.objects.filter(Level2_id=SalesEmployeeCode,Level2Status="Rejected").order_by("-id")
        elif int(level) == 1:
            quot_obj = TenderQuotation.objects.filter(Level1_id=SalesEmployeeCode,Level1Status="Rejected").order_by("-id")
        print(quot_obj)

        allqt = TenderQuotationShow(quot_obj)                        
        return Response({"message": "Success","status": 200,"data":allqt})
    except Exception as e:
        return Response({"message": "Error","status": 201,"data":[str(e)]})


#TenderQuotation pending for approval
@api_view(["POST"])
def approved(request):
    SalesEmployeeCode = request.data['SalesEmployeeCode']
    level = tree(SalesEmployeeCode)
    print(level)
    if int(level) == 3:
        quot_obj = TenderQuotation.objects.filter(Level3_id=SalesEmployeeCode,Level3Status="Approved").order_by("-id")
    elif int(level) == 2:
        quot_obj = TenderQuotation.objects.filter(Level2_id=SalesEmployeeCode,Level2Status="Approved").order_by("-id")
    elif int(level) == 1:
        quot_obj = TenderQuotation.objects.filter(FinalStatus="Approved").order_by("-id")
    print(quot_obj)

    allqt = TenderQuotationShow(quot_obj)                        
    return Response({"message": "Success","status": 200,"data":allqt})


#TenderQuotation Update API
@api_view(['POST'])
def approve_old(request):
    fetchid = request.data['id']
    try:
        model = TenderQuotation.objects.get(pk = fetchid)
        model.U_APPROVEID = request.data['U_APPROVEID']
        model.U_APPROVENM = request.data['U_APPROVENM']
        model.save()
        return Response({"message":"successful","status":200, "data":[]})
    except Exception as e:
        return Response({"message":"Not Update","status":201,"data":[{"Error":str(e)}]})

#TenderQuotation Update API

@api_view(['POST'])
def update(request):
    fetchid = request.data['id']
    try:
        model = TenderQuotation.objects.get(pk = fetchid)
        model.TaxDate = request.data['TaxDate']
        model.DocDate = request.data['DocDate']
        model.DocDueDate = request.data['DocDueDate']
        model.ContactPersonCode = request.data['ContactPersonCode']
        model.DiscountPercent = request.data['DiscountPercent']
        model.Comments = request.data['Comments']
        model.SalesPersonCode = request.data['SalesPersonCode']

        model.PaymentGroupCode = request.data['PaymentGroupCode']
        
        model.U_Term_Condition = request.data['U_Term_Condition']
        model.U_TermInterestRate = request.data['U_TermInterestRate']
        model.U_TermPaymentTerm = request.data['U_TermPaymentTerm']
        model.U_TermDueDate = request.data['U_TermDueDate']
        
        model.BPLID = request.data['BPLID']
        
        model.U_QUOTNM = request.data['U_QUOTNM']
        model.U_PREQUOTATION = request.data['U_PREQUOTATION']
        
        model.UpdateDate = request.data['UpdateDate']
        model.UpdateTime = request.data['UpdateTime']

        model.PoNo = request.data['PoNo']
        model.PoAmt = request.data['PoAmt']
        model.PoDate = request.data['PoDate']
        model.PRID = request.data['PRID']

        model.ShippingAndHandling = request.data['ShippingAndHandling']
        model.TermsAndConditions = request.data['TermsAndConditions']

        model.save()
        
        if AddressExtension.objects.filter(id = request.data['AddressExtension']['id']).exists():
            model_add = AddressExtension.objects.get(id = request.data['AddressExtension']['id'])
            print(model_add)
            
            model_add.BillToBuilding = request.data['AddressExtension']['BillToBuilding']
            model_add.ShipToState = request.data['AddressExtension']['ShipToState']
            model_add.BillToCity = request.data['AddressExtension']['BillToCity']
            model_add.ShipToCountry = request.data['AddressExtension']['ShipToCountry']
            model_add.BillToZipCode = request.data['AddressExtension']['BillToZipCode']
            model_add.ShipToStreet = request.data['AddressExtension']['ShipToStreet']
            model_add.BillToState = request.data['AddressExtension']['BillToState']
            model_add.ShipToZipCode = request.data['AddressExtension']['ShipToZipCode']
            model_add.BillToStreet = request.data['AddressExtension']['BillToStreet']
            model_add.ShipToBuilding = request.data['AddressExtension']['ShipToBuilding']
            model_add.ShipToCity = request.data['AddressExtension']['ShipToCity']
            model_add.BillToCountry = request.data['AddressExtension']['BillToCountry']
            model_add.U_SCOUNTRY = request.data['AddressExtension']['U_SCOUNTRY']
            model_add.U_SSTATE = request.data['AddressExtension']['U_SSTATE']
            model_add.U_SHPTYPB = request.data['AddressExtension']['U_SHPTYPB']
            model_add.U_BSTATE = request.data['AddressExtension']['U_BSTATE']
            model_add.U_BCOUNTRY = request.data['AddressExtension']['U_BCOUNTRY']
            model_add.U_SHPTYPS = request.data['AddressExtension']['U_SHPTYPS']
    
            model_add.save()
            print("add save")
        
        lines = request.data['DocumentLines']
        updatedItemIds = []
        for line in lines:

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            if len(line['ReferenceItem']) != 0:
                ReferenceItemCode = line['ReferenceItem'][0]['ItemCode']
            else:
                ReferenceItemCode = ""
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            if line["id"] !="":
                model_line = DocumentLines.objects.get(pk = line['id'])
                model_line.Quantity=line['Quantity']
                model_line.UnitPrice=line['UnitPrice']
                model_line.DiscountPercent=line['DiscountPercent']
                model_line.ItemCode=line['ItemCode']
                model_line.ItemDescription=line['ItemDescription']
                model_line.TaxCode=line['TaxCode']            
                # model_line.ItemType=line['ItemType']         
                model_line.FreeText=line['FreeText']            
                model_line.CostingCode2=line['CostingCode2']
                model_line.Frequency       = line['Frequency']   
                model_line.StartDate       = line['StartDate']   
                model_line.EndDate         = line['EndDate']   
                model_line.ReferenceItem   = ReferenceItemCode            
                model_line.save()

                updatedItemIds.append(line['id'])
                print("update tdquotation item id", line['id'])
            else:
                NewLine = 0
                if DocumentLines.objects.filter(TenderQuotationID = fetchid).exists():
                    lastline = DocumentLines.objects.filter(TenderQuotationID = fetchid).order_by('-LineNum')[:1]
                    NewLine = int(lastline[0].LineNum) + 1
                
                model_lines = DocumentLines(TenderQuotationID = fetchid, LineNum=NewLine, Quantity = line['Quantity'], UnitPrice = line['UnitPrice'], DiscountPercent = line['DiscountPercent'], ItemCode = line['ItemCode'], ItemDescription = line['ItemDescription'], U_FGITEM = line['U_FGITEM'], CostingCode2 = line['CostingCode2'], ProjectCode = line['ProjectCode'], FreeText = line['FreeText'], Frequency = line['Frequency'], StartDate = line['StartDate'], EndDate = line['EndDate'], ReferenceItem = ReferenceItemCode)
                model_lines.save()
                quotObj = DocumentLines.objects.latest('id')
                updatedItemIds.append(quotObj.id)
                print("new tdquotation item id", quotObj.id)

        print("ids", updatedItemIds)

        if DocumentLines.objects.filter(TenderQuotationID = fetchid).exclude(id__in = updatedItemIds).exists():
            DocumentLines.objects.filter(TenderQuotationID = fetchid).exclude(id__in = updatedItemIds).delete()

        # with open("../bridge/bridge/db.json") as f:
        #     db = f.read()
        #     data = json.loads(db)
        
        # r = requests.post('http://157.241.48.182:50001/b1s/v1/Login', data=json.dumps(data), verify=False)
        # token = json.loads(r.text)['SessionId']
        # print(token)
        
        qt_data = {
            "TaxDate": request.data['TaxDate'],
            "DocDueDate": request.data['DocDueDate'],
            "DocDate": request.data['DocDate'],
            "ContactPersonCode": request.data['ContactPersonCode'],
            "DiscountPercent": request.data['DiscountPercent'],
            "Comments": request.data['Comments'],
            "SalesPersonCode": request.data['SalesPersonCode'],
            "BPL_IDAssignedToInvoice": request.data['BPLID'],
            "PaymentGroupCode":request.data['PaymentGroupCode'],
            "U_PRID": request.data['PRID'],
            "NumAtCard": request.data['PoNo'],
            "TaxDate": request.data['PoDate'],
            "AddressExtension": {
                "BillToBuilding": request.data['AddressExtension']['BillToBuilding'],
                "ShipToState": request.data['AddressExtension']['ShipToState'],
                "BillToCity": request.data['AddressExtension']['BillToCity'],
                "ShipToCountry": request.data['AddressExtension']['ShipToCountry'],
                "BillToZipCode": request.data['AddressExtension']['BillToZipCode'],
                "ShipToStreet": request.data['AddressExtension']['ShipToStreet'],
                "BillToState": request.data['AddressExtension']['BillToState'],
                "ShipToZipCode": request.data['AddressExtension']['ShipToZipCode'],
                "BillToStreet": request.data['AddressExtension']['BillToStreet'],
                "ShipToBuilding": request.data['AddressExtension']['ShipToBuilding'],
                "ShipToCity": request.data['AddressExtension']['ShipToCity'],
                "BillToCountry": request.data['AddressExtension']['BillToCountry']
            },
            "DocumentLines": lines
        }
        
        print(qt_data)
        print(json.dumps(qt_data))
        return Response({"message":"successful","status":200, "data":[json.loads(json.dumps(request.data))]})   
    except Exception as e:
        return Response({"message":"Not Update","status":201,"data":[{"Error":str(e)}]})

#TenderQuotation All API
@api_view(["GET"])
def all_old(request):
    quot_obj = TenderQuotation.objects.all().order_by("-id")    
    quot_json = TenderQuotationSerializer(quot_obj, many=True)
    return Response({"message": "Success","status": 200,"data":quot_json.data})

#TenderQuotation All API
@api_view(["GET"])
def all(request):
    allqt = [];
    quot_obj = TenderQuotation.objects.all().order_by("-id")    
    allqt = TenderQuotationShow(quot_obj)    
    return Response({"message": "Success","status": 200,"data":allqt})

def TenderQuotationShow(quot_obj):
    allqt = []
    for qt in quot_obj:
    
        qtobj = TenderQuotation.objects.get(pk=qt.id)
        qt_json = TenderQuotationSerializer(qtobj, many=False)
        quot = json.loads(json.dumps(qt_json.data))
        
        if AddressExtension.objects.filter(TenderQuotationID=qt.id).exists():
            qtaddr = AddressExtension.objects.filter(TenderQuotationID=qt.id)
            qtaddr_json = AddressExtensionSerializer(qtaddr, many=True)
            quot["AddressExtension"]= qtaddr_json.data[0]
        else:
            quot["AddressExtension"]= {"id":"","TenderQuotationID":"","BillToBuilding":"","ShipToState":"","BillToCity":"","ShipToCountry":"","BillToZipCode":"","ShipToStreet":"","BillToState":"","ShipToZipCode":"","BillToStreet":"","ShipToBuilding":"","ShipToCity":"","BillToCountry":"","U_SCOUNTRY":"","U_SSTATE":"","U_SHPTYPB":"","U_BSTATE":"","U_BCOUNTRY":"","U_SHPTYPS":""}

        
        lines = DocumentLines.objects.filter(TenderQuotationID=qt.id)
        # lines_json = DocumentLinesSerializer(lines, many=True)
        allLines = []
        for line in lines:
            referenceItemid = line.ReferenceItem
            lineObj = DocumentLinesSerializer(line)
            linejson = json.loads(json.dumps(lineObj.data))
            # if Category.objects.filter(Number = line.ProjectCode).exists():
            if str(line.ProjectCode) != "":
                cateObj = Category.objects.get(Number = line.ProjectCode)
                linejson['CategoryName'] = cateObj.GroupName
                linejson['IsService'] = cateObj.IsService
            else:
                linejson['CategoryName'] = ""
                linejson['IsService'] = ""
                

            if referenceItemid != "":
                tempobj = DocumentLines.objects.filter(TenderQuotationID = qt.id, ItemCode = referenceItemid)
                tempjson = DocumentLinesSerializer(tempobj, many=True)
                linejson['ReferenceItem'] = tempjson.data
            else:
                linejson['ReferenceItem'] = []
            allLines.append(linejson)

        quot["DocumentLines"]= allLines

        cont = BPEmployee.objects.filter(InternalCode=qt.ContactPersonCode).values("InternalCode","FirstName")
        cont_json = BPEmployeeSerializer(cont, many=True)
        cont_all = json.loads(json.dumps(cont_json.data))
        print(cont_all)
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

        quot["ContactPersonCode"]= ContactPerson
        quot["SalesPersonCode"]= SalesPerson
        
        #added by millan on 16-11-2022 for showing business partner email based on card code
        if qt.CardCode != "":
            if BusinessPartner.objects.filter(CardCode = qt.CardCode).exists():
                bpemail_dls = BusinessPartner.objects.filter(CardCode = qt.CardCode).values_list('EmailAddress',flat=True)
                quot['BPEmail'] = bpemail_dls[0]
            else:
                quot['BPEmail'] = []
        else:
            quot['BPEmail'] = []
        #added by millan on 16-11-2022 for showing business partner email based on card code
        
            
        #allqt.append(context)
        allqt.append(quot)
    return allqt

#TenderQuotation All API
@api_view(["POST"])
def all_filter(request):
    try: 
        json_data = request.data 
        if "U_OPPID" in json_data:
            if json_data['U_OPPID'] !='':
                
                quot_obj = TenderQuotation.objects.filter(U_OPPID=json_data['U_OPPID']).order_by("-id")
                if len(quot_obj) ==0:
                    return Response({"message": "Success","status": 200,"data":[]})
                else:
                    
                    allqt = TenderQuotationShow(quot_obj)
                            
                return Response({"message": "Success","status": 200,"data":allqt})     

        if "SalesPersonCode" in json_data:            
            SalesPersonID = json_data['SalesPersonCode']       
            if Employee.objects.filter(SalesEmployeeCode=SalesPersonID).exists():
                empids = getAllReportingToIdsSubdep(SalesPersonID, "Sales")            
                """
                empids = []
                roles = ['support manager', 'support', 'engineer']
                emp_obj =  Employee.objects.get(SalesEmployeeCode=SalesPersonID)
                if emp_obj.role == 'admin':
                    print('-- Admin --')
                    empids = Employee.objects.filter(SalesEmployeeCode__gt=0).exclude(role__in = roles).values_list('SalesEmployeeCode', flat=True)
                    # empids = Employee.objects.filter(SalesEmployeeCode__gt=0).values_list('SalesEmployeeCode', flat=True)
                    empids = list(empids)
                    # empids.append(SalesEmployeeCode)                   
                elif emp_obj.role == 'manager':
                    print('--- manager---')
                    empids = Employee.objects.filter(reportingTo = SalesPersonID).exclude(role__in = roles).values_list('SalesEmployeeCode', flat=True)
                    # empids = Employee.objects.filter(reportingTo = SalesPersonID).values_list('SalesEmployeeCode', flat=True)
                    empids = list(empids)
                    empids.append(SalesPersonID)
                else:
                    empids=[SalesPersonID]
                
                """
                print(empids)
                
                for ke in json_data.keys():
                    if ke =='U_FAV' :
                        print("yes filter")
                        if json_data['U_FAV'] !='':
                            quot_obj = TenderQuotation.objects.filter(SalesPersonCode__in=empids, U_FAV=json_data['U_FAV']).order_by("-id")
                            if len(quot_obj) ==0:
                                return Response({"message": "Not Available","status": 201,"data":[]})
                            else:
                                allqt = TenderQuotationShow(quot_obj)
                                return Response({"message": "Success","status": 200,"data":allqt})
                    
                    else:
                        print("no filter")
                        quot_obj = TenderQuotation.objects.filter(SalesPersonCode__in=empids).order_by("-id")
                        allqt = TenderQuotationShow(quot_obj)
                            
                        return Response({"message": "Success","status": 200,"data":allqt})
            else:
                return Response({"message": "Unsuccess","status": 201,"data":[{"error":"SalesPersonCode not found?"}]})
        else:
            print("no")
            return Response({"message": "Unsuccess","status": 201,"data":[{"error":"SalesPersonCode?"}]})
    except Exception as e:
            return Response({"message": str(e), "status": 201, "data":[]})


#TenderQuotation One API
@api_view(["POST"])
def one(request):
    tdid=request.data['tdid']
    quot_obj = TenderQuotation.objects.filter(U_TENDERID=tdid)
    allqt = TenderQuotationShow(quot_obj)
    
    return Response({"message": "Success","status": 200,"data":allqt})

#TenderQuotation Cancel
@api_view(['POST'])
def cancel(request):
    fetchid=request.data['DocEntry']
    try:
        odr=TenderQuotation.objects.get(DocEntry=fetchid)
        odr.DocumentStatus='bost_Close'
        odr.CancelStatus='csYes'
        odr.FinalStatus='Cancel'
        odr.save()
        # with open("../bridge/bridge/db.json") as f:
        #     db = f.read()
        # print(db)
        # data = json.loads(db)
        # print(data)
    
        try:
            # r = requests.post('http://157.241.48.182:50001/b1s/v1/Login', data=json.dumps(data), verify=False)
            # token = json.loads(r.text)['SessionId']
            # print(token)
            # res = requests.post('http://157.241.48.182:50001/b1s/v1/TenderQuotations('+fetchid+')/Cancel', cookies=r.cookies, verify=False)
            
            sapdb = settings.SAPSESSION("api")
            
            res = requests.post(sapdb['sapurl']+'/TenderQuotations('+fetchid+')/Cancel', headers={'Authorization': "Bearer "+sapdb['SessionId']+""}, verify=False)
            return Response({"message":"successful","status":200,"data":[]})
        except:
            return Response({"message":"successful","status":200,"data":[]})        
    except Exception as e:
         return Response({"message":str(e),"status":201,"data":[]})
