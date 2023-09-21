from django.conf import settings
from django.shortcuts import render, redirect  
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from BusinessPartner.models import BusinessPartner
from Order.models import Order
from Quotation.models import Quotation
from Quotation.views import QuotationShow
from global_fun import getAllReportingToIds, getAllReportingToIdsSubdep


from .models import *
from Employee.models import Employee

import requests, json

from rest_framework.decorators import api_view    
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import JSONParser

from pytz import timezone
from datetime import datetime as dt

date = dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d')
yearmonth = dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m')
time = dt.now(timezone("Asia/Kolkata")).strftime('%H:%M %p')


# Create your views here.  

#Invoice Create API
@api_view(['POST'])
def create(request):
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
    
    
    lines = request.data['DocumentLines']
    DocTotal=0
    for line in lines:
        DocTotal = float(DocTotal) + float(line['Quantity']) * float(line['UnitPrice'])
    print(DocTotal)

    model=Invoice(TaxDate = TaxDate, DocDueDate = DocDueDate, ContactPersonCode = ContactPersonCode, DiscountPercent = DiscountPercent, DocDate = DocDate, CardCode = CardCode, CardName = CardName, Comments = Comments, SalesPersonCode = SalesPersonCode, DocumentStatus="bost_Open", DocTotal = DocTotal, CreateDate = CreateDate, CreateTime = CreateTime, UpdateDate = UpdateDate, UpdateTime = UpdateTime, PaymentGroupCode=PaymentGroupCode, BPLID=BPLID,U_Term_Condition=U_Term_Condition)
    
    model.save()
    qt = Invoice.objects.latest('id')
    
    addr = request.data['AddressExtension']
    
    model_add = AddressExtension(InvoiceID = qt.id, BillToBuilding = addr['BillToBuilding'], ShipToState = addr['ShipToState'], BillToCity = addr['BillToCity'], ShipToCountry = addr['ShipToCountry'], BillToZipCode = addr['BillToZipCode'], ShipToStreet = addr['ShipToStreet'], BillToState = addr['BillToState'], ShipToZipCode = addr['ShipToZipCode'], BillToStreet = addr['BillToStreet'], ShipToBuilding = addr['ShipToBuilding'], ShipToCity = addr['ShipToCity'], BillToCountry = addr['BillToCountry'], U_SCOUNTRY = addr['U_SCOUNTRY'], U_SSTATE = addr['U_SSTATE'], U_SHPTYPB = addr['U_SHPTYPB'], U_BSTATE = addr['U_BSTATE'], U_BCOUNTRY = addr['U_BCOUNTRY'], U_SHPTYPS = addr['U_SHPTYPS'])
    
    model_add.save()

    LineNum = 0
    for line in lines:
        model_lines = DocumentLines(LineNum = LineNum, InvoiceID = qt.id, Quantity = line['Quantity'], UnitPrice = line['UnitPrice'], DiscountPercent = line['DiscountPercent'], ItemCode = line['ItemCode'], ItemDescription = line['ItemDescription'], TaxCode = line['TaxCode'], U_FGITEM = line['U_FGITEM'], CostingCode2 = line['CostingCode2'], ProjectCode = line['ProjectCode'], FreeText = line['FreeText'])
        model_lines.save()
        LineNum=LineNum+1
    r = requests.post(settings.BASEURL+'/Login', data=json.dumps(settings.SAPDB), verify=False)
    token = json.loads(r.text)['SessionId']
    print(token)
    
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

    res = requests.post(settings.BASEURL+'/Invoices', data=json.dumps(qt_data), cookies=r.cookies, verify=False)
    live = json.loads(res.text)
    
    fetchid = qt.id
    
    if "DocEntry" in live:
        print(live['DocEntry'])
        
        model = Invoice.objects.get(pk = fetchid)
        model.DocEntry = live['DocEntry']
        model.save()
        
        return Response({"message":"successful","status":200,"data":[{"qt_Id":qt.id, "DocEntry":live['DocEntry']}]})
    else:
        SAP_MSG = live['error']['message']['value']
        print(SAP_MSG)
        #Invoice.objects.get(pk=qt.id).delete()
        allline = DocumentLines.objects.filter(InvoiceID=qt.id)
        for dcline in allline:
            dcline.delete()
            
        alladd = AddressExtension.objects.filter(InvoiceID=qt.id)
        for ad in alladd:
            ad.delete()
        return Response({"message":SAP_MSG,"SAP_error":SAP_MSG, "status":202,"data":[]})

