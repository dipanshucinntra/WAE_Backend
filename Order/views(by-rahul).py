from django.conf import settings
from django.shortcuts import render, redirect  
from django.http import JsonResponse, HttpResponse
from PaymentTermsTypes.models import PaymentTermsTypes
from PaymentTermsTypes.serializers import PaymentTermsTypesSerializer

from Project.models import Project
from Project.serializers import ProjectSerializer
from global_fun import tree
from .models import *
from Employee.models import Employee
from BusinessPartner.models import *
from Opportunity.models import *
from Lead.models import Lead
import requests, json

from Attachment.models import Attachment
from Attachment.serializers import AttachmentSerializer

from rest_framework.decorators import api_view    
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import JSONParser

from BusinessPartner.serializers import *
from Employee.serializers import *

from pytz import timezone
from datetime import datetime as dt

import os
from django.core.files.storage import FileSystemStorage

date = dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d')
yearmonth = dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m')
time = dt.now(timezone("Asia/Kolkata")).strftime('%H:%M %p')

# Create your views here.  

#Order Create API
@api_view(['POST'])
def create(request):
    try:
        TaxDate = request.data['TaxDate']
        DocDueDate = request.data['DocDueDate']
        ContactPersonCode = request.data['ContactPersonCode']
        ContactPersonCodeEnd = request.data['ContactPersonCodeEnd']
        DiscountPercent = request.data['DiscountPercent']
        DocDate = request.data['DocDate']
        CardCode = request.data['CardCode']
        CardName = request.data['CardName']
        CardCodeEnd = request.data['CardCodeEnd']
        CardNameEnd = request.data['CardNameEnd']
        Comments = request.data['Comments']
        SalesPersonCode = request.data['SalesPersonCode']
        
        ContactPersonName = request.data['ContactPersonName']
        ContactNumber = request.data['ContactNumber']
        Designation = request.data['Designation']
        Email = request.data['Email']
        Address = request.data['Address']
        
        CreateDate = request.data['CreateDate']
        CreateTime = request.data['CreateTime']
        UpdateDate = request.data['UpdateDate']
        UpdateTime = request.data['UpdateTime']
        
        OrdNo = request.data['OrdNo']
        PoNo = request.data['PoNo']
        DatePO = request.data['DatePO']
        Attach = request.data['Attach']
        Caption = request.data['Caption']
        Project = request.data['Project']
        
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
        
        NetTotal = request.data['NetTotal']
        
        U_LEADID = request.data['U_LEADID']
        U_LEADNM = request.data['U_LEADNM']
        
        #added by millan on 07-10-2022
        GroupType = request.data['GroupType']
        POAmount = request.data['POAmount']
        ProjectLocation = request.data['ProjectLocation']
        OPSNumber = request.data['OPSNumber']
        UrlNo = request.data['UrlNo']
        OtherInstruction = request.data['OtherInstruction']
        GSTNo = request.data['GSTNo']
        #added by millan on 07-10-2022
        
        #added by millan on 11-10-2022
        MICharges = request.data['MICharges']
        LOCharges = request.data['LOCharges']
        Intall = request.data['Intall']
        CivWork = request.data['CivWork']
        SSStatus = request.data['SSStatus']
        PlumStatus = request.data['PlumStatus']
        #added by millan on 11-10-2022
        
        IncidentalCharges = request.data['IncidentalCharges']
        CivilWorkCharges = request.data['CivilWorkCharges']
        PlumbingCharges = request.data['PlumbingCharges']
        
        #added by millan on 04-11-2022
        technical_details = request.data['technical_details']
        approved_drawing = request.data['approved_drawing']
        addendum = request.data['addendum']
        special_instructions = request.data['special_instructions']

        # new keys added 22-02-2023
        PlumbingStatusSide = request.data['PlumbingStatusSide']
        CivilWorkSide      = request.data['CivilWorkSide']
        SiteSurveySide     = request.data['SiteSurveySide']
        SiteSurveySerialNo     = request.data['SiteSurveySerialNo']
        CrainCharges       = request.data['CrainCharges']
        LabourCharges      = request.data['LabourCharges']

        ConsultingFee      = request.data['ConsultingFee']
        SolutionType      = request.data['SolutionType']
        
        # these keys are for project
        kit_consultant_code = request.data['kit_consultant_code']
        kit_consultant_name = request.data['kit_consultant_name']
        kit_contact_person = request.data['kit_contact_person']
        
        mep_consultant_code = request.data['mep_consultant_code']
        mep_consultant_name = request.data['mep_consultant_name']
        mep_contact_person = request.data['mep_contact_person']
        
        pm_consultant_code = request.data['pm_consultant_code']
        pm_consultant_name = request.data['pm_consultant_name']
        pm_contact_person = request.data['pm_contact_person']
        
        cli_consultant_code = request.data['cli_consultant_code']
        cli_consultant_name = request.data['cli_consultant_name']
        cli_contact_person = request.data['cli_contact_person']
        
        contr_consultant_code = request.data['contr_consultant_code']
        contr_consultant_name = request.data['contr_consultant_name']
        contr_contact_person = request.data['contr_contact_person']
        
        fcm_consultant_code = request.data['fcm_consultant_code']
        fcm_consultant_name = request.data['fcm_consultant_name']
        fcm_contact_person = request.data['fcm_contact_person']
        
        arch_consultant_code = request.data['arch_consultant_code']
        arch_consultant_name = request.data['arch_consultant_name']
        arch_contact_person = request.data['arch_contact_person']
        
        oth_consultant_code = request.data['oth_consultant_code']
        oth_consultant_name = request.data['oth_consultant_name']
        oth_contact_person =  request.data['oth_contact_person']

        
        lines = json.loads(request.data['DocumentLines'])
        print("Lines", len(lines))
        addonlines = json.loads(request.data['AddOnDocumentLines'])
        #print(addonlines)
        print("Add on Lines", len(addonlines))
        DocTotal=0
        for line in lines:
            DocTotal = float(DocTotal) + float(line['Quantity']) * float(line['UnitPrice'])
        print(DocTotal)
        try:
            model=Order(OrdNo = OrdNo, PoNo = PoNo, DatePO = DatePO, Project = Project, TaxDate = TaxDate, DocDueDate = DocDueDate, ContactPersonCode = ContactPersonCode, ContactPersonCodeEnd = ContactPersonCodeEnd, DiscountPercent = DiscountPercent, DocDate = DocDate, CardCode = CardCode, CardName = CardName, CardCodeEnd = CardCodeEnd, CardNameEnd = CardNameEnd, Comments = Comments, SalesPersonCode = SalesPersonCode, DocumentStatus="bost_Open", CancelStatus="csNo", DocTotal = DocTotal, NetTotal=NetTotal, CreateDate = CreateDate, CreateTime = CreateTime, UpdateDate = UpdateDate, UpdateTime = UpdateTime, PaymentGroupCode=PaymentGroupCode, BPLID=BPLID,U_Term_Condition=U_Term_Condition, U_TermInterestRate=U_TermInterestRate, U_TermPaymentTerm=U_TermPaymentTerm, U_TermDueDate=U_TermDueDate, U_OPPID=U_OPPID, U_OPPRNM=U_OPPRNM, U_QUOTNM=U_QUOTNM, U_QUOTID=U_QUOTID, U_LEADID=U_LEADID, U_LEADNM=U_LEADNM, GroupType=GroupType, POAmount=POAmount, ProjectLocation=ProjectLocation, OPSNumber=OPSNumber, UrlNo=UrlNo, OtherInstruction=OtherInstruction, GSTNo=GSTNo, SSStatus = SSStatus, technical_details = technical_details, approved_drawing = approved_drawing, addendum = addendum, special_instructions = special_instructions, MICharges = MICharges, LOCharges = LOCharges, Intall = Intall, CivWork = CivWork, PlumStatus = PlumStatus, IncidentalCharges = IncidentalCharges, CivilWorkCharges = CivilWorkCharges, PlumbingCharges = PlumbingCharges, ContactPersonName = ContactPersonName, ContactNumber = ContactNumber, Designation = Designation, Email = Email, Address = Address,
            PlumbingStatusSide = PlumbingStatusSide, CivilWorkSide = CivilWorkSide, SiteSurveySide = SiteSurveySide, SiteSurveySerialNo=SiteSurveySerialNo, CrainCharges = CrainCharges, LabourCharges = LabourCharges, ConsultingFee=ConsultingFee, SolutionType=SolutionType, kit_consultant_code = kit_consultant_code, kit_consultant_name = kit_consultant_name, kit_contact_person = kit_contact_person, mep_consultant_code = mep_consultant_code, mep_consultant_name = mep_consultant_name, mep_contact_person = mep_contact_person, pm_consultant_code = pm_consultant_code, pm_consultant_name = pm_consultant_name, pm_contact_person = pm_contact_person, cli_consultant_code = cli_consultant_code, cli_consultant_name = cli_consultant_name, cli_contact_person = cli_contact_person, contr_consultant_code = contr_consultant_code, contr_consultant_name = contr_consultant_name, contr_contact_person = contr_contact_person, fcm_consultant_code = fcm_consultant_code, fcm_consultant_name = fcm_consultant_name, fcm_contact_person = fcm_contact_person, arch_consultant_code = arch_consultant_code, arch_consultant_name = arch_consultant_name, arch_contact_person = arch_contact_person, oth_consultant_code = oth_consultant_code, oth_consultant_name = oth_consultant_name, oth_contact_person =  oth_contact_person)
    
            model.save()

            qt = Order.objects.latest('id')
            fetchid = qt.id
            
            ORD = "ORD"+str(format(fetchid, '05'))
            model = Order.objects.get(pk = fetchid)
            model.OrdNo = ORD
            model.save()
            
            #added by millan on 12-10-2022
            cc_code = model.CardCode
            if cc_code != "" and BusinessPartner.objects.filter(CardCode = cc_code).exists():
                model = BusinessPartner.objects.get(CardCode = cc_code)
                model.CustomerStatus = 'Customer'
                model.save()

            #added by millan on 12-10-2022
                        
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
                
                FileName = File.name #added by millan on 17-10-2022 for storing file name

                att=Attachment(File=attachmentsImage_url, Caption=Caption, LinkType="Order", LinkID=fetchid, CreateDate=CreateDate, CreateTime=CreateTime, UpdateDate=UpdateDate, UpdateTime=UpdateTime, FileName = FileName)
                
                att.save()
            
        except Exception as e:
            return Response({"message":str(e),"status":201,"data":[]})
        try:
            addr = json.loads(request.data['AddressExtension'])
            model_add = AddressExtension(OrderID = qt.id, BillToBuilding = addr['BillToBuilding'], ShipToState = addr['ShipToState'], BillToCity = addr['BillToCity'], ShipToCountry = addr['ShipToCountry'], BillToZipCode = addr['BillToZipCode'], ShipToStreet = addr['ShipToStreet'], BillToState = addr['BillToState'], ShipToZipCode = addr['ShipToZipCode'], BillToStreet = addr['BillToStreet'], ShipToBuilding = addr['ShipToBuilding'], ShipToCity = addr['ShipToCity'], BillToCountry = addr['BillToCountry'], U_SCOUNTRY = addr['U_SCOUNTRY'], U_SSTATE = addr['U_SSTATE'], U_SHPTYPB = addr['U_SHPTYPB'], U_BSTATE = addr['U_BSTATE'], U_BCOUNTRY = addr['U_BCOUNTRY'], U_SHPTYPS = addr['U_SHPTYPS'])
            model_add.save()
        except Exception as e:
            Order.objects.filter(pk=qt.id).delete()
            return Response({"message":str(e),"status":201,"data":[{"model":"AddressExtension"}]})
        
        try:
            LineNum = 0
            for line in lines:
                model_lines = DocumentLines(LineNum = LineNum, OrderID = qt.id, Quantity = line['Quantity'], UnitPrice = line['UnitPrice'], DiscountPercent = line['DiscountPercent'], ItemCode = line['ItemCode'], ItemDescription = line['ItemDescription'], TaxCode = line['TaxCode'], U_FGITEM = line['U_FGITEM'], CostingCode2 = line['CostingCode2'], ProjectCode = line['ProjectCode'], FreeText = line['FreeText'], Tap_Qty = line['Tap_Qty'], Tap_Type = line['Tap_Type'], Ht_Capacity = line['Ht_Capacity'], Ct_Capacity = line['Ct_Capacity'], At_Capacity = line['At_Capacity'], Pro_Capacity = line['Pro_Capacity'], Machine_Dimension = line['Machine_Dimension'], Machine_Colour = line['Machine_Colour'], Type_of_Machine = line['Type_of_Machine'], Machine_Body_Material = line['Machine_Body_Material'], UV_Germ = line['UV_Germ'], Sales_Type = line['Sales_Type'], Special_Remark = line['Special_Remark'], Tax = line['Tax'], UomNo = line['UomNo'], IT_MICharges=line['IT_MICharges'], IT_LOCharges=line['IT_LOCharges'], IT_Intall=line['IT_Intall']) #updated by millan on 01-November-2022
                model_lines.save()
                LineNum=LineNum+1
        except Exception as e:
            DocumentLines.objects.filter(OrderID=qt.id).delete()
            Order.objects.filter(pk=qt.id).delete()
            return Response({"message":str(e),"status":201,"data":[{"model":"DocumentLines"}]})
        
        print("Len--", addonlines)
        if addonlines !="":
            try:
                LineNum = 0
                for addon in addonlines:
                    model_addlines = AddOnDocumentLines(LineNum = LineNum, OrderID = qt.id, Quantity = addon['Quantity'], UnitPrice = addon['UnitPrice'], ItemCode = addon['ItemCode'], ParentItemCode = addon['ParentItemCode'], ItemDescription = addon['ItemDescription'])
                    model_addlines.save()
                    LineNum=LineNum+1
            except Exception as e:
                DocumentLines.objects.filter(OrderID=qt.id).delete()
                AddOnDocumentLines.objects.filter(OrderID=qt.id).delete()
                Order.objects.filter(pk=qt.id).delete()
                return Response({"message":str(e),"status":201,"data":[{"model":"AddOnDocumentLines"}]})

        #return Response({"message":"successful","status":200,"data":[{"qt_Id":qt.id}]})
            
        if settings.SAPORD == True:
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
            
            print(qt_data)
            print(json.dumps(qt_data))

            res = requests.post(settings.BASEURL+'/Orders', data=json.dumps(qt_data), cookies=r.cookies, verify=False)
            live = json.loads(res.text)
            
            if "DocEntry" in live:
                print(live['DocEntry'])
                
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
                
                return Response({"message":"successful","status":200,"data":[{"qt_Id":qt.id, "DocEntry":live['DocEntry']}]})
            else:
                SAP_MSG = live['error']['message']['value']
                print(SAP_MSG)
                Order.objects.get(pk=qt.id).delete()
                allline = DocumentLines.objects.filter(OrderID=qt.id)
                for dcline in allline:
                    dcline.delete()
                    
                alladd = AddressExtension.objects.filter(OrderID=qt.id)
                for ad in alladd:
                    ad.delete()
                return Response({"message":SAP_MSG,"SAP_error":SAP_MSG, "status":202,"data":[]})
        else:
            model = Order.objects.get(pk = fetchid)
            model.DocEntry = fetchid
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
                emp_obj =  Employee.objects.get(SalesEmployeeCode=SalesPersonCode)
                report_obj = Employee.objects.get(SalesEmployeeCode=emp_obj.reportingTo)
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
                    model.OrdLevel1_id = report_SalesEmployeeCode
                    model.OrdLevel1Status = "Pending"
                elif int(level) == 3:
                    model.OrdLevel3_id = SalesPersonCode
                    model.OrdLevel3Status = "Approved"
                    model.OrdLevel2_id = report_SalesEmployeeCode
                    model.OrdOrdLevel2Status = "Pending"
                elif int(level) == 4:
                    model.OrdLevel3_id = report_SalesEmployeeCode
                    model.OrdLevel3Status = "Pending"
                model.save()
            
            return Response({"message":"successful","status":200,"data":[{"qt_Id":qt.id, "DocEntry":qt.id}]})
    except Exception as e:
        return Response({"message":str(e),"status":201,"data":[{"model":"End"}]})



