from django.shortcuts import render, redirect  
from django.http import JsonResponse, HttpResponse

from Category.models import Category
from Item.models import Tax

from .models import *
from Employee.models import Employee
from Employee import views as EmpView
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

#Quotation Create API
@api_view(['POST'])
def createServiceQuotation(request):
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
        U_OPPRNM = request.data['U_OPPRNM']
        U_QUOTNM = request.data['U_QUOTNM']
        U_PREQUOTATION = request.data['U_PREQUOTATION']
        U_PREQTNM = request.data['U_PREQTNM']
        U_LEADID = request.data['U_LEADID']
        U_LEADNM = request.data['U_LEADNM']        
        PaymentGroupCode = request.data['PaymentGroupCode']
        BPLID = request.data['BPLID']
        U_Term_Condition    = request.data['U_Term_Condition']
        U_TermInterestRate  = request.data['U_TermInterestRate']
        U_TermPaymentTerm   = request.data['U_TermPaymentTerm']
        U_TermDueDate   = request.data['U_TermDueDate']
        CreateDate = request.data['CreateDate']
        CreateTime = request.data['CreateTime']
        UpdateDate = request.data['UpdateDate']
        UpdateTime = request.data['UpdateTime']

        PoNo   = request.data['PoNo']
        PoDate = request.data['PoDate']
        PoAmt  = request.data['PoAmt']
        PRID   = request.data['PRID']

        # ReferenceItemCode = request.data['ReferenceItem']

        ShippingAndHandling  = request.data['ShippingAndHandling']
        TermsAndConditions   = request.data['TermsAndConditions']
        
        lines = request.data['DocumentLines']

        DocTotal=0
        for line in lines:
            DocTotal = float(DocTotal) + float(line['Quantity']) * float(line['UnitPrice'])
        print(DocTotal)

        model=Quotation(TaxDate = TaxDate, DocDueDate = DocDueDate, ContactPersonCode = ContactPersonCode, DiscountPercent = DiscountPercent, DocDate = DocDate, CardCode = CardCode, CardName = CardName, Comments = Comments, SalesPersonCode = SalesPersonCode, DocumentStatus="bost_Open", CancelStatus="csNo", DocTotal = DocTotal, U_OPPID=U_OPPID, U_OPPRNM=U_OPPRNM, U_QUOTNM=U_QUOTNM, U_PREQUOTATION=U_PREQUOTATION, U_PREQTNM=U_PREQTNM, U_FAV='N', CreateDate = CreateDate, CreateTime = CreateTime, UpdateDate = UpdateDate, UpdateTime = UpdateTime, PaymentGroupCode=PaymentGroupCode, BPLID=BPLID, U_Term_Condition=U_Term_Condition, U_TermInterestRate=U_TermInterestRate, U_TermPaymentTerm=U_TermPaymentTerm, U_TermDueDate=U_TermDueDate, U_LEADID=U_LEADID, U_LEADNM=U_LEADNM, PoNo = PoNo, PoAmt = PoAmt, PoDate = PoDate, PRID = PRID, ShippingAndHandling = ShippingAndHandling,TermsAndConditions = TermsAndConditions)
        
        model.save()

        qt = Quotation.objects.latest('id')
        #for stop SAP add DocEntry
        model.DocEntry = qt.id
        model.save()
        
        addr = request.data['AddressExtension']
        
        model_add = AddressExtension(QuotationID = qt.id, BillToBuilding = addr['BillToBuilding'], ShipToState = addr['ShipToState'], BillToCity = addr['BillToCity'], ShipToCountry = addr['ShipToCountry'], BillToZipCode = addr['BillToZipCode'], ShipToStreet = addr['ShipToStreet'], BillToState = addr['BillToState'], ShipToZipCode = addr['ShipToZipCode'], BillToStreet = addr['BillToStreet'], ShipToBuilding = addr['ShipToBuilding'], ShipToCity = addr['ShipToCity'], BillToCountry = addr['BillToCountry'], U_SCOUNTRY = addr['U_SCOUNTRY'], U_SSTATE = addr['U_SSTATE'], U_SHPTYPB = addr['U_SHPTYPB'], U_BSTATE = addr['U_BSTATE'], U_BCOUNTRY = addr['U_BCOUNTRY'], U_SHPTYPS = addr['U_SHPTYPS'])
        
        model_add.save()
        
        LineNum = 0
        #TaxCode = line['TaxCode'], 
        for line in lines:
                
            model_lines = DocumentLines(LineNum = LineNum, QuotationID = qt.id, Quantity = line['Quantity'], UnitPrice = line['UnitPrice'], DiscountPercent = line['DiscountPercent'], ItemCode = line['ItemCode'], ItemDescription = line['ItemDescription'], U_FGITEM = line['U_FGITEM'], CostingCode2 = line['CostingCode2'], ProjectCode = line['ProjectCode'], FreeText = line['FreeText'], Frequency = line['Frequency'], StartDate = line['StartDate'], EndDate = line['EndDate'], ReferenceItem = line['ReferenceItem'])
            model_lines.save()
            LineNum=LineNum+1
        
        
        return Response({"message":"successful","status":200,"data":[{"qt_Id":qt.id, "DocEntry":qt.id}]})
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
        sapdb = settings.SAPSESSION("api")
        
        # res = requests.post(sapdb['sapurl']+'/Quotations', data=json.dumps(qt_data), headers={'Authorization': "Bearer "+sapdb['SessionId']+""}, verify=False)
        # live = json.loads(res.text)
        res = settings.CALLAPI('post', '/Quotations', 'api', qt_data)
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

                if DocumentLines.objects.filter(QuotationID = fetchid, LineNum = LineNum).exists():
                    DocumentLines.objects.filter(QuotationID = fetchid, LineNum = LineNum).update(TaxCode = TaxCode, TaxRate = TaxRate)

                print('------ SAP docline update--------')
                # print('data', LineNum,TaxCode, TaxRate)
                # print('data', TaxCode, TaxRate)
            
            model = Quotation.objects.get(pk = fetchid)
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
            Quotation.objects.filter(id=qt.id).delete()
            allline = DocumentLines.objects.filter(QuotationID=qt.id)
            for dcline in allline:
                dcline.delete()
                
            alladd = AddressExtension.objects.filter(QuotationID=qt.id)
            for ad in alladd:
                ad.delete()
            return Response({"message":SAP_MSG,"SAP_error":SAP_MSG, "status":202,"data":[]})
    except Exception as e:
        return Response({"message":str(e), "status":202,"data":[]})


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@api_view(["POST"])
def all_filter_for_service(request):
    try: 
        SalesPersonID = request.data['SalesPersonCode']  
        if Employee.objects.filter(SalesEmployeeCode=SalesPersonID).exists():
            
            SalesPersonID = EmpView.GetTeam(SalesPersonID,"Operation")            
            
            quot_obj = Quotation.objects.filter(SalesPersonCode__in=SalesPersonID).order_by("-id")
            allqt = QuotationShow2(quot_obj)
                
            return Response({"message": "Success","status": 200,"data":allqt})
        else:
            return Response({"message": "Unsuccess","status": 201,"data":[{"error":"SalesPersonCode invalid"}]})
    except Exception as e:
            return Response({"message": str(e), "status": 201, "data":[]})

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def QuotationShow2(quot_obj):
    allqt = []
    for qt in quot_obj:
    
        qtobj = Quotation.objects.get(pk=qt.id)
        
        qt_json = QuotationSerializer(qtobj, many=False)
        
        quot = json.loads(json.dumps(qt_json.data))
        
        if AddressExtension.objects.filter(QuotationID=qt.id).exists():
            qtaddr = AddressExtension.objects.filter(QuotationID=qt.id)
            qtaddr_json = AddressExtensionSerializer(qtaddr, many=True)
            quot["AddressExtension"]= qtaddr_json.data[0]
        else:
            quot["AddressExtension"]= {"id":"","QuotationID":"","BillToBuilding":"","ShipToState":"","BillToCity":"","ShipToCountry":"","BillToZipCode":"","ShipToStreet":"","BillToState":"","ShipToZipCode":"","BillToStreet":"","ShipToBuilding":"","ShipToCity":"","BillToCountry":"","U_SCOUNTRY":"","U_SSTATE":"","U_SHPTYPB":"","U_BSTATE":"","U_BCOUNTRY":"","U_SHPTYPS":""}

        lines = DocumentLines.objects.filter(QuotationID=qt.id)
        allLines = []
        for line in lines:
            # referenceItemid = line.ReferenceItem
            lineObj = DocumentLinesSerializer(line)
            linejson = json.loads(json.dumps(lineObj.data))
            if str(line.ProjectCode) != "" and Category.objects.filter(Number = line.ProjectCode).exists():
                cateObj = Category.objects.get(Number = line.ProjectCode)
                linejson['CategoryName'] = cateObj.GroupName
                linejson['IsService'] = cateObj.IsService
            else:
                linejson['CategoryName'] = ""
                linejson['IsService'] = ""
                
            # if referenceItemid != "":
            #     tempobj = DocumentLines.objects.filter(QuotationID = qt.id, ItemCode = referenceItemid)
            #     tempjson = DocumentLinesSerializer(tempobj, many=True)
            #     linejson['ReferenceItem'] = tempjson.data
            # else:
            #     linejson['ReferenceItem'] = []

            allLines.append(linejson)

        quot["DocumentLines"]= allLines

        cont = BPEmployee.objects.filter(InternalCode=qt.ContactPersonCode).values("InternalCode","FirstName")
        cont_json = BPEmployeeSerializer(cont, many=True)
        cont_all = json.loads(json.dumps(cont_json.data))
        print(cont_all)
        if len(cont) > 0:
            ContactPerson = cont_json.data
            print(ContactPerson)
        else:
            ContactPerson = []
            print(ContactPerson)

        sobj = Employee.objects.filter(SalesEmployeeCode=qt.SalesPersonCode)
        sobj_json = EmployeeSerializer(sobj, many=True)
        sobj_all = json.loads(json.dumps(sobj_json.data))
        # SalesPerson = sobj_json.data

        quot["ContactPersonCode"]= ContactPerson
        quot["SalesPersonCode"]= sobj_all
        
        if qt.CardCode != "":
            if BusinessPartner.objects.filter(CardCode = qt.CardCode).exists():
                bpemail_dls = BusinessPartner.objects.filter(CardCode = qt.CardCode).values_list('EmailAddress',flat=True)
                quot['BPEmail'] = bpemail_dls[0]
            else:
                quot['BPEmail'] = []
        else:
            quot['BPEmail'] = []
        
        allqt.append(quot)
    return allqt