#Invoice Update API
@api_view(['POST'])
def update(request):
    fetchid = request.data['id']
    try:
        model = Invoice.objects.get(pk = fetchid)

        model.TaxDate = request.data['TaxDate']
        model.DocDate = request.data['DocDate']
        model.DocDueDate = request.data['DocDueDate']
        
        model.ContactPersonCode = request.data['ContactPersonCode']
        model.DiscountPercent = request.data['DiscountPercent']
        model.Comments = request.data['Comments']
        model.SalesPersonCode = request.data['SalesPersonCode']
        
        model.PaymentGroupCode = request.data['PaymentGroupCode']
        model.U_Term_Condition = request.data['U_Term_Condition']
        model.BPLID = request.data['BPLID']
        
        model.UpdateDate = request.data['UpdateDate']
        model.UpdateTime = request.data['UpdateTime']

        model.save()
        
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
        for line in lines:
            if "id" in line:
                model_line = DocumentLines.objects.get(pk = line['id'])
                model_line.Quantity=line['Quantity']
                model_line.UnitPrice=line['UnitPrice']
                model_line.DiscountPercent=line['DiscountPercent']
                model_line.ItemCode=line['ItemCode']
                model_line.ItemDescription=line['ItemDescription']
                model_line.TaxCode=line['TaxCode']
                
                model_line.ProjectCode=line['ProjectCode']
                model_line.U_FGITEM=line['U_FGITEM']
                model_line.CostingCode2=line['CostingCode2']
                model_line.FreeText=line['FreeText']               
                model_line.save()
            else:
                lastline = DocumentLines.objects.filter(InvoiceID = fetchid).order_by('-LineNum')[:1]
                NewLine = int(lastline[0].LineNum) + 1
                model_lines = DocumentLines(InvoiceID = fetchid, LineNum=NewLine, Quantity = line['Quantity'], UnitPrice = line['UnitPrice'], DiscountPercent = line['DiscountPercent'], ItemCode = line['ItemCode'], ItemDescription = line['ItemDescription'], TaxCode = line['TaxCode'], U_FGITEM = line['U_FGITEM'], CostingCode2 = line['CostingCode2'], ProjectCode = line['ProjectCode'], FreeText = line['FreeText'])
                model_lines.save()
            
            

        
        r = requests.post(settings.BASEURL+'/Login', data=json.dumps(settings.SAPDB), verify=False)
        token = json.loads(r.text)['SessionId']
        print(token)
        
        qt_data = {
            "TaxDate": request.data['TaxDate'],
            "DocDueDate": request.data['DocDueDate'],
            "ContactPersonCode": request.data['ContactPersonCode'],
            "DiscountPercent": request.data['DiscountPercent'],
            "DocDate": request.data['DocDate'],
            "Comments": request.data['Comments'],
            "SalesPersonCode": request.data['SalesPersonCode'],
            "BPL_IDAssignedToInvoice": request.data['BPLID'],
            "PaymentGroupCode":request.data['PaymentGroupCode'],
            "U_Term_Condition":request.data['U_Term_Condition'],
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

    
        print("http://122.160.67.60:50001/b1s/v1/Invoices('"+model.DocEntry+"')");
        res = requests.patch("http://122.160.67.60:50001/b1s/v1/Invoices("+model.DocEntry+")", data=json.dumps(qt_data), cookies=r.cookies, verify=False)
        print(res.content)

        if len(res.content) !=0 :
            res1 = json.loads(res.content)
            SAP_MSG = res1['error']['message']['value']
            return Response({"message":"Partely successful","status":202,"SAP_error":SAP_MSG, "data":[request.data]})
        else:
            return Response({"message":"successful","status":200, "data":[json.loads(json.dumps(request.data))]})
    except Exception as e:
        return Response({"message":"Not Update","status":201,"data":[{"Error":str(e)}]})


def InvoiceShow(Invoices_obj):
    allqt = []
    for qt in Invoices_obj:

        # invoice
        invoice_obj = InvoiceSerializer(qt, many=False)
        finalInvoice = json.loads(json.dumps(invoice_obj.data))

        # invoice order
        qtaddr = AddressExtension.objects.filter(InvoiceID=qt.id)
        qtaddr_json = AddressExtensionSerializer(qtaddr, many=True)
        jss_ = json.loads(json.dumps(qtaddr_json.data))
        for j in jss_:
            # jss0=j
            finalInvoice['AddressExtension'] = j
        
        # invoice document line
        lines = DocumentLines.objects.filter(InvoiceID=qt.id)
        lines_json = DocumentLinesSerializer(lines, many=True)
        finalInvoice['DocumentLines'] = json.loads(json.dumps(lines_json.data))
        allqt.append(finalInvoice)
        
    return allqt

@api_view(["POST"])
def delivery(request):
    json_data = request.data    
    if "SalesEmployeeCode" in json_data:
        print("yes")
        
        if json_data['SalesEmployeeCode']!="":
            SalesEmployeeCode = json_data['SalesEmployeeCode']
            
            emp_obj =  Employee.objects.get(SalesEmployeeCode=SalesEmployeeCode)
            if emp_obj.role == 'admin' or emp_obj.role == 'ceo':
                emps = Employee.objects.filter(SalesEmployeeCode__gt=0)
                SalesEmployeeCode=[]
                for emp in emps:
                    SalesEmployeeCode.append(emp.SalesEmployeeCode)                    
            elif emp_obj.role == 'manager':
                emps = Employee.objects.filter(reportingTo=SalesEmployeeCode)#.values('id', 'SalesEmployeeCode')
                SalesEmployeeCode=[SalesEmployeeCode]
                for emp in emps:
                    SalesEmployeeCode.append(emp.SalesEmployeeCode)
            else:
                SalesEmployeeCode=[SalesEmployeeCode]
            print(SalesEmployeeCode)
            if json_data['Type'] =="over":
                ord = Invoice.objects.filter(SalesPersonCode__in=SalesEmployeeCode, DocumentStatus="bost_Open", DocDueDate__lt=date)
                allord = InvoiceShow(ord)
                #print(allord)
            elif json_data['Type'] =="open":
                ord = Invoice.objects.filter(SalesPersonCode__in=SalesEmployeeCode, DocumentStatus="bost_Open", DocDueDate__gte=date)
                allord = InvoiceShow(ord)
                #print(allord)
            else:
                ord = Invoice.objects.filter(SalesPersonCode__in=SalesEmployeeCode, DocumentStatus="bost_Close")
                allord = InvoiceShow(ord)
            return Response({"message": "Success","status": 200,"data":allord})
        else:
            return Response({"message": "Unsuccess","status": 201,"data":[{"error":"SalesEmployeeCode?"}]})
    else:
        return Response({"message": "Unsuccess","status": 201,"data":[{"error":"SalesEmployeeCode?"}]})
	
	
#Quotation All API
@api_view(["POST"])
def all_filter(request):
    json_data = request.data
    if "SalesPersonCode" in json_data:
        print("yes")        
        if json_data['SalesPersonCode']!="":
            SalesPersonID = json_data['SalesPersonCode']            
            emp_obj = Employee.objects.get(SalesEmployeeCode=SalesPersonID)            
            if emp_obj.role == 'manager':
                emps = Employee.objects.filter(reportingTo=SalesPersonID)#.values('id', 'SalesEmployeeCode')
                SalesPersonID=[SalesPersonID]
                for emp in emps:
                    SalesPersonID.append(emp.SalesEmployeeCode)                
            elif emp_obj.role == 'admin' or emp_obj.role == 'ceo':
                emps = Employee.objects.filter(SalesEmployeeCode__gt=0)
                SalesPersonID=[]
                for emp in emps:
                    SalesPersonID.append(emp.SalesEmployeeCode)
            else:
                SalesPersonID = json_data['SalesPersonCode']
            
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
                    quot_obj = Invoice.objects.filter(SalesPersonCode__in=SalesPersonID).order_by("-id")
                    allqt = InvoiceShow(quot_obj)                        
                    return Response({"message": "Success","status": 200,"data":allqt})
        else:
            return Response({"message": "Unsuccess","status": 201,"data":[{"error":"SalesPersonCode?"}]})
    else:
        print("no")
        return Response({"message": "Unsuccess","status": 201,"data":[{"error":"SalesPersonCode?"}]})


#Invoice All API
@api_view(["GET"])
def all(request):
    Invoices_obj = Invoice.objects.all().order_by("-id")
    allqt = InvoiceShow(Invoices_obj)
    return Response({"message": "Success","status": 200,"data":allqt})

#Invoice One API
@api_view(["POST"])
def one(request):
    id=request.data['id']
    
    Invoices_obj = Invoice.objects.filter(id=id)
    
    allqt = InvoiceShow(Invoices_obj)
    return Response({"message": "Success","status": 200,"data":allqt})


#Invoice delete
@api_view(['POST'])
def delete(request):
    fetchid=request.data['id']
    try:
        emp=Invoice.objects.get(pk=fetchid)
        SalesInvoiceCode = emp.SalesInvoiceCode        
        fetchdata=Invoice.objects.filter(pk=fetchid).delete()
        try:
            r = requests.post(settings.BASEURL+'/Login', data=json.dumps(settings.SAPDB), verify=False)
            token = json.loads(r.text)['SessionId']
            print(token)
            res = requests.delete(settings.BASEURL+'/SalesPersons('+SalesInvoiceCode+')', cookies=r.cookies, verify=False)
            return Response({"message":"successful","status":"200","data":[]})
        except:
            return Response({"message":"successful","status":"200","data":[]})        
    except:
         return Response({"message":"Id wrong","status":"201","data":[]})

################ CODE ADDED BY DIPANSHU FROM STANDALONE SUPPORT #################

#Invoice All API
@api_view(["POST"])
def all_filter_page(request):
    json_data = request.data
    SearchText = json_data['SearchText']
    page = settings.PAGE(request.data)
    print(page)
    
    if "SalesPersonCode" in json_data:
        print("yes")
        
        if json_data['SalesPersonCode']!="":
            SalesPersonID = json_data['SalesPersonCode']
            
            SalesPersonID = getAllReportingToIdsSubdep(SalesPersonID,"Sales")                                    
            print('SalesPersonID')
            print(SalesPersonID)
            
            #objs = Invoice.objects.filter(SalesPersonCode__in=SalesPersonID).order_by("-id")
            objs = Invoice.objects.filter(Q(CardName__icontains=SearchText, SalesPersonCode__in=SalesPersonID)|Q(DocEntry__icontains=SearchText, SalesPersonCode__in=SalesPersonID)|Q(CreationDate__icontains=SearchText, SalesPersonCode__in=SalesPersonID))
            
            objs = settings.FILTER(json_data['field'], objs, "invoice")    
            count = objs.count()
            objs = objs[page['startWith']:page['endWith']]
            
            allqt = InvoiceShowMini(objs)
                
            return Response({"message": "Success","status": 200,"data":allqt, "meta":{"count":count}})
            
        else:
            return Response({"message": "Unsuccess","status": 201,"data":[{"error":"SalesPersonCode?"}]})
    else:
        print("no")
        return Response({"message": "Unsuccess","status": 201,"data":[{"error":"SalesPersonCode?"}]})


@api_view(['POST'])
def one_receipt(request):
    try:
        ReceiptId=request.data['ReceiptId']
        if IncomingPayments.objects.filter(pk=ReceiptId).exists():
            paymentObj = IncomingPayments.objects.filter(pk=ReceiptId)
            result = showIncomingPayments(paymentObj)
            return Response({"message":"successful","status":"200","data":result})
        else:
            return Response({"message":"Invalid Receipt Id?","status":"201","data":[]})      
    except Exception as e:
        return Response({"message":str(e),"status":"201","data":[]})
  
@api_view(['POST'])
def bp_wise_receipt(request):
    try:
        CardCode = request.data['CardCode']
        FromDate = request.data['FromDate']
        ToDate = request.data['ToDate']
        if BusinessPartner.objects.filter(CardCode = CardCode).exists():
            paymentObj = IncomingPayments.objects.filter(CardCode = CardCode)
            result = showIncomingPayments(paymentObj)
            return Response({"message":"successful","status":"200","data":result})
        else:
            return Response({"message":"Invalid BP Code?","status":"201","data":[]})      
    except Exception as e:
        return Response({"message":str(e),"status":"201","data":[]})  
    
@api_view(['POST'])
def incoming_payments(request):
    try:
        InvoiceId=request.data['id']
        FromDate = request.data['FromDate']
        ToDate = request.data['ToDate']
        if Invoice.objects.filter(pk=InvoiceId).exists():
            invObj = Invoice.objects.filter(pk=InvoiceId).first()
            incomingPayObj = []
            result = []
            if str(FromDate) !="":
                
                incomingPayIds = IncomingPaymentInvoices.objects.filter(InvoiceDocEntry = invObj.DocEntry, DocDate__gte = FromDate, DocDate__lte = ToDate).values_list('IncomingPaymentsId', flat=True)
                incomingPayObj = IncomingPayments.objects.filter(pk__in = incomingPayIds)
                result = showIncomingPayments(incomingPayObj)
            else:
                incomingPayIds = IncomingPaymentInvoices.objects.filter(InvoiceDocEntry = invObj.DocEntry).values_list('IncomingPaymentsId', flat=True)
                incomingPayObj = IncomingPayments.objects.filter(pk__in = incomingPayIds)
                result = showIncomingPayments(incomingPayObj)
                
            # incomingPayJson = IncomingPaymentsSerializer(incomingPayObj, many=True)
            return Response({"message":"successful","status":"200","data":result})
        else:
            return Response({"message":"Invalid Invoice Id?","status":"201","data":[]})      
    except Exception as e:
        return Response({"message":str(e),"status":"201","data":[]})
    

@api_view(['POST'])
def all_incoming_payments(request):
    try:
        SalesEmployeeCode = request.data['SalesEmployeeCode']
        FromDate = request.data['FromDate']
        ToDate = request.data['ToDate']
        allEmp = getAllReportingToIds(SalesEmployeeCode)
        docEntrys = list(Invoice.objects.filter(SalesPersonCode__in = allEmp).values_list('DocEntry', flat=True))
        
        totalSalesList = 0
        allPaymentsList = 0

        if str(FromDate) != "":
            totalSalesList = list(Invoice.objects.filter(SalesPersonCode__in = allEmp, DocDate__gte = FromDate, DocDate__lte = ToDate).values_list('DocTotal', flat=True))
            allPaymentsList = IncomingPaymentInvoices.objects.filter(InvoiceDocEntry__in = docEntrys, DocDate__gte = FromDate, DocDate__lte = ToDate).values_list('SumApplied', flat=True)
            
        else:
            totalSalesList = list(Invoice.objects.filter(SalesPersonCode__in = allEmp).values_list('DocTotal', flat=True))
            allPaymentsList = IncomingPaymentInvoices.objects.filter(InvoiceDocEntry__in = docEntrys).values_list('SumApplied', flat=True)
            
        totalSales = 0
        allPayment = 0

        for item in totalSalesList:
            totalSales += float(item)

        for item in allPaymentsList:
            allPayment += float(item)

        # incomingPayJson = IncomallPaymentingPaymentsSerializer(incomingPayObj, many=True)
        context = {
            "TotalSales": totalSales,
            "TotalReceivePayment": allPayment,
            "DifferenceAmount": float(float(totalSales) - float(allPayment))
        }
        return Response({"message":"successful","status":"200","data":[context]})
        # else:
        #     return Response({"message":"Invalid Invoice Id?","status":"201","data":[]})      
    except Exception as e:
        return Response({"message":str(e),"status":"201","data":[]})

@api_view(['POST'])
def credit_notes(request):
    try:
        InvoiceId=request.data['id']
        FromDate = request.data['FromDate']
        ToDate = request.data['ToDate']
        if Invoice.objects.filter(pk=InvoiceId).exists():
            invObj = Invoice.objects.filter(pk=InvoiceId).first()
            incomingPayObj = []
            if str(FromDate) != "":
                incomingPayObj = CreditNotes.objects.filter(InvoiceDocEntry = invObj.DocEntry, DocDate__gte = FromDate, DocDate__lte = ToDate)
            else:
                incomingPayObj = CreditNotes.objects.filter(InvoiceDocEntry = invObj.DocEntry)

            incomingPayJson = CreditNotesSerializer(incomingPayObj, many=True)
            return Response({"message":"successful","status":"200","data":incomingPayJson.data})
        else:
            return Response({"message":"Invalid Invoice Id?","status":"201","data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":"201","data":[]})

@api_view(['POST'])
def payment_collection_dashboard(request):
    try:
        # SalesType = request.data['Type']
        FromDate = request.data['FromDate']
        ToDate = request.data['ToDate']
        cardCodeList = list(Invoice.objects.all().values_list('CardCode', flat=True).distinct())
        print("<><><><>< cardCodeList", cardCodeList)
        bpObjs = BusinessPartner.objects.filter(CardCode__in = cardCodeList).values("id", "CardCode", "CardName")
        dataContext = []
        docEntrys = []
        totalSales = 0
        allPaymentsList = 0
        for bpobj in bpObjs:
            orderList = []
            if str(FromDate) != "":
                orderList = Invoice.objects.filter(CardCode = bpobj['CardCode'], DocDate__gte = FromDate, DocDate__lte = ToDate).values("id","DocTotal", "CreateDate", "VatSum", "DocEntry")
            else:
                orderList = Invoice.objects.filter(CardCode = bpobj['CardCode']).values("id","DocTotal", "CreateDate", "VatSum", "DocEntry")
            
            totalSalesByBp = 0 
            print("Length of objects orderList: ", len(orderList))
            if len(orderList) != 0:
                print("Query", orderList.query)
                for order in orderList:
                    print("in invoice list")
                    docEntry = order['DocEntry']
                    print(docEntry)
                    docEntrys.append(docEntry)
                    DocTotal = order['DocTotal']
                    # VatSum = order['VatSum']
                    totalSalesByBp = totalSalesByBp + float(DocTotal)
                
                print("docEntry", docEntrys)
                if str(FromDate) != "":
                    # allPayments = IncomingPayments.objects.filter(InvoiceDocEntry__in = docEntrys, DocDate__gte = FromDate, DocDate__lte = ToDate).values_list('TransferSum', flat=True)
                    allPayments = IncomingPaymentInvoices.objects.filter(InvoiceDocEntry__in = docEntrys, DocDate__gte = FromDate, DocDate__lte = ToDate).values_list('SumApplied', flat=True)
                else:
                    # allPayments = IncomingPayments.objects.filter(InvoiceDocEntry__in = docEntrys).values_list('TransferSum', flat=True)
                    allPayments = IncomingPaymentInvoices.objects.filter(InvoiceDocEntry__in = docEntrys).values_list('SumApplied', flat=True)

                
                print("allPayments: ",allPayments)

                allPayment = 0
                for item in allPayments:
                    allPayment += float(item)
                
                allPaymentsList = allPaymentsList + allPayment

                InvDifferenceAmount = round(float(float(totalSalesByBp) - float(allPaymentsList)), 2)

                bpData = {
                    "CardName": bpobj['CardName'],
                    "CardCode": bpobj['CardCode'],
                    "TotalSales": round(InvDifferenceAmount, 2)
                }
                dataContext.append(bpData)
                totalSales = float(totalSales) + float(totalSalesByBp)
            else:
                pass
                print('no invoices')

        TotalSales = totalSales
        TotalReceivePayment = round(allPaymentsList, 2)
        DifferenceAmount = round(float(float(TotalSales) - float(allPaymentsList)), 2)

        return Response({"message": "Success","status": 200, "data":dataContext, "TotalSales": TotalSales, "TotalReceivePayment": TotalReceivePayment, "DifferenceAmount": DifferenceAmount})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})