# #Order amendment update API
# @api_view(['POST'])
# def orderamendment_update(request):
#     fetchid = request.data['id']
#     try:
#         model = Order.objects.get(pk = fetchid)
#         lines = request.data['DocumentLines']
#         item_ids = [item["Oid"] for item in lines if 'Oid' in item]
#         doc = DocumentLines.objects.filter(OrderID = fetchid).exclude(id__in=item_ids)
#         for line in lines:
#             if "Oid" in line:
#                 model_line = DocumentLines.objects.get(pk = line['Oid'])
#                 model_line.Quantity=line['Quantity']
#                 model_line.UnitPrice=line['UnitPrice']
#                 model_line.DiscountPercent=line['DiscountPercent']
#                 model_line.ItemCode=line['ItemCode']
#                 model_line.ItemDescription=line['ItemDescription']
#                 model_line.TaxCode=line['TaxCode']
#                 model_line.ProjectCode=line['ProjectCode']
#                 model_line.U_FGITEM=line['U_FGITEM']
#                 model_line.CostingCode2=line['CostingCode2']
#                 model_line.FreeText=line['FreeText']               
#                 model_line.UomNo=line['UomNo']               
#                 model_line.Tax=line['Tax']               
#                 model_line.IT_MICharges=line['IT_MICharges']               
#                 model_line.IT_LOCharges=line['IT_LOCharges']               
#                 model_line.IT_Intall=line['IT_Intall']               
#                 model_line.Tap_Qty=line['Tap_Qty']               
#                 model_line.Tap_Type=line['Tap_Type']               
#                 model_line.Ht_Capacity=line['Ht_Capacity']               
#                 model_line.Ct_Capacity=line['Ct_Capacity']               
#                 model_line.At_Capacity=line['At_Capacity']               
#                 model_line.Pro_Capacity=line['Pro_Capacity']               
#                 model_line.Machine_Dimension=line['Machine_Dimension']               
#                 model_line.Machine_Colour=line['Machine_Colour']               
#                 model_line.Type_of_Machine=line['Type_of_Machine']               
#                 model_line.Machine_Body_Material=line['Machine_Body_Material']               
#                 model_line.UV_Germ=line['UV_Germ']               
#                 model_line.Sales_Type=line['Sales_Type']               
#                 model_line.Special_Remark=line['Special_Remark']               
#                 model_line.addon_line=line['addon_line']               
#                 model_line.save()
#             else:
#                 # lastline = DocumentLines.objects.filter(OrderID = fetchid).order_by('-LineNum')[:1]
#                 NewLine = 0
#                 model_lines = DocumentLines(OrderID = fetchid, LineNum=NewLine, Quantity = line['Quantity'], UnitPrice = line['UnitPrice'], DiscountPercent = line['DiscountPercent'], ItemCode = line['ItemCode'], ItemDescription = line['ItemDescription'], TaxCode = line['TaxCode'], U_FGITEM = line['U_FGITEM'], CostingCode2 = line['CostingCode2'], ProjectCode = line['ProjectCode'], FreeText = line['FreeText'], IT_MICharges=line['IT_MICharges'],IT_LOCharges=line['IT_LOCharges'],IT_Intall=line['IT_Intall'],Tax=line['Tax'],UomNo=line['UomNo'],Tap_Qty=line['Tap_Qty'],Tap_Type=line['Tap_Type'],Ht_Capacity=line['Ht_Capacity'],Ct_Capacity=line['Ct_Capacity'],At_Capacity=line['At_Capacity'],Pro_Capacity=line['Pro_Capacity'],Machine_Dimension=line['Machine_Dimension'],Machine_Colour=line['Machine_Colour'],Type_of_Machine=line['Type_of_Machine'],Machine_Body_Material=line['Machine_Body_Material'],UV_Germ=line['UV_Germ'],Sales_Type=line['Sales_Type'],Special_Remark=line['Special_Remark'])
#                 model_lines.save()
#         model.NetTotal = request.data['NetTotal']
#         model.save()
#         doc.delete()
#         return Response({"message":"successful","status":200, "data":[]})
#     except Exception as e:
#         return Response({"message":str(e),"status":201,"data":[{"model":"End"}]})


# #Order Update API
# @api_view(['POST'])
# def orderamendment_update(request):
#     fetchid = request.data['id']
#     try:
#         model = Order.objects.get(pk = fetchid)
#         if model.amendment_status != "Inactive":
#             model.TaxDate = request.data['TaxDate']
#             model.DocDueDate = request.data['DocDueDate']
#             model.ContactPersonCode = request.data['ContactPersonCode']
#             model.ContactPersonCodeEnd = request.data['ContactPersonCodeEnd']
#             model.DiscountPercent = float(request.data['DiscountPercent'])
#             model.DocDate = request.data['DocDate']
#             model.CardCode = request.data['CardCode']
#             model.CardName = request.data['CardName']
#             model.CardCodeEnd = request.data['CardCodeEnd']
#             model.CardNameEnd = request.data['CardNameEnd']
#             model.Comments = request.data['Comments']
#             model.SalesPersonCode = request.data['SalesPersonCode']
            
#             model.ContactPersonName = request.data['ContactPersonName']
#             model.ContactNumber = request.data['ContactNumber']
#             model.Designation = request.data['Designation']
#             model.Email = request.data['Email']
#             model.Address = request.data['Address']
            
#             model.CreateDate = request.data['CreateDate']
#             model.CreateTime = request.data['CreateTime']
#             model.UpdateDate = request.data['UpdateDate']
#             model.UpdateTime = request.data['UpdateTime']
            
#             model.OrdNo = request.data['OrdNo']
#             model.PoNo = request.data['PoNo']
#             model.DatePO = request.data['DatePO']
#             model.Attach = request.data['Attach']
#             model.Caption = request.data['Caption']
#             model.Project = request.data['Project']
            
#             model.PaymentGroupCode = request.data['PaymentGroupCode']
#             model.BPLID = request.data['BPLID']
#             model.U_Term_Condition = request.data['U_Term_Condition']
#             model.U_TermInterestRate = request.data['U_TermInterestRate']
#             model.U_TermPaymentTerm = request.data['U_TermPaymentTerm']
#             model.U_TermDueDate = request.data['U_TermDueDate']
            
#             model.U_QUOTNM = request.data['U_QUOTNM']
#             model.U_QUOTID = request.data['U_QUOTID']    
            
#             model.U_OPPID = request.data['U_OPPID']
#             model.U_OPPRNM = request.data['U_OPPRNM']
            
#             model.NetTotal = request.data['NetTotal']
            
#             model.U_LEADID = request.data['U_LEADID']
#             model.U_LEADNM = request.data['U_LEADNM']
            
#             #added by millan on 07-10-2022
#             model.GroupType = request.data['GroupType']
#             model.POAmount = request.data['POAmount']
#             model.ProjectLocation = request.data['ProjectLocation']
#             model.OPSNumber = request.data['OPSNumber']
#             model.UrlNo = request.data['UrlNo']
#             model.OtherInstruction = request.data['OtherInstruction']
#             model.GSTNo = request.data['GSTNo']
#             #added by millan on 07-10-2022
            
#             #added by millan on 11-10-2022
#             model.MICharges = request.data['MICharges']
#             model.LOCharges = request.data['LOCharges']
#             model.Intall = request.data['Intall']
#             model.CivWork = request.data['CivWork']
#             model.SSStatus = request.data['SSStatus']
#             model.PlumStatus = request.data['PlumStatus']
#             #added by millan on 11-10-2022
            
#             model.IncidentalCharges = request.data['IncidentalCharges']
#             model.CivilWorkCharges = request.data['CivilWorkCharges']
#             model.PlumbingCharges = request.data['PlumbingCharges']
            
#             #added by millan on 04-11-2022
#             model.technical_details = request.data['technical_details']
#             model.approved_drawing = request.data['approved_drawing']
#             model.addendum = request.data['addendum']
#             model.special_instructions = request.data['special_instructions']

#             # new keys added 22-02-2023
#             model.PlumbingStatusSide = request.data['PlumbingStatusSide']
#             model.CivilWorkSide      = request.data['CivilWorkSide']
#             model.SiteSurveySide     = request.data['SiteSurveySide']
#             model.SiteSurveySerialNo     = request.data['SiteSurveySerialNo']
#             model.CrainCharges       = request.data['CrainCharges']
#             model.LabourCharges      = request.data['LabourCharges']

#             model.ConsultingFee      = request.data['ConsultingFee']
#             model.SolutionType      = request.data['SolutionType']
            
#             #these keys are for project
#             model.kit_consultant_code = request.data['kit_consultant_code']
#             model.kit_consultant_name = request.data['kit_consultant_name']
#             model.kit_contact_person = request.data['kit_contact_person']

#             model.mep_consultant_code = request.data['mep_consultant_code']
#             model.mep_consultant_name = request.data['mep_consultant_name']
#             model.mep_contact_person = request.data['mep_contact_person']

#             model.pm_consultant_code = request.data['pm_consultant_code']
#             model.pm_consultant_name = request.data['pm_consultant_name']
#             model.pm_contact_person = request.data['pm_contact_person']

#             model.cli_consultant_code = request.data['cli_consultant_code']
#             model.cli_consultant_name = request.data['cli_consultant_name']
#             model.cli_contact_person = request.data['cli_contact_person']
            
#             model.contr_consultant_code = request.data['contr_consultant_code']
#             model.contr_consultant_name = request.data['contr_consultant_name']
#             model.contr_contact_person = request.data['contr_contact_person']
            
#             model.fcm_consultant_code = request.data['fcm_consultant_code']
#             model.fcm_consultant_name = request.data['fcm_consultant_name']
#             model.fcm_contact_person = request.data['fcm_contact_person']
            
#             model.arch_consultant_code = request.data['arch_consultant_code']
#             model.arch_consultant_name = request.data['arch_consultant_name']
#             model.arch_contact_person = request.data['arch_contact_person']
            
#             model.oth_consultant_code = request.data['oth_consultant_code']
#             model.oth_consultant_name = request.data['oth_consultant_name']
#             model.oth_contact_person =  request.data['oth_contact_person']
#             am_count = int(model.amendment_action) + 1
#             model.amendment_action = str(am_count)
#             model.save()
#             print('Draft Update')
#             if request.data['AddressExtension'] !="":
#                 addr = json.loads(request.data['AddressExtension'])
#                 model_add = AddressExtension.objects.get(id = addr['id'])
#                 print(model_add)
                
#                 model_add.BillToBuilding = addr['BillToBuilding']
#                 model_add.ShipToState = addr['ShipToState']
#                 model_add.BillToCity = addr['BillToCity']
#                 model_add.ShipToCountry = addr['ShipToCountry']
#                 model_add.BillToZipCode = addr['BillToZipCode']
#                 model_add.ShipToStreet = addr['ShipToStreet']
#                 model_add.BillToState = addr['BillToState']
#                 model_add.ShipToZipCode = addr['ShipToZipCode']
#                 model_add.BillToStreet = addr['BillToStreet']
#                 model_add.ShipToBuilding = addr['ShipToBuilding']
#                 model_add.ShipToCity = addr['ShipToCity']
#                 model_add.BillToCountry = addr['BillToCountry']
#                 model_add.U_SCOUNTRY = addr['U_SCOUNTRY']
#                 model_add.U_SSTATE = addr['U_SSTATE']
#                 model_add.U_SHPTYPB = addr['U_SHPTYPB']
#                 model_add.U_BSTATE = addr['U_BSTATE']
#                 model_add.U_BCOUNTRY = addr['U_BCOUNTRY']
#                 model_add.U_SHPTYPS = addr['U_SHPTYPS']
        