# bp list with total purchase
@api_view(['POST'])
def bp_payment_collection(request):
    try:
        CardCode = request.data['CardCode']
        # SalesType = request.data['Type'] # Gross/Net
        FromDate = request.data['FromDate']
        ToDate = request.data['ToDate']
        
        dataContext = []
        docEntrys = []
        totalSales = 0
        totalSalesByBp = 0
        allPaymentsList = 0

        if BusinessPartner.objects.filter(CardCode = CardCode).exists():
            orderList = []
            if str(FromDate) != "":
                orderList = Invoice.objects.filter(CardCode = CardCode, DocDate__gte = FromDate, DocDate__lte = ToDate).values("id","DocTotal", "CreateDate", "VatSum", "DocEntry")
            else:
                orderList = Invoice.objects.filter(CardCode = CardCode).values("id","DocTotal", "CreateDate", "VatSum", "DocEntry")
            
            print("Length of objects orderList: ", len(orderList))
            if len(orderList) != 0:
                for order in orderList:
                    docEntrys.append(order['DocEntry'])
                    DocTotal = order['DocTotal']

                    if str(FromDate) != "":
                        # allPayments = IncomingPayments.objects.filter(InvoiceDocEntry = order['DocEntry'], DocDate__gte = FromDate, DocDate__lte = ToDate).values_list('TransferSum', flat=True)
                        allPayments = IncomingPaymentInvoices.objects.filter(InvoiceDocEntry = order['DocEntry'], DocDate__gte = FromDate, DocDate__lte = ToDate).values_list('SumApplied', flat=True)
                    else:
                        # allPayments = IncomingPayments.objects.filter(InvoiceDocEntry = order['DocEntry']).values_list('TransferSum', flat=True)
                        allPayments = IncomingPaymentInvoices.objects.filter(InvoiceDocEntry = order['DocEntry']).values_list('SumApplied', flat=True)
                    
                    print("allPayments: ",allPayments)

                    allPayment = 0
                    for item in allPayments:
                        allPayment += float(item)
                    
                    allPaymentsList = allPaymentsList + allPayment

                    InvDifferenceAmount = round(float(float(DocTotal) - float(allPayment)), 2)

                    bpData = {
                        "OrderId": order['id'],
                        "OrderAmount": InvDifferenceAmount,
                        "CreateDate": order['CreateDate']
                    }                    
                    dataContext.append(bpData)
                    totalSalesByBp = totalSalesByBp + float(DocTotal)
            else:
                print('no invoice')
        else:
            return Response({"message": "Invalid CardCode","status": 201, "data":[], "TotalSales": 0})

        TotalSales = round(totalSalesByBp, 2)
        TotalReceivePayment = round(allPaymentsList, 2)
        DifferenceAmount = round(float(float(totalSalesByBp) - float(allPaymentsList)), 2)

        return Response({"message": "Success","status": 200, "data":dataContext, "TotalSales": TotalSales, "TotalReceivePayment": TotalReceivePayment, "DifferenceAmount": DifferenceAmount})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})