#                 model_add.save()
#                 print("add save")
            
#             print('lines', request.data['DocumentLines'])
#             updatedItemIdsDoc = []
#             if request.data['DocumentLines'] !=[]:
#                 print('if lines')
#                 lines = json.loads(request.data['DocumentLines'])
#                 print(lines)
#                 for line in lines:
#                     print('line')
#                     print(line)
#                     if "id" in line:
#                         try:
#                             model_line = DocumentLines.objects.get(pk = line['id'])
#                             model_line.At_Capacity=line['At_Capacity']
#                             model_line.CostingCode2=line['CostingCode2']
#                             model_line.Ct_Capacity=line['Ct_Capacity']
#                             model_line.DiscountPercent=line['DiscountPercent']
#                             model_line.FreeText=line['FreeText']
#                             model_line.Ht_Capacity=line['Ht_Capacity']
#                             model_line.ItemCode=line['ItemCode']
#                             model_line.ItemDescription=line['ItemDescription']
#                             model_line.IT_Intall=line['IT_Intall']
#                             model_line.IT_LOCharges=line['IT_LOCharges']
#                             model_line.IT_MICharges=line['IT_MICharges']
#                             model_line.Machine_Body_Material=line['Machine_Body_Material']
#                             model_line.Machine_Colour=line['Machine_Colour']
#                             model_line.Machine_Dimension=line['Machine_Dimension']
#                             model_line.ProjectCode=line['ProjectCode']
#                             model_line.Pro_Capacity=line['Pro_Capacity']
#                             model_line.Quantity=line['Quantity']
#                             model_line.Sales_Type=line['Sales_Type']
#                             model_line.Special_Remark=line['Special_Remark']
#                             model_line.Tap_Qty=line['Tap_Qty']
#                             model_line.Tap_Type=line['Tap_Type']
#                             model_line.Tax=line['Tax']
#                             model_line.TaxCode=line['TaxCode']
#                             model_line.Type_of_Machine=line['Type_of_Machine']
#                             model_line.UnitPrice=line['UnitPrice']
#                             model_line.UomNo=line['UomNo']
#                             model_line.UV_Germ=line['UV_Germ']
#                             model_line.U_FGITEM=line['U_FGITEM']

#                             model_line.save()
#                             updatedItemIdsDoc.append(line['id'])
#                             print("item update")
#                         except Exception as e:
#                             print("item not update")
#                             return Response({"message":"Item not update","status":201,"data":[{"Error":str(e)}]})
#                     else:
#                         try:
#                             print('go add for item')
#                             print(line)
#                             if DocumentLines.objects.filter(OrderID = fetchid).exists():
#                                 lastline = DocumentLines.objects.filter(OrderID = fetchid).order_by('-LineNum')[:1]
#                                 NewLine = int(lastline[0].LineNum) + 1
#                             else:
#                                 NewLine = 1
#                             print('NewLine', NewLine)
#                             print(line['Quantity'])
#                             print(line['ItemCode'])
#                             model_lines = DocumentLines(OrderID = fetchid, LineNum=NewLine, At_Capacity = line['At_Capacity'], CostingCode2 = line['CostingCode2'], Ct_Capacity = line['Ct_Capacity'], DiscountPercent = line['DiscountPercent'], FreeText = line['FreeText'], Ht_Capacity = line['Ht_Capacity'], ItemCode = line['ItemCode'], ItemDescription = line['ItemDescription'], IT_Intall = line['IT_Intall'], IT_LOCharges = line['IT_LOCharges'], IT_MICharges = line['IT_MICharges'], Machine_Body_Material = line['Machine_Body_Material'], Machine_Colour = line['Machine_Colour'], Machine_Dimension = line['Machine_Dimension'], ProjectCode = line['ProjectCode'], Pro_Capacity = line['Pro_Capacity'], Quantity = line['Quantity'], Sales_Type = line['Sales_Type'], Special_Remark = line['Special_Remark'], Tap_Qty = line['Tap_Qty'], Tap_Type = line['Tap_Type'], Tax = line['Tax'], TaxCode = line['TaxCode'], Type_of_Machine = line['Type_of_Machine'], UnitPrice = line['UnitPrice'], UomNo = line['UomNo'], UV_Germ = line['UV_Germ'], U_FGITEM = line['U_FGITEM'])
#                             model_lines.save()
#                             Itm = DocumentLines.objects.latest('id')
#                             updatedItemIdsDoc.append(Itm.id)
#                             print("item insert")
#                         except Exception as e:
#                             print("item not add")
#                             print(str(e))
#                             return Response({"message":"Item not add","status":201,"data":[{"Error":str(e)}]})
#                 if DocumentLines.objects.filter(OrderID = fetchid).exclude(id__in = updatedItemIdsDoc).exists():
#                     DocumentLines.objects.filter(OrderID = fetchid).exclude(id__in = updatedItemIdsDoc).delete()
#                     print('delete old item')
#             else:
#                 if DocumentLines.objects.filter(OrderID = fetchid).exists():
#                     DocumentLines.objects.filter(OrderID = fetchid).delete()
#                     print('delete all old item')
            
#             print('Add lines', request.data['AddOnDocumentLines'])
#             updatedItemIds = []
#             if request.data['AddOnDocumentLines'] !=[]:
#                 print('if addlines')
#                 addlines = json.loads(request.data['AddOnDocumentLines'])
#                 for line in addlines:
#                     if "id" in line:
#                         model_line = AddOnDocumentLines.objects.get(pk = line['id'])
#                         model_line.Quantity=line['Quantity']
#                         model_line.UnitPrice=line['UnitPrice']
#                         model_line.ItemCode=line['ItemCode']
#                         model_line.ParentItemCode=line['ParentItemCode']
#                         model_line.ItemDescription=line['ItemDescription']
#                         model_line.save()
#                         updatedItemIds.append(line['id'])
#                         print("addon item update")
#                     else:
#                         if AddOnDocumentLines.objects.filter(OrderID = fetchid).exists():
#                             lastline = AddOnDocumentLines.objects.filter(OrderID = fetchid).order_by('-LineNum')[:1]
#                             NewLine = int(lastline[0].LineNum) + 1
#                         else:
#                             NewLine = 1
#                         model_lines = AddOnDocumentLines(OrderID = fetchid, LineNum=NewLine, Quantity = line['Quantity'], UnitPrice = line['UnitPrice'], ItemCode = line['ItemCode'], ParentItemCode=line['ParentItemCode'], ItemDescription = line['ItemDescription'])
#                         model_lines.save()
#                         AddOnItm = AddOnDocumentLines.objects.latest('id')
#                         updatedItemIds.append(AddOnItm.id)
#                         print("addon item insert")
            
#                 if AddOnDocumentLines.objects.filter(OrderID = fetchid).exclude(id__in = updatedItemIds).exists():
#                     AddOnDocumentLines.objects.filter(OrderID = fetchid).exclude(id__in = updatedItemIds).delete()
#                     print('delete old addon item')
#             else:
#                 if AddOnDocumentLines.objects.filter(OrderID = fetchid).exists():
#                     AddOnDocumentLines.objects.filter(OrderID = fetchid).delete()
#                     print('delete all old addon item')
                
#                 return Response({"message":"successful","status":200, "data":[json.loads(json.dumps(request.data))]})
#             return Response({"message":"successful","status":200, "data":[json.loads(json.dumps(request.data))]})
#         else:
#             return Response({"message":"Time Out","status":200, "data":[]})
#     except Exception as e:
#         return Response({"message":"Not Update","status":201,"data":[{"Error":str(e)}]})


#Order Update API
@api_view(['POST'])
def orderamendment_update(request):
    fetchid = request.data['id']
    try:
        model = Order.objects.get(pk = fetchid)
        if model.amendment_status != "Inactive":
            am_count = int(model.amendment_action) + 1
            model.amendment_action = str(am_count)
            model.save()
            try:
                modelhistory_data = OrderHistory.objects.filter(OrderID=fetchid).last().Number
                modelhistory_data += 1
            except:
                modelhistory_data = 1
            modelHistory = OrderHistory(Number=modelhistory_data, OrderID=fetchid, NetTotal=request.data['NetTotal'], CreatedDate=request.data['CreateDate'], CreatedTime=request.data['CreateTime'])
            modelHistory.save()
            
            print('lines', request.data['DocumentLines'])
            if request.data['DocumentLines'] !=[]:
                lines = json.loads(request.data['DocumentLines'])
                lineNum = 1
                for line in lines:
                    model_lines = DocumentLinesHistory(orderhistory_id=modelHistory, OrderID = fetchid, LineNum=lineNum, At_Capacity = line['At_Capacity'], CostingCode2 = line['CostingCode2'], Ct_Capacity = line['Ct_Capacity'], DiscountPercent = line['DiscountPercent'], FreeText = line['FreeText'], Ht_Capacity = line['Ht_Capacity'], ItemCode = line['ItemCode'], ItemDescription = line['ItemDescription'], IT_Intall = line['IT_Intall'], IT_LOCharges = line['IT_LOCharges'], IT_MICharges = line['IT_MICharges'], Machine_Body_Material = line['Machine_Body_Material'], Machine_Colour = line['Machine_Colour'], Machine_Dimension = line['Machine_Dimension'], ProjectCode = line['ProjectCode'], Pro_Capacity = line['Pro_Capacity'], Quantity = line['Quantity'], Sales_Type = line['Sales_Type'], Special_Remark = line['Special_Remark'], Tap_Qty = line['Tap_Qty'], Tap_Type = line['Tap_Type'], Tax = line['Tax'], TaxCode = line['TaxCode'], Type_of_Machine = line['Type_of_Machine'], UnitPrice = line['UnitPrice'], UomNo = line['UomNo'], UV_Germ = line['UV_Germ'], U_FGITEM = line['U_FGITEM'])
                    model_lines.save()
                    lineNum += 1
                    if request.data['AddOnDocumentLines'] !=[]:
                        print('if addlines')
                        addlines = json.loads(request.data['AddOnDocumentLines'])
                        NewLine = 1
                        for liness in addlines:
                            if line['ItemCode'] == liness['ParentItemCode']:
                                model_lines = AddOnDocumentLinesHistory(documentlineshistory_id= model_lines, OrderID = fetchid, LineNum=NewLine, Quantity = liness['Quantity'], UnitPrice = liness['UnitPrice'], ItemCode = liness['ItemCode'], ParentItemCode=liness['ParentItemCode'], ItemDescription = liness['ItemDescription'])
                                model_lines.save()
                                NewLine+=1
            return Response({"message":"successful","status":200, "data":[json.loads(json.dumps(request.data))]})
        else:
            return Response({"message":"Time Out","status":200, "data":[]})
    except Exception as e:
        return Response({"message":"Not Update","status":201,"data":[{"Error":str(e)}]})




#Order Update API
@api_view(['POST'])
def update(request):
    fetchid = request.data['id']
    try:
        model = Order.objects.get(pk = fetchid)

        model.TaxDate = request.data['TaxDate']
        model.DocDate = request.data['DocDate']
        model.DocDueDate = request.data['DocDueDate']
        
        model.ContactPersonCode = request.data['ContactPersonCode']
        model.DiscountPercent = request.data['DiscountPercent']
        model.Comments = request.data['Comments']
        model.SalesPersonCode = request.data['SalesPersonCode']
        
        model.PaymentGroupCode = request.data['PaymentGroupCode']
        
        
        model.NetTotal = request.data['NetTotal']
        
        model.PoNo = request.data['PoNo']
        model.DatePO = request.data['DatePO']
        model.Attach = request.data['Attach']
        model.Project = request.data['Project']        

        model.U_Term_Condition = request.data['U_Term_Condition']
        model.U_TermInterestRate = request.data['U_TermInterestRate']
        model.U_TermPaymentTerm = request.data['U_TermPaymentTerm']
        model.U_TermDueDate = request.data['U_TermDueDate']
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
                lastline = DocumentLines.objects.filter(OrderID = fetchid).order_by('-LineNum')[:1]
                NewLine = int(lastline[0].LineNum) + 1
                model_lines = DocumentLines(OrderID = fetchid, LineNum=NewLine, Quantity = line['Quantity'], UnitPrice = line['UnitPrice'], DiscountPercent = line['DiscountPercent'], ItemCode = line['ItemCode'], ItemDescription = line['ItemDescription'], TaxCode = line['TaxCode'], U_FGITEM = line['U_FGITEM'], CostingCode2 = line['CostingCode2'], ProjectCode = line['ProjectCode'], FreeText = line['FreeText'])
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

    
        # print(settings.BASEURL+"/Orders('"+model.DocEntry+"')");
        # res = requests.patch(settings.BASEURL+"/Orders("+model.DocEntry+")", data=json.dumps(qt_data), cookies=r.cookies, verify=False)

        print(settings.BASEURL+"/Orders('"+model.DocEntry+"')");
        res = requests.patch(settings.BASEURL+"/Orders("+model.DocEntry+")", data=json.dumps(qt_data), cookies=r.cookies, verify=False)
        print(res.content)

        if len(res.content) !=0 :
            res1 = json.loads(res.content)
            SAP_MSG = res1['error']['message']['value']
            return Response({"message":"Partely successful","status":202,"SAP_error":SAP_MSG, "data":[request.data]})
        else:
            return Response({"message":"successful","status":200, "data":[json.loads(json.dumps(request.data))]})
    except Exception as e:
        return Response({"message":"Not Update","status":201,"data":[{"Error":str(e)}]})

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
        lines_json = DocumentLinesSerializer(lines, many=True)
        jss1 = json.loads(json.dumps(lines_json.data))
        finalOrder['DocumentLines'] = jss1

        # cont = BPEmployee.objects.filter(InternalCode=qt.ContactPersonCode).values("InternalCode","FirstName")
        cont = BPEmployee.objects.filter(InternalCode=qt.ContactPersonCode)
        cont_json = BPEmployeeSerializer(cont, many=True)
        cont_all = json.loads(json.dumps(cont_json.data))

        contEnd = BPEmployee.objects.filter(InternalCode=qt.ContactPersonCodeEnd)
        contEnd_json = BPEmployeeSerializer(contEnd, many=True)
        contEnd_all = json.loads(json.dumps(contEnd_json.data))
        
        #added by millan on 12-September-2022
        try:
            if qt.Project != "":
                if Project.objects.filter(id = qt.Project).exists():
                    project_dls = Project.objects.filter(id = qt.Project)
                    project_json = ProjectSerializer(project_dls, many=True)
                    finalOrder['Project'] = project_json.data
                else:
                    finalOrder['Project'] = []
            else:
                finalOrder['Project'] = []        
        except Exception as e:
            return Response({"message": str(e),"status": 201,"data":[]})        
        
        try:
            if AddOnDocumentLines.objects.filter(OrderID=qt.id).exists():
                addlines = AddOnDocumentLines.objects.filter(OrderID=qt.id)
                addlines_json = AddOnDocumentLinesSerializer(addlines, many=True)
                adjs = json.loads(json.dumps(addlines_json.data))
                finalOrder['AddOnDocumentLines'] = adjs

            else:
                finalOrder['AddOnDocumentLines'] = []
        except Exception as e:
            return Response({"message": str(e),"status": 201,"data":[]})        

        try:
            if Attachment.objects.filter(LinkID = qt.id, LinkType="Order").exists():
                attachment_dls = Attachment.objects.filter(LinkID = qt.id, LinkType="Order")
                attachment_json = AttachmentSerializer(attachment_dls, many=True)
                finalOrder['Attach'] = attachment_json.data
            else:
                finalOrder['Attach'] = []
        except Exception as e:
            return Response({"message": str(e),"status": 201,"data":[]})
       
        try:
            if qt.PaymentGroupCode != "":
                if PaymentTermsTypes.objects.filter(GroupNumber = qt.PaymentGroupCode).exists():
                    payment_dls = PaymentTermsTypes.objects.filter(GroupNumber = qt.PaymentGroupCode)
                    payment_dls_json = PaymentTermsTypesSerializer(payment_dls, many=True)
                    finalOrder['PaymentGroupCode'] = payment_dls_json.data
                else:
                    finalOrder['PaymentGroupCode'] = []
            else:
                finalOrder['PaymentGroupCode'] = []        
        except Exception as e:
            return Response({"message": str(e),"status": 201,"data":[]})        
        #added by millan on 12-September-2022
        
        #added by millan on 04-November-2022
        # try:
        if qt.CardCode !="":
            if BusinessPartner.objects.filter(CardCode = qt.CardCode).exists():
                BPCustCode = BusinessPartner.objects.filter(CardCode = qt.CardCode).values_list('BPCustCode', flat=True)
                BPCCCode = BPCustCode[0][0:6]
                
                if CustCode.objects.filter(OrderId=qt.id).exists(): 
                    
                    model = CustCode.objects.filter(OrderId=qt.id)
                    
                    BPURN = str(model[0].cc_prefix)+str('/URN1')+str(format(model[0].counter, '04'))
                    print("if BPURN: "+str(BPURN))
                    
                    finalOrder['URN'] = BPURN 
                    
                    OrdUrn = Order.objects.get(pk=qt.id)
                    OrdUrn.URN = BPURN
                    
                    OrdUrn.save()
                    
                else:
                    print(BPCCCode)
                    if CustCode.objects.filter(cc_prefix=BPCCCode).exists():
                        cc = CustCode.objects.filter(cc_prefix=BPCCCode).order_by('-id')[:1][0].counter 
                        
                        counter = int(cc) + 1
                        print("if")
                        model = CustCode(cc_prefix=BPCCCode, counter=counter, CustCodeBp=qt.CardCode, OrderId=qt.id)
                        model.save()

                    else: 
                        print("else")
                        counter =1
                        model = CustCode(cc_prefix=BPCCCode, CustCodeBp=qt.CardCode, counter =counter, OrderId=qt.id)
                        model.save()
                    
                    BPURN= str(BPCCCode)+str('/URN1')+str(format(counter, '04'))
                    finalOrder['URN'] = BPURN
                    print("else BPURN: "+str(BPURN))
                    
                    OrdUrn = Order.objects.get(pk=qt.id)
                    OrdUrn.URN = BPURN
                    OrdUrn.save()
                    
        else:
            return Response({"message": "Customer Card Must Exist","status": 201,"data":[]})     
                
        # except Exception as e:
        #     return Response({"message": str(e),"status": 201,"data":[]}) 
        #added by millan on 04-November-2022
        
        # print(cont_all)
        if len(cont) > 0:
            #ContactPerson = cont[0].FirstName
            ContactPerson = cont_json.data
            # print(ContactPerson)
        else:
            ContactPerson = ""

        if len(contEnd) > 0:
            #ContactPerson = cont[0].FirstName
            ContactPersonEnd = contEnd_json.data
            # print(ContactPerson)
        else:
            ContactPersonEnd = ""
            

        sobj = Employee.objects.filter(SalesEmployeeCode=qt.SalesPersonCode).values("SalesEmployeeCode","EmployeeID","SalesEmployeeName", "lastName")
        sobj_json = EmployeeSerializer(sobj, many=True)
        sobj_all = json.loads(json.dumps(sobj_json.data))
        SalesPerson = sobj_json.data

        finalOrder['ContactPersonCode'] = ContactPerson
        finalOrder['ContactPersonCodeEnd'] = ContactPersonEnd
        
        finalOrder['SalesPersonCode'] = SalesPerson
        
        # context = {
        #     'id':qt.id,
        #     'DocEntry':qt.DocEntry,
        #     'DocDueDate':qt.DocDueDate,
        #     'DocDate':qt.DocDate,
        #     'TaxDate':qt.TaxDate,
        #     'ContactPersonCode':qt.ContactPersonCode,
        #     'DiscountPercent':qt.DiscountPercent,
        #     'CardCode':qt.CardCode,
        #     'CardName':qt.CardName,
        #     'Comments':qt.Comments,
        #     'SalesPersonCode':qt.SalesPersonCode,
            
        #     'DocumentStatus':qt.DocumentStatus,
        #     'CancelStatus':qt.CancelStatus,
        #     'DocCurrency':qt.DocCurrency,
        #     'DocTotal':qt.DocTotal,
        #     'VatSum':qt.VatSum,
            
        #     'PaymentGroupCode':qt.PaymentGroupCode,
        #     'U_Term_Condition':qt.U_Term_Condition,
        #     'U_TermInterestRate':qt.U_TermInterestRate,
        #     'U_TermPaymentTerm':qt.U_TermPaymentTerm,
        #     'U_TermDueDate':qt.U_TermDueDate,
        #     'U_LEADID':qt.U_LEADID,
        #     'U_LEADNM':qt.U_LEADNM,
        #     'BPLID':qt.BPLID,
            
        #     'CreationDate':qt.CreationDate,
            
        #     'AddressExtension':jss0,
        #     'DocumentLines':jss1,
            
        #     "CreateDate":qt.CreateDate,
        #     "CreateTime":qt.CreateTime,
        #     "UpdateDate":qt.UpdateDate,
        #     "UpdateTime":qt.UpdateTime
        #     }
            
        allqt.append(finalOrder)
        
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
                # emps = Employee.objects.filter(reportingTo=emp_obj.reportingTo)#.values('id', 'SalesEmployeeCode')
                # SalesEmployeeCode=[]
                # for emp in emps:
                    # SalesEmployeeCode.append(emp.SalesEmployeeCode)
            
            print(SalesEmployeeCode)

            if json_data['Type'] =="over":
                ord = Order.objects.filter(SalesPersonCode__in=SalesEmployeeCode, DocumentStatus="bost_Open", DocDueDate__lt=date)
                allord = OrderShow(ord)
                #print(allord)
            elif json_data['Type'] =="open":
                ord = Order.objects.filter(SalesPersonCode__in=SalesEmployeeCode, DocumentStatus="bost_Open", DocDueDate__gte=date)
                allord = OrderShow(ord)
                #print(allord)
            else:
                ord = Order.objects.filter(SalesPersonCode__in=SalesEmployeeCode, DocumentStatus="bost_Close")
                allord = OrderShow(ord)
                #print(allord)
			
            #{"SalesEmployeeCode":"2"}
            return Response({"message": "Success","status": 200,"data":allord})
            
            #return Response({"message": "Success","status": 201,"data":[{"emp":SalesEmployeeCode}]})
        else:
            return Response({"message": "Unsuccess","status": 201,"data":[{"error":"SalesEmployeeCode?"}]})
    else:
        return Response({"message": "Unsuccess","status": 201,"data":[{"error":"SalesEmployeeCode?"}]})
	