# bp list with total purchase
@api_view(['POST'])
def credit_note_dashboard(request):
    try:
        # SalesType = request.data['Type']
        FromDate = request.data['FromDate']
        ToDate = request.data['ToDate']
        cardCodeList = list(Invoice.objects.all().values_list('CardCode', flat=True).distinct())
        print("<><><><>< cardCodeList", cardCodeList)
        bpObjs = BusinessPartner.objects.filter(CardCode__in = cardCodeList).values("id", "CardCode", "CardName")
        dataContext = []
        docEntrys = []
        totalSales = 0
        allPaymentsList = 0
        for bpobj in bpObjs:
            orderList = []
            if str(FromDate) != "":
                orderList = Invoice.objects.filter(CardCode = bpobj['CardCode'], DocDate__gte = FromDate, DocDate__lte = ToDate).values("id","DocTotal", "CreateDate", "VatSum", "DocEntry")
            else:
                orderList = Invoice.objects.filter(CardCode = bpobj['CardCode']).values("id","DocTotal", "CreateDate", "VatSum", "DocEntry")
            
            totalSalesByBp = 0 
            print("Length of objects orderList: ", len(orderList))
            if len(orderList) != 0:
                # print("Query", orderList.query)
                for order in orderList:
                    print("in invoice list")
                    docEntry = order['DocEntry']
                    docEntrys.append(docEntry)
                    DocTotal = order['DocTotal']
                    totalSalesByBp = totalSalesByBp + float(DocTotal)
                
                print("docEntry", docEntrys)
                if str(FromDate) != "":
                    allPayments = CreditNotes.objects.filter(InvoiceDocEntry__in = docEntrys, DocDate__gte = FromDate, DocDate__lte = ToDate).values_list('DocTotal', flat=True)
                else:
                    allPayments = CreditNotes.objects.filter(InvoiceDocEntry__in = docEntrys).values_list('DocTotal', flat=True)

                print("allPayments: ",allPayments)

                allPayment = 0
                for item in allPayments:
                    allPayment += float(item)
                
                allPaymentsList = allPaymentsList + allPayment

                # InvDifferenceAmount = round(float(float(totalSalesByBp) - float(allPaymentsList)), 2)

                bpData = {
                    "CardName": bpobj['CardName'],
                    "CardCode": bpobj['CardCode'],
                    "TotalSales": round(allPayment, 2) # total 
                }
                dataContext.append(bpData)
                totalSales = float(totalSales) + float(totalSalesByBp)
            else:
                print('no invoices')


        TotalSales = totalSales
        TotalReceivePayment = round(allPaymentsList, 2)
        DifferenceAmount = round(float(float(TotalSales) - float(allPaymentsList)), 2)

        return Response({"message": "Success","status": 200, "data":dataContext, "TotalSales": TotalSales, "TotalReceivePayment": TotalReceivePayment, "DifferenceAmount": DifferenceAmount})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})