#Order All API
@api_view(["POST"])
def all_filter(request):
    json_data = request.data
    
    # if "U_OPPID" in json_data:
        # if json_data['U_OPPID'] !='':
            
            # quot_obj = Order.objects.filter(U_OPPID=json_data['U_OPPID']).order_by("-id")
            # if len(quot_obj) ==0:
                # return Response({"message": "Not Available","status": 201,"data":[]})
            # else:
                
                # allqt = OrderShow(quot_obj)
                        
            # return Response({"message": "Success","status": 200,"data":allqt})
                
    
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
                SalesPersonID = [json_data['SalesPersonCode']]
            
            print(SalesPersonID)
            
            for ke in json_data.keys():
                if ke =='U_FAV' :
                    print("yes filter")
                    if json_data['U_FAV'] !='':
                        quot_obj = Order.objects.filter(SalesPersonCode__in=SalesPersonID, U_FAV=json_data['U_FAV']).order_by("-id")
                        if len(quot_obj) ==0:
                            return Response({"message": "Not Available","status": 201,"data":[]})
                        else:
                            allqt = OrderShow(quot_obj)
                            return Response({"message": "Success","status": 200,"data":allqt})
                # elif ke =='U_TYPE' :
                    # if json_data['U_TYPE'] !='':
                        # quot_obj = Order.objects.filter(SalesPersonCode__in=SalesPersonID, U_TYPE=json_data['U_TYPE']).order_by("-id")
                        # if len(quot_obj) ==0:
                            # return Response({"message": "Not Available","status": 201,"data":[]})
                        # else:
                            # quot_json = OrderSerializer(quot_obj, many=True)
                            # return Response({"message": "Success","status": 200,"data":quot_json.data})
                # elif ke =='Status' :
                    # if json_data['Status'] !='':
                        # quot_obj = Order.objects.filter(SalesPersonCode__in=SalesPersonID, Status=json_data['Status']).order_by("-id")
                        # if len(quot_obj) ==0:
                            # return Response({"message": "Not Available","status": 201,"data":[]})
                        # else:
                            # quot_json = OrderSerializer(quot_obj, many=True)
                            # return Response({"message": "Success","status": 200,"data":quot_json.data})
                
                else:
                    print("no filter")
                    # qt = Order.objects.filter(SalesPersonCode__in=SalesPersonID).order_by("-id")
                    # quot_json = OrderSerializer(quot_obj, many=True)
                    # return Response({"message": "Success","status": 200,"data":quot_json.data})
                    quot_obj = Order.objects.filter(SalesPersonCode__in=SalesPersonID).order_by("-id")
                    allqt = OrderShow(quot_obj)
                        
                    return Response({"message": "Success","status": 200,"data":allqt})
            
        else:
            return Response({"message": "Unsuccess","status": 201,"data":[{"error":"SalesPersonCode?"}]})
    else:
        print("no")
        return Response({"message": "Unsuccess","status": 201,"data":[{"error":"SalesPersonCode?"}]})



#Order All API
@api_view(["POST"])
def all_filter_page(request):
    json_data = request.data
    PageNo = json_data['PageNo']     #### 10/02/2023 update
    try:
        MaxItem = json_data['MaxItem']
    except:
        MaxItem = 10
    if MaxItem!="All":
        endWith = (PageNo * MaxItem)
        startWith = (endWith - MaxItem)
    # if "U_OPPID" in json_data:
        # if json_data['U_OPPID'] !='':
            
            # quot_obj = Order.objects.filter(U_OPPID=json_data['U_OPPID']).order_by("-id")
            # if len(quot_obj) ==0:
                # return Response({"message": "Not Available","status": 201,"data":[]})
            # else:
                
                # allqt = OrderShow(quot_obj)
                        
            # return Response({"message": "Success","status": 200,"data":allqt})
                
    
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
                SalesPersonID = [json_data['SalesPersonCode']]
            
            print(SalesPersonID)
            
            for ke in json_data.keys():
                if ke =='U_FAV' :
                    print("yes filter")
                    if json_data['U_FAV'] !='':
                        quot_obj = Order.objects.filter(SalesPersonCode__in=SalesPersonID, U_FAV=json_data['U_FAV']).order_by("-id")
                        if len(quot_obj) ==0:
                            return Response({"message": "Not Available","status": 201,"data":[]})
                        else:
                            allqt = OrderShow(quot_obj)
                            return Response({"message": "Success","status": 200,"data":allqt})
                # elif ke =='U_TYPE' :
                    # if json_data['U_TYPE'] !='':
                        # quot_obj = Order.objects.filter(SalesPersonCode__in=SalesPersonID, U_TYPE=json_data['U_TYPE']).order_by("-id")
                        # if len(quot_obj) ==0:
                            # return Response({"message": "Not Available","status": 201,"data":[]})
                        # else:
                            # quot_json = OrderSerializer(quot_obj, many=True)
                            # return Response({"message": "Success","status": 200,"data":quot_json.data})
                # elif ke =='Status' :
                    # if json_data['Status'] !='':
                        # quot_obj = Order.objects.filter(SalesPersonCode__in=SalesPersonID, Status=json_data['Status']).order_by("-id")
                        # if len(quot_obj) ==0:
                            # return Response({"message": "Not Available","status": 201,"data":[]})
                        # else:
                            # quot_json = OrderSerializer(quot_obj, many=True)
                            # return Response({"message": "Success","status": 200,"data":quot_json.data})
                
                else:
                    print("no filter")
                    # qt = Order.objects.filter(SalesPersonCode__in=SalesPersonID).order_by("-id")
                    # quot_json = OrderSerializer(quot_obj, many=True)
                    # return Response({"message": "Success","status": 200,"data":quot_json.data})
                    if MaxItem!="All":
                        quot_obj = Order.objects.filter(SalesPersonCode__in=SalesPersonID).order_by("-id")
                        total_count = quot_obj.count()
                        quot_obj = quot_obj[startWith:endWith]
                    else:
                        quot_obj = Order.objects.filter(SalesPersonCode__in=SalesPersonID).order_by("-id")
                        total_count = quot_obj.count()
                    allqt = OrderShowPage(quot_obj)
                        
                    return Response({"message": "Success","status": 200,"data":allqt, "extra":{"total_count":total_count}})
            
        else:
            return Response({"message": "Unsuccess","status": 201,"data":[{"error":"SalesPersonCode?"}]})
    else:
        print("no")
        return Response({"message": "Unsuccess","status": 201,"data":[{"error":"SalesPersonCode?"}]})


def OrderShowPage(Orders_obj):
    allqt = [];
    for qt in Orders_obj:
        order_obj = {}
        order_obj["id"] = qt.id
        order_obj["TaxDate"] = qt.TaxDate
        order_obj["DocDueDate"] = qt.DocDueDate
        order_obj["CardCode"] = qt.CardCode
        order_obj["CardName"] = qt.CardName
        order_obj["DocumentStatus"] = qt.DocumentStatus
        order_obj["CancelStatus"] = qt.CancelStatus
        order_obj["FinalStatus"] = qt.FinalStatus
        order_obj["DocEntry"] = qt.DocEntry
        order_obj["ReadLevel1"] = qt.ReadLevel1
        order_obj["ReadLevel2"] = qt.ReadLevel2
        order_obj["ReadLevel3"] = qt.ReadLevel3
        order_obj["U_OPPID"] = qt.U_OPPID
        if OrderHistory.objects.filter(OrderID=qt.id).exists():
            order_obj["NetTotal"] = OrderHistory.objects.filter(OrderID=qt.id).last().NetTotal
        else:
            order_obj["NetTotal"] = qt.NetTotal
        order_obj["DocDate"] = qt.DocDate
        order_obj["amendment_status"] = qt.amendment_status
        order_obj["amendment_action"] = qt.amendment_action
        try:
            if Attachment.objects.filter(LinkID = qt.id, LinkType="Order").exists():
                attachment_dls = Attachment.objects.filter(LinkID = qt.id, LinkType="Order")
                attachment_json = AttachmentSerializer(attachment_dls, many=True)
                order_obj['Attach'] = attachment_json.data
            else:
                order_obj['Attach'] = []
        except Exception as e:
            return Response({"message": str(e),"status": 201,"data":[]})
        allqt.append(order_obj)
        
    return allqt








#Order All API
@api_view(["GET"])
def all(request):
    Orders_obj = Order.objects.all().order_by("-id")
    allqt = OrderShow(Orders_obj)
    return Response({"message": "Success","status": 200,"data":allqt})

# #Order One API
# @api_view(["POST"])
# def one(request):
#     id=request.data['id']
    
#     Orders_obj = Order.objects.filter(id=id)
    
#     allqt = OrderShow(Orders_obj)
#     return Response({"message": "Success","status": 200,"data":allqt})



#Order One API
@api_view(["POST"])
def one(request):
    id=request.data['id']
    
    Orders_obj = Order.objects.filter(id=id)
    
    allqt = OrderShow(Orders_obj)
    all_history = OrderHistoryShow(id)
    return Response({"message": "Success","status": 200,"data":allqt, "extra":{"history":all_history}})

def OrderHistoryShow(oid):
    history = []
    if OrderHistory.objects.filter(OrderID=oid).exists():
        history_data = OrderHistory.objects.filter(OrderID=oid).last()
        orderhistory = OrderHistorySerializer(history_data).data
        print("ttttttttttttt",orderhistory)
        if DocumentLinesHistory.objects.filter(orderhistory_id=history_data.id).exists():
            documentlinehistory_data = DocumentLinesHistory.objects.filter(orderhistory_id=history_data.id)
            orderhistory["DocumentLines"] = DocumentLinesHistorySerializer(documentlinehistory_data, many=True).data
            addonlist = []
            for data in documentlinehistory_data:
                if AddOnDocumentLinesHistory.objects.filter(documentlineshistory_id=data.id).exists():
                    addondata = AddOnDocumentLinesHistory.objects.filter(documentlineshistory_id=data.id)
                    for obj in addondata:
                        add_data = AddOnDocumentLinesHistorySerializer(obj).data
                        addonlist.append(add_data)
            orderhistory["AddOnDocumentLines"] = addonlist
        else:
            orderhistory["DocumentLines"] = []
            orderhistory["AddOnDocumentLines"] = []
        history.append(orderhistory)
    return history







#Order delete
@api_view(['POST'])
def cancel(request):
    fetchid=request.data['DocEntry']
    try:
        odr=Order.objects.get(DocEntry=fetchid)
        odr.DocumentStatus='bost_Close'
        odr.CancelStatus='csYes'
        odr.save()            
        if settings.SAP==True:    
            try:
                r = requests.post(settings.BASEURL+'/Login', data=json.dumps(settings.SAPDB), verify=False)
                token = json.loads(r.text)['SessionId']
                print(token)
                res = requests.post(settings.BASEURL+'/Orders('+fetchid+')/Cancel', cookies=r.cookies, verify=False)
                return Response({"message":"successful","status":200,"data":[]})
            except:
                return Response({"message":"successful","status":200,"data":[]})        
        else:
            return Response({"message":"successful","status":200,"data":[]})        
    except:
         return Response({"message":"Id wrong","status":201,"data":[]})

#update delivery
@api_view(['POST'])
def delivery_update(request):
   id = request.data['id']
   DelStatus = request.data['DelStatus']
   Obj = Order.objects.get(pk=id)
   Obj.DelStatus = DelStatus
   Obj.save()
   return Response({"message":"successful", "status":200, "data":[]})
   
#added by millan on 06-09-2022

#addendum create api
@api_view(['POST'])   
def addendumcreate(request):
    try:
        if request.data['OrderID'] == "":
            return Response({"message":"Order Id Can't be Empty","status":201,"data":[]})
        elif request.data['Date'] == "":
            return Response({"message":"Date Can't be Empty","status":201,"data":[]})
        elif request.data['Time'] == "":
            return Response({"message":"Time Can't be Empty","status":201,"data":[]})
        elif request.data['Attachments'] == "":
            return Response({"message":"Attachments Can't be Empty","status":201,"data":[]})
        else:
            OrderID = request.data['OrderID']
            Date = request.data['Date']
            Time = request.data['Time']
            Attachments = request.data['Attachments']
            
            attachmentsImage_url = ""
            if Attachments:
                target ='./bridge/static/image/addendumorder'
                os.makedirs(target, exist_ok=True)
                fss = FileSystemStorage()
                file = fss.save(target+"/"+Attachments.name, Attachments)
                productImage_url = fss.url(file)
                attachmentsImage_url = productImage_url.replace('/bridge', '')
            print(attachmentsImage_url)
            
            model = AddendumRequest(OrderID=OrderID, Date=Date, Time=Time, Attachments=attachmentsImage_url)
            model.save()

            addendumId = AddendumRequest.objects.latest('id')
            print(addendumId)
            
            return Response({"message":"success","status":200,"data":[]})
        
    except Exception as e:
        return Response({"message":str(e),"status":201,"data":[]})
        
#addendum All API 
@api_view(["POST"])
def addendumall(request):
    try:
        fetchid = request.data['OrderID']
        if AddendumRequest.objects.filter(OrderID=fetchid).exists():
            Addendum_obj = AddendumRequest.objects.filter(OrderID=fetchid)
            addn_obj = AddendumSerializer(Addendum_obj, many=True)
            finalAddendum = json.loads(json.dumps(addn_obj.data))
            #print(finalAddendum)
            return Response({"message": "Success","status": 200,"data":finalAddendum})
        else:
            return Response({"message": "Enter a Valid OrderID","status": 201,"data":[]})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})