# bp list with total purchase
@api_view(['POST'])
def bp_credit_note(request):
    try:
        CardCode = request.data['CardCode']
        # SalesType = request.data['Type'] # Gross/Net
        FromDate = request.data['FromDate']
        ToDate = request.data['ToDate']
        
        dataContext = []
        docEntrys = []
        totalSalesByBp = 0
        allPaymentsList = 0

        if BusinessPartner.objects.filter(CardCode = CardCode).exists():
            orderList = []
            if str(FromDate) != "":
                orderList = Invoice.objects.filter(CardCode = CardCode, DocDate__gte = FromDate, DocDate__lte = ToDate).values("id","DocTotal", "CreateDate", "VatSum", "DocEntry")
            else:
                orderList = Invoice.objects.filter(CardCode = CardCode).values("id","DocTotal", "CreateDate", "VatSum", "DocEntry")
            
            print("Length of objects orderList: ", len(orderList))
            if len(orderList) != 0:
                for order in orderList:
                    docEntrys.append(order['DocEntry'])
                    DocTotal = order['DocTotal']
                    if str(FromDate) != "":
                        allPayments = CreditNotes.objects.filter(InvoiceDocEntry__in = docEntrys, DocDate__gte = FromDate, DocDate__lte = ToDate).values_list('DocTotal', flat=True)
                    else:
                        allPayments = CreditNotes.objects.filter(InvoiceDocEntry__in = docEntrys).values_list('DocTotal', flat=True)
                    
                    print("allPayments: ",allPayments)

                    allPayment = 0
                    for item in allPayments:
                        allPayment += float(item)
                    
                    allPaymentsList = allPaymentsList + allPayment

                    # InvDifferenceAmount = round(float(float(DocTotal) - float(allPayment)), 2)

                    bpData = {
                        "OrderId": order['id'],
                        "OrderAmount": allPayment,
                        "CreateDate": order['CreateDate']
                    }                    
                    dataContext.append(bpData)
                    totalSalesByBp = totalSalesByBp + float(DocTotal)
            else:
                print('no invoice')
        else:
            return Response({"message": "Invalid CardCode","status": 201, "data":[], "TotalSales": 0})

        TotalSales = round(totalSalesByBp, 2)
        TotalReceivePayment = round(allPaymentsList, 2)
        DifferenceAmount = round(float(float(totalSalesByBp) - float(allPaymentsList)), 2)

        return Response({"message": "Success","status": 200, "data":dataContext, "TotalSales": TotalSales, "TotalReceivePayment": TotalReceivePayment, "DifferenceAmount": DifferenceAmount})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})

@api_view(['GET'])  
def pending_payment_collection(request):
        import datetime
        all_collection = []
        if Invoice.objects.filter(DocumentStatus = 'bost_Open').exists():
            inv_obj = Invoice.objects.filter(DocumentStatus = 'bost_Open')
            for obj in inv_obj:
                InvoiceEntry = obj.DocEntry
                if DocumentLines.objects.filter(InvoiceID = obj.id).exists():

                    itemObj = DocumentLines.objects.filter(InvoiceID = obj.id).values('BaseEntry').first()

                    OrderEntry = itemObj['BaseEntry']
                    CardName = obj.CardName
                    totalOrderAmount = 0
                    if Order.objects.filter(DocEntry = OrderEntry).exists():
                        ord_obj = Order.objects.filter(DocEntry = OrderEntry).first()
                        totalOrderAmount = ord_obj.DocTotal
                        
                    totalInvoiceAmount = float(obj.DocTotal)
                    DocDueDate = datetime.datetime.strptime(obj.DocDueDate, "%Y-%m-%d")
                    CreateDate = datetime.datetime.strptime(obj.CreateDate, "%Y-%m-%d")
                    TodayDate = datetime.datetime.strptime(date, "%Y-%m-%d")

                    PaymentStatus = "Due"
                    DiscountAmount = 0
                    DiscountPercentage = 0
                    dateDifference = (TodayDate - CreateDate).days
                    print(dateDifference)
                    if dateDifference <= 10:
                        DiscountAmount = (totalInvoiceAmount * 0.04)
                        DiscountPercentage = 4
                    elif (dateDifference >= 11) and (dateDifference <= 20):
                        DiscountAmount = (totalInvoiceAmount * 0.03)
                        DiscountPercentage = 3
                    elif (dateDifference >= 21) and (dateDifference <= 30):
                        DiscountAmount = (totalInvoiceAmount * 0.02)
                        DiscountPercentage = 2
                    elif (dateDifference >= 31) and (dateDifference <= 40):
                        DiscountAmount = (totalInvoiceAmount * 0.01)
                        DiscountPercentage = 1
                    elif TodayDate < DocDueDate:
                        PaymentStatus = "Due"
                    else:
                        PaymentStatus = "Overdue"
                        
                    PaymentAmount = 0
                    PendingAmount = 0
                    if IncomingPaymentInvoices.objects.filter(InvoiceDocEntry = InvoiceEntry).exists():
                        objs = IncomingPaymentInvoices.objects.filter(InvoiceDocEntry = InvoiceEntry)
                        for obj in objs:
                            PaymentAmount = PaymentAmount + float(obj.SumApplied)

                    PendingAmount = totalInvoiceAmount - PaymentAmount
                    contaxt = {
                        "InvoiceNo": InvoiceEntry,
                        "OrderNo": OrderEntry, 
                        "CustomerName": CardName,
                        "OrderAmount": totalOrderAmount, 
                        "InvoiceAmount": totalInvoiceAmount,
                        "PaymentAmount": PaymentAmount,
                        "PendingAmount": PendingAmount,
                        "PaymentDueDate": DocDueDate.date(),
                        "CreateDate": CreateDate.date(),
                        "DiscountAmount": DiscountAmount,
                        "DiscountPercentage": DiscountPercentage,
                        "PaymentStatus": PaymentStatus
                    }
                    all_collection.append(contaxt)
                    
        return Response({"message":"successful","status":"200","data":all_collection})
   