# #order pending for approval
# @api_view(["POST"])
# def remarksHistory(request):
#     try:
#         qtid = request.data['id']
#         allRemarks = []
#         if OrderStatusRemarks.objects.filter(OrderID = qtid).exists():
#             remarkObj = OrderStatusRemarks.objects.filter(OrderID = qtid)
#             print(remarkObj)
#             # remarkJson = QuotStatusRemarksSerializer(remarkObj, many=True)
#             for obj in remarkObj:
#                 SalesEmployeeCode = obj.SalesEmployeeCode
#                 remarkJson = OrderStatusRemarksSerializer(obj)
#                 remarkData = json.loads(json.dumps(remarkJson.data))

#                 if Employee.objects.filter(SalesEmployeeCode = SalesEmployeeCode).exists():
#                     empObj = Employee.objects.filter(SalesEmployeeCode = SalesEmployeeCode).values_list('firstName', flat=True)[0]
#                     remarkData['EmployeeName'] = str(empObj)
#                 else:
#                     remarkData['EmployeeName'] = ""

#                 allRemarks.append(remarkData)
#         else:
#             print('nodata')
#         return Response({"message":"Success","status":200,"data":allRemarks}) 
#     except Exception as e:
#         return Response({"message":str(e),"status":201,"data":[]})        






#Order Update API
@api_view(['POST'])
def approve(request):
    SalesEmployeeCode = request.data['SalesEmployeeCode']
    qtid = request.data['id']
    FinalStatus = request.data['FinalStatus']
    #SalesEmployeeCode=2 #salesman
    #SalesEmployeeCode=1 #manager
    #SalesEmployeeCode=38 #admin
    try:
        # UPDATE `Order_Order` SET `APPROVEID_id`= NULL, `FinalStatus`="", `Level3_id` = NULL, `Level2_id` = NULL, `Level1_id` = NULL, `Level3Status` = "", `Level2Status` = "", `Level1Status` = "" WHERE `Order_Order`.`id` = 30;
        level = tree(SalesEmployeeCode) 
        print("Level: "+level)
        slave_obj =  AppSlave.objects.filter(Level=level)
        min = slave_obj[0].Min
        max = slave_obj[0].Max

        print(str(min)+"-"+str(max))

        qt =  Order.objects.get(pk=qtid)
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
            #SELECT * FROM `Order_appslave` WHERE Min <= 11 and Max >=11;
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
        return Response({"message":"Success","status":201,"data":[]})

    except Exception as e:
        return Response({"message":str(e),"status":201,"data":[{"Error":str(e)}]})

#Order pending for approval
@api_view(["POST"])
def pending(request):
    SalesEmployeeCode = request.data['SalesEmployeeCode']
    level = tree(SalesEmployeeCode)
    print(level)
    if int(level) == 3:
        quot_obj = Order.objects.filter(Level3_id=SalesEmployeeCode,Level3Status="Pending").order_by("-id")
    elif int(level) == 2:
        quot_obj = Order.objects.filter(Level2_id=SalesEmployeeCode,Level2Status="Pending").order_by("-id")
    elif int(level) == 1:
        quot_obj = Order.objects.filter(Level1_id=SalesEmployeeCode,Level1Status="Pending").order_by("-id")
    print(quot_obj)

    allqt = OrderShow(quot_obj)                        
    return Response({"message": "Success","status": 200,"data":allqt})

#Order pending for approval
@api_view(["POST"])
def approved(request):
    SalesEmployeeCode = request.data['SalesEmployeeCode']
    level = tree(SalesEmployeeCode)
    print(level)
    if int(level) == 3:
        quot_obj = Order.objects.filter(Level3_id=SalesEmployeeCode,Level3Status="Approved").order_by("-id")
    elif int(level) == 2:
        quot_obj = Order.objects.filter(Level2_id=SalesEmployeeCode,Level2Status="Approved").order_by("-id")
    elif int(level) == 1:
        quot_obj = Order.objects.filter(FinalStatus="Approved").order_by("-id")
    print(quot_obj)

    allqt = OrderShow(quot_obj)                        
    return Response({"message": "Success","status": 200,"data":allqt})


#TapType Create API
@api_view(['POST'])
def taptype_create(request):
    Name = request.data['Name']    
    if TapType.objects.filter(Name=Name).exists():        
        return Response({"message":"Already exist","status":409,"data":[]})
    else:        
        try:
            CreatedDate = request.data['CreatedDate']
            CreatedTime = request.data['CreatedTime']
            model=TapType(Name = Name, CreatedDate = CreatedDate, CreatedTime = CreatedTime)            
            model.save()            
            sc = TapType.objects.latest('id')
            return Response({"message":"successful","status":200,"data":[{"id":sc.id}]})
        except Exception as e:
            return Response({"message":"Can not create","status":"201","data":[{"Error":str(e)}]})        

#Type Update API
@api_view(['POST'])
def taptype_update(request):
    fetchid = request.data['id']
    try:
        model = TapType.objects.get(pk = fetchid)
        model.Name  = request.data['Name']
        model.CreatedDate  = request.data['CreatedDate']
        model.CreatedTime  = request.data['CreatedTime']
        model.save()
        return Response({"message":"successful","status":200,"data":[request.data]})
    except:
        return Response({"message":"ID Wrong","status":201,"data":[]})


#TapType All API
@api_view(["GET"])
def taptype_all(request):
    TapType_obj = TapType.objects.all()        
    TapType_json = TapTypeSerializer(TapType_obj, many=True)
    return Response({"message": "Success","status": 200,"data":TapType_json.data})

#TapTypeType One API
@api_view(["POST"])
def taptype_one(request):
    fetch = request.data['id']
    TapType_obj = TapType.objects.filter(pk=fetch)        
    TapType_json = TapTypeSerializer(TapType_obj, many=True)
    return Response({"message": "Success","status": 200,"data":TapType_json.data})


#TapType delete
@api_view(['POST'])
def taptype_delete(request):
    fetchid=request.data['id']
    try:
        fetchdata=TapType.objects.filter(pk=fetchid).delete()
        return Response({"message":"successful","status":"200","data":[]})        
    except Exception as e:
         return Response({"message":str(e),"status":"201","data":[]})

#MachineType Create API
@api_view(['POST'])
def machinetype_create(request):
    Name = request.data['Name']    
    if MachineType.objects.filter(Name=Name).exists():        
        return Response({"message":"Already exist","status":409,"data":[]})
    else:        
        try:
            CreatedDate = request.data['CreatedDate']
            CreatedTime = request.data['CreatedTime']
            model=MachineType(Name = Name, CreatedDate = CreatedDate, CreatedTime = CreatedTime)            
            model.save()            
            sc = MachineType.objects.latest('id')
            return Response({"message":"successful","status":200,"data":[{"id":sc.id}]})
        except Exception as e:
            return Response({"message":"Can not create","status":"201","data":[{"Error":str(e)}]})        

#Type Update API
@api_view(['POST'])
def machinetype_update(request):
    fetchid = request.data['id']
    try:
        model = MachineType.objects.get(pk = fetchid)
        model.Name  = request.data['Name']
        model.CreatedDate  = request.data['CreatedDate']
        model.CreatedTime  = request.data['CreatedTime']
        model.save()
        return Response({"message":"successful","status":200,"data":[request.data]})
    except:
        return Response({"message":"ID Wrong","status":201,"data":[]})


#MachineType All API
@api_view(["GET"])
def machinetype_all(request):
    MachineType_obj = MachineType.objects.all()        
    MachineType_json = MachineTypeSerializer(MachineType_obj, many=True)
    return Response({"message": "Success","status": 200,"data":MachineType_json.data})

#MachineTypeType One API
@api_view(["POST"])
def machinetype_one(request):
    fetch = request.data['id']
    MachineType_obj = MachineType.objects.filter(pk=fetch)        
    MachineType_json = MachineTypeSerializer(MachineType_obj, many=True)
    return Response({"message": "Success","status": 200,"data":MachineType_json.data})


#MachineType delete
@api_view(['POST'])
def machinetype_delete(request):
    fetchid=request.data['id']
    try:
        fetchdata=MachineType.objects.filter(pk=fetchid).delete()
        return Response({"message":"successful","status":"200","data":[]})        
    except Exception as e:
         return Response({"message":str(e),"status":"201","data":[]})


#Order Read
@api_view(['POST'])
def read(request):
    try:
        fetchid=request.data['id']
        SalesPersonCode = request.data['SalesPersonCode']
        
        if Order.objects.filter(pk=fetchid).exists():
            model =  Order.objects.get(pk=fetchid)
            print(model)
            level = tree(SalesPersonCode) 
            if int(level) == 1:
                model.ReadLevel1 = SalesPersonCode
            elif int(level) == 2:
                model.ReadLevel2 = SalesPersonCode
            elif int(level) == 3:
                model.ReadLevel3 = SalesPersonCode
            else:
                print("self")            
            model.save()
            return Response({"message":"successful","status":"200","data":[]})
        else:
            return Response({"message":"Order not exists: ", "status":"201","data":[]})
    except Exception as e:
         return Response({"message":str(e),"status":"201","data":[]})

#all pos
@api_view(['GET'])
def all_po_no(request):
    try:
        ordObj = Order.objects.all().values('id', 'PoNo', 'DatePO')
        ordJson = OrderSerializer(ordObj, many=True)
        return Response({"message":"successful","status":"200","data":ordJson.data})
    except Exception as e:
         return Response({"message":str(e),"status":"201","data":[]})