@api_view(['POST'])
def bp_wise_sold_items(request):
    try:
        contaxt = {}
        CardCode = request.data['CardCode']
        FromDate = request.data['FromDate']
        ToDate = request.data['ToDate']

        if BusinessPartner.objects.filter(CardCode = CardCode).exists():
            invoiceIDs = []
            if str(FromDate) != "":
                invoiceIDs = Invoice.objects.filter(CardCode = CardCode, DocDate__gte = FromDate, DocDate__lte = ToDate).values_list('id', flat=True)
            else:
                invoiceIDs = Invoice.objects.filter(CardCode = CardCode).values_list('id', flat=True)
                
            itemCodes = DocumentLines.objects.filter(InvoiceID__in = invoiceIDs).values_list('ItemCode', flat=True).distinct()
            itemList = []
            for code in itemCodes:
                itms = DocumentLines.objects.filter(InvoiceID__in = invoiceIDs, ItemCode = code).order_by('id')
                ItemQuantity = 0
                InvoiceID = 0
                ItemOrderList = []
                LastSoldDate = ""
                for itm in itms:
                    ItemQuantity = ItemQuantity + int(itm.Quantity)
                    InvoiceID = itm.InvoiceID
                    createDate = Invoice.objects.filter(pk = InvoiceID).values_list('DocDate', flat=True).first()
                    itemOrder = {
                        "OrderId": InvoiceID,
                        "UnitPirce": itm.UnitPrice,
                        "SoldDate":str(createDate),
                        "TotalQty": ItemQuantity,
                    }
                    ItemOrderList.append(itemOrder)
                    LastSoldDate = createDate

                tempContaxt = {
                    "ItemName": itms[0].ItemDescription,
                    "ItemCode": itms[0].ItemCode,
                    "UnitPirce": itms[0].UnitPrice,
                    "LastSoldDate":LastSoldDate,
                    "TotalQty": ItemQuantity,
                    "ItemOrderList": ItemOrderList
                }
                itemList.append(tempContaxt)

            return Response({"message":"Success","status":200,"data":itemList}) 
        else:            
            return Response({"message":"Invalid CardCode","status":201,"data":[]}) 
    except Exception as e:
        return Response({"message":str(e),"status":201,"data":[]})

# update Category Invoice and Uom
@api_view(['GET'])
def syncInvoice(request):
    # try:
        # Import and sync Invoice
        invoiceFile ="Invoice/INV.py"
        exec(compile(open(invoiceFile, "rb").read(), invoiceFile, 'exec'), {})
        
        # Import and sync Invoice recive payment
        incomingPayments ="Invoice/inv_incoming_payments.py"
        exec(compile(open(incomingPayments, "rb").read(), incomingPayments, 'exec'), {})
       
        # Import and sync Invoice return items or credit note
        creditNotes ="Invoice/inv_credit_notes.py"
        exec(compile(open(creditNotes, "rb").read(), creditNotes, 'exec'), {})

        return Response({"message":"Successful","status":200, "data":[]})
    # except Exception as e:
    #     return Response({"message":str(e),"status":201,"Model": "Invoice" ,"data":[]})


def showIncomingPayments(objs):
    allIncomingPayments = []
    for obj in objs:
        paymentObj = IncomingPaymentsSerializer(obj, many=False)
        finalIncomingPayment = json.loads(json.dumps(paymentObj.data))

        if IncomingPaymentInvoices.objects.filter(IncomingPaymentsId = obj.id).exists():
            invObjs = IncomingPaymentInvoices.objects.filter(IncomingPaymentsId = obj.id)
            invJson = IncomingPaymentInvoicesSerializer(invObjs, many=True)
            finalIncomingPayment['IncomingPaymentInvoices'] = invJson.data
        else:
            finalIncomingPayment['IncomingPaymentInvoices'] = []
        allIncomingPayments.append(finalIncomingPayment)

    return allIncomingPayments



# {"SalesPersonCode": 1}
def InvoiceShowMini(Invoices_obj):
    allqt = InvoiceSerializer(Invoices_obj, many=True)
    return allqt.data