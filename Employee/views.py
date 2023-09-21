from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from Item.serializers import *
from Category.serializers import *
from Order.serializers import *
from Opportunity.serializers import OpportunitySerializer
from .serializers import *
from rest_framework.response import Response
from rest_framework import serializers
from django.contrib import messages
from Quotation.models import Quotation, AppSlave
from Invoice.models import Invoice
from Order.models import Order, DocumentLines
from Opportunity.models import Opportunity
from BusinessPartner.models import BusinessPartner
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .forms import EmployeeForm
from .models import *
from .models import Department as EmpDepartment
from .serializers import DepartmentSerializer as EmpDepartmentSerializer
from Activity.models import Activity
from Lead.models import Lead
from Item.models import Item
from Category.models import *
from Campaign.models import *
from Tender.models import Tender
from Notification.models import Notification
import requests
import json

from django.conf import settings

from django.db.models import Sum, F #added by millan on 05-September-2022

from datetime import date, timedelta
from collections import Counter

from global_fun import *

from pytz import timezone
from datetime import datetime as dt

tdate = dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d')
yearmonth = dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m')
time = dt.now(timezone("Asia/Kolkata")).strftime('%H:%M %p')


# Create your views here.
@api_view(["GET"])
def top5itembyamount(request):
    #added by millan on 05-September-2022
    try:
        top2bp = DocumentLines.objects.values('ItemCode').annotate(Total = Sum(F('Quantity')*F('UnitPrice'))).order_by('-Total')[:5]
    
        top5=[]

        for od in top2bp:
            top5dt = DocumentLines.objects.filter(ItemCode = od['ItemCode']).values('ItemDescription')
            for desc in top5dt:
                print(desc)
            top5.append({"ItemCode":od['ItemCode'], "ItemName":desc['ItemDescription'], "Total":od['Total']})
        
        return Response({"message": "Success","status": 200,"data":top5}) #added by millan on 05-September-2022
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})

@api_view(["GET"])
def top5bp(request):
    try:
        #added by millan on 05-September-2022
        top2bp = Order.objects.values('CardCode').annotate(Total = Sum(F('DocTotal'))).order_by('-Total')[:5]
        print(top2bp)
        top5=[]
        for od in top2bp:
            try:
                cd = BusinessPartner.objects.filter(CardCode = od['CardCode']).values('CardName')
                for cName in cd:
                    print(cName)
                top5.append({"CardCode":od['CardCode'], "CardName":cName['CardName'], 'Total':od['Total']})
            except Exception as e:
                top5.append({"CardCode":od['CardCode'], "CardName":od['CardCode'], 'Total':od['Total']})
            
        return Response({"message": "Success","status": 200,"data":top5})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})


@api_view(["POST"])
def opportunity_bystage(request):

    json_data = request.data

    if "SalesEmployeeCode" in json_data:
        print("yes")

        if json_data['SalesEmployeeCode'] != "":
            SalesEmployeeCode = json_data['SalesEmployeeCode']

            emp_obj = Employee.objects.get(SalesEmployeeCode=SalesEmployeeCode)
            if emp_obj.role == 'admin' or emp_obj.role == 'ceo':
                emps = Employee.objects.filter(SalesEmployeeCode__gt=0)
                SalesEmployeeCode = []
                for emp in emps:
                    SalesEmployeeCode.append(emp.SalesEmployeeCode)
            elif emp_obj.role == 'manager':
                # .values('id', 'SalesEmployeeCode')
                emps = Employee.objects.filter(reportingTo=SalesEmployeeCode)
                SalesEmployeeCode = [SalesEmployeeCode]
                for emp in emps:
                    SalesEmployeeCode.append(emp.SalesEmployeeCode)
            else:
                SalesEmployeeCode = [SalesEmployeeCode]
            print(SalesEmployeeCode)

            opp_Lead_count = Opportunity.objects.filter(
                SalesPerson__in=SalesEmployeeCode, CurrentStageName="Lead").count()
            opp_Need_count = Opportunity.objects.filter(
                SalesPerson__in=SalesEmployeeCode, CurrentStageName="Need Analysis").count()
            opp_Quotation_count = Opportunity.objects.filter(
                SalesPerson__in=SalesEmployeeCode, CurrentStageName="Quotation").count()
            opp_Negotiation_count = Opportunity.objects.filter(
                SalesPerson__in=SalesEmployeeCode, CurrentStageName="Negotiation").count()
            opp_Order_count = Opportunity.objects.filter(
                SalesPerson__in=SalesEmployeeCode, CurrentStageName="Order").count()

            opportunity_context = {
                "Lead": opp_Lead_count,
                "NeedAnalysis": opp_Need_count,
                "Quotation": opp_Quotation_count,
                "Negotiation": opp_Negotiation_count,
                "Order": opp_Order_count
            }

            return Response({"message": "Success", "status": 200, "data": [opportunity_context]})
        else:
            return Response({"message": "Unsuccess", "status": 201, "data": [{"error": "SalesEmployeeCode?"}]})
    else:
        return Response({"message": "Unsuccess", "status": 201, "data": [{"error": "SalesEmployeeCode?"}]})


@api_view(["POST"])
def analytics(request):

    json_data = request.data
    month = int(json_data['month'])

    if "SalesEmployeeCode" in json_data:
        print("yes")

        if json_data['SalesEmployeeCode'] != "":
            SalesEmployeeCode = json_data['SalesEmployeeCode']

            emp_obj = Employee.objects.get(SalesEmployeeCode=SalesEmployeeCode)
            if emp_obj.role == 'admin' or emp_obj.role == 'ceo':
                emps = Employee.objects.filter(SalesEmployeeCode__gt=0)
                SalesEmployeeCode = []
                for emp in emps:
                    SalesEmployeeCode.append(emp.SalesEmployeeCode)
            elif emp_obj.role == 'manager':
                # .values('id', 'SalesEmployeeCode')
                emps = Employee.objects.filter(reportingTo=SalesEmployeeCode)
                SalesEmployeeCode = [SalesEmployeeCode]
                for emp in emps:
                    SalesEmployeeCode.append(emp.SalesEmployeeCode)
            else:
                SalesEmployeeCode = [SalesEmployeeCode]
            print(SalesEmployeeCode)

            tgt_all = Target.objects.filter(SalesPersonCode__in=SalesEmployeeCode).exclude(
                monthYear=yearmonth).order_by("-monthYear")[:month]
            #{"month":"3", "SalesEmployeeCode":"3"}
            amount = sum(tgt_all.values_list('amount', flat=True))
            print(amount)
            #amount = "{:.2f}".format(amount)
            #print(amount)

            sale = sum(tgt_all.values_list('sale', flat=True))
            print(sale)

            sale_diff = sum(tgt_all.values_list('sale_diff', flat=True))
            print(sale_diff)

            notification = Notification.objects.filter(
                Emp=emp_obj.id, CreatedDate=tdate, Read=0).order_by("-id").count()
            print(notification)

            return Response({"message": "Success", "status": 200, "data": [{"notification": notification, "amount": amount, "sale": sale, "sale_diff": sale_diff}]})

            #return Response({"message": "Success","status": 201,"data":[{"emp":SalesEmployeeCode}]})
        else:
            return Response({"message": "Unsuccess", "status": 201, "data": [{"error": "SalesEmployeeCode?"}]})
    else:
        return Response({"message": "Unsuccess", "status": 201, "data": [{"error": "SalesEmployeeCode?"}]})


#Target Create API
@api_view(['POST'])
def target_create(request):
    try:
        TargetFor = request.data['TargetFor']
        amount = request.data['amount']
        monthYear = request.data['monthYear']
        qtr = request.data['qtr']
        department = request.data['department']

        SalesPersonCode = request.data['SalesPersonCode']
        reportingTo = request.data['reportingTo'].strip()
        CreatedDate = request.data['CreatedDate']
        if reportingTo == "":
            model = Target(TargetFor=TargetFor, amount=amount, monthYear=monthYear, qtr=qtr,
                           SalesPersonCode_id=SalesPersonCode, CreatedDate=CreatedDate, UpdatedDate=CreatedDate)
        else:
            model = Target(TargetFor=TargetFor, amount=amount, monthYear=monthYear, qtr=qtr, SalesPersonCode_id=SalesPersonCode,
                           reportingTo_id=reportingTo, CreatedDate=CreatedDate, UpdatedDate=CreatedDate)

        model = Target(TargetFor=TargetFor, amount=amount, monthYear=monthYear, qtr=qtr, SalesPersonCode_id=SalesPersonCode,
                       reportingTo_id=reportingTo, CreatedDate=CreatedDate, UpdatedDate=CreatedDate)
        model.save()

        tgt = Target.objects.latest('id')
        print(tgt.id)
        return Response({"message": "Success", "status": "200", "data": []})
    except Exception as e:
        return Response({"message": str(e), "status": "201", "data": [{"Error": str(e)}]})

# most order item in last 30 days


@api_view(['GET'])
def movingitems(request):
    try:
        fastMovingdate = date.today() - timedelta(days=15)
        slowMovingdate = date.today() - timedelta(days=30)

        print(fastMovingdate)
        print(slowMovingdate)

        itemCodeList = []
        fastMovingItemList = []
        # ----------------------------------------------------------------------------
        # ------------------------- Fast Moving Items --------------------------------
        # ----------------------------------------------------------------------------
        fastMovingOrder_obj = Order.objects.filter(
            CreateDate__gte=fastMovingdate)
        fastMovingItemCodeArr = []
        for order in fastMovingOrder_obj:
            order_id = order.id
            docLineObj = DocumentLines.objects.filter(OrderID=order_id)
            for docLine in docLineObj:
                # print(docLine)
                # docJason = DocumentLinesSerializer(docLine);
                itemCode = docLine.ItemCode
                itemObj = Item.objects.get(ItemCode=itemCode)
                itemJson = ItemSerializer(itemObj)

                if itemCode not in fastMovingItemCodeArr:
                    fastMovingItemList.append(itemJson.data)
                    fastMovingItemCodeArr.append(itemCode)
                    itemCodeList.append(itemCode)

        FastItemsCount = len(fastMovingItemCodeArr)

        # ----------------------------------------------------------------------------
        # ------------------------- Slow Moving Itmes --------------------------------
        # ----------------------------------------------------------------------------
        slowMovingdate_obj = Order.objects.filter(
            CreateDate__lte=fastMovingdate, CreateDate__gte=slowMovingdate)
        slowMovingItemCodeArr = []
        slowMovingItemList = []
        for order in slowMovingdate_obj:
            order_id = order.id
            docLineObj = DocumentLines.objects.filter(OrderID=order_id)
            for docLine in docLineObj:
                # docJason = DocumentLinesSerializer(docLine);
                itemCode = docLine.ItemCode
                itemObj = Item.objects.get(ItemCode=itemCode)
                itemJson = ItemSerializer(itemObj)
                if itemCode not in fastMovingItemCodeArr:
                    slowMovingItemList.append(itemJson.data)
                    slowMovingItemCodeArr.append(itemCode)
                    itemCodeList.append(itemCode)

        SlowItemsCount = len(slowMovingItemCodeArr)

        dictItem = set(itemCodeList)
        # notMovingItemCount = Item.objects.all().exclude(ItemCode__in = dictItem).count()
        notMovingItemObj = Item.objects.all().exclude(ItemCode__in=dictItem)
        notMovingItemJson = ItemSerializer(notMovingItemObj, many=True)
        notMovingItemCount = len(notMovingItemObj)
        context = {
            "FastMovingItemsList": fastMovingItemList,
            "FastItemsCount": FastItemsCount,
            "SlowMovingItemsList": slowMovingItemList,
            "SlowItemsCount": SlowItemsCount,
            "NotMovingItemsList": notMovingItemJson.data,
            "NotMovingItemsCount": notMovingItemCount
        }

        print(FastItemsCount)
        print(SlowItemsCount)
        print(notMovingItemCount)

        return Response({"message": "successful", "status": 200, "data": [context]})
    except Exception as e:
        return Response({"message": "Error", "status": 201, "data": [str(e)]})

# most order item in last 30 days


@api_view(['GET'])
def movingitems_count(request):
    try:
        fastMovingdate = date.today() - timedelta(days=15)
        slowMovingdate = date.today() - timedelta(days=30)
        itemCodeList = []
        # --------------------------------------------------------------------------
        # ------------------------- Fast Moving Items ------------------------------
        # --------------------------------------------------------------------------
        fastMovingOrder_obj = Order.objects.filter(
            CreateDate__gte=fastMovingdate)
        fastMovingItemCodeArr = []
        for order in fastMovingOrder_obj:
            order_id = order.id
            docLineObj = DocumentLines.objects.filter(OrderID=order_id)
            for docLine in docLineObj:
                itemCode = docLine.ItemCode
                if itemCode not in fastMovingItemCodeArr:
                    fastMovingItemCodeArr.append(itemCode)
                    itemCodeList.append(itemCode)

        FastItemsCount = len(fastMovingItemCodeArr)

        # ----------------------------------------------------------------------------
        # ------------------------- Slow Moving Itmes --------------------------------
        # ----------------------------------------------------------------------------
        slowMovingdate_obj = Order.objects.filter(
            CreateDate__lte=fastMovingdate, CreateDate__gte=slowMovingdate)
        slowMovingItemCodeArr = []
        # slowMovingItemList = []
        for order in slowMovingdate_obj:
            order_id = order.id
            docLineObj = DocumentLines.objects.filter(OrderID=order_id)
            for docLine in docLineObj:
                itemCode = docLine.ItemCode
                if itemCode not in fastMovingItemCodeArr:
                    slowMovingItemCodeArr.append(itemCode)
                    itemCodeList.append(itemCode)

        SlowItemsCount = len(slowMovingItemCodeArr)
        dictItem = set(itemCodeList)
        notMovingItemCount = Item.objects.all().exclude(ItemCode__in=dictItem).count()

        context = {
            # "FastMovingItemsList": fastMovingItemList,
            "FastItemsCount": FastItemsCount,
            # "SlowMovingItemsList": slowMovingItemList,
            "SlowItemsCount": SlowItemsCount,
            "NotMovingItemsCount": notMovingItemCount
            # "NotMovingItemsList": notMovingItemJson.data
        }

        return Response({"message": "successful", "status": 200, "data": [context]})
    except Exception as e:
        return Response({"message": str(e), "status": 201, "data": [str(e)]})


@api_view(["POST"])
def dashboard(request):

    json_data = request.data

    if "SalesEmployeeCode" in json_data:
        print("yes")
        if json_data['SalesEmployeeCode'] != "":
            SalesEmployeeCode = json_data['SalesEmployeeCode']
            if Employee.objects.filter(SalesEmployeeCode=SalesEmployeeCode).exists():
                emp_obj = Employee.objects.get(SalesEmployeeCode=SalesEmployeeCode)
                if emp_obj.role == 'admin' or emp_obj.role == 'ceo':
                    #emps = Employee.objects.filter(SalesEmployeeCode__gt=0)
                    emps = Employee.objects.all()
                    SalesEmployeeCode = []
                    for emp in emps:
                        SalesEmployeeCode.append(emp.SalesEmployeeCode)
                elif emp_obj.role == 'manager':
                    # .values('id', 'SalesEmployeeCode')
                    emps = Employee.objects.filter(reportingTo=SalesEmployeeCode)
                    SalesEmployeeCode = [SalesEmployeeCode]
                    for emp in emps:
                        SalesEmployeeCode.append(emp.SalesEmployeeCode)
                else:
                    SalesEmployeeCode = [SalesEmployeeCode]
                    # emps = Employee.objects.filter(reportingTo=emp_obj.reportingTo)#.values('id', 'SalesEmployeeCode')
                    # SalesEmployeeCode=[]
                    # for emp in emps:
                    # SalesEmployeeCode.append(emp.SalesEmployeeCode)

                print(SalesEmployeeCode)

                emp_ids = Employee.objects.filter(
                    SalesEmployeeCode__in=SalesEmployeeCode).values_list('id', flat=True)
                print(emp_ids)
                #{"SalesEmployeeCode":4}

                lead_all = Lead.objects.filter(assignedTo__in=emp_ids).count()
                print(lead_all)
                from django.db.models import Q

                lead_prod = Lead.objects.filter(
                    assignedTo__in=emp_ids).filter(~Q(intProdCat="")).count()
                print("lead_prod")
                print(lead_prod)

                lead_proj = Lead.objects.filter(
                    assignedTo__in=emp_ids).filter(~Q(intProjCat="")).count()
                print("lead_proj")
                print(lead_proj)

                opp_all = Opportunity.objects.filter(
                    SalesPerson__in=SalesEmployeeCode).count()
                #print(opp_all)

                quot_all = Quotation.objects.filter(
                    SalesPersonCode__in=SalesEmployeeCode).count()
                #print(quot_all)

                ord_all = Order.objects.filter(
                    SalesPersonCode__in=SalesEmployeeCode).count()
                #print(ord_all)

                inv_all = Invoice.objects.filter(
                    SalesPersonCode__in=SalesEmployeeCode).count()
                #print(inv_all)

                tnd_all = Tender.objects.filter(
                    SalesPersonCode__in=SalesEmployeeCode).count()
                print(tnd_all)

                #bp_all = BusinessPartner.objects.filter(SalesPersonCode__in=SalesEmployeeCode).count()
                bp_all = BusinessPartner.objects.all().count()
                #print(bp_all)

                tgt_all = Target.objects.filter(
                    SalesPersonCode__in=SalesEmployeeCode, monthYear=yearmonth)

                amount = sum(tgt_all.values_list('amount', flat=True))
                print(amount)
                #amount = "{:.2f}".format(amount)
                #print(amount)

                sale = sum(tgt_all.values_list('sale', flat=True))
                print(sale)

                sale_diff = sum(tgt_all.values_list('sale_diff', flat=True))
                print(sale_diff)

                notification = Notification.objects.filter(
                    Emp=emp_obj.id, CreatedDate=tdate, Read=0).order_by("-id").count()
                print(notification)

                ord_over = Order.objects.filter(
                    SalesPersonCode__in=SalesEmployeeCode, DocumentStatus="bost_Open", DocDueDate__lt=tdate).count()
                print(ord_over)
                print(tdate)

                ord_open = Order.objects.filter(
                    SalesPersonCode__in=SalesEmployeeCode, DocumentStatus="bost_Open", DocDueDate__gte=tdate).count()
                print(ord_open)

                ord_close = Order.objects.filter(
                    SalesPersonCode__in=SalesEmployeeCode, DocumentStatus="bost_Close").count()
                print(ord_close)

                campset_all = CampaignSet.objects.filter(
                    CampaignSetOwner__in=SalesEmployeeCode).count()
                print(campset_all)

                #{"SalesEmployeeCode":"2"}
                return Response({"message": "Success", "status": 200, "data": [{"notification": notification, "amount": amount, "sale": sale, "sale_diff": sale_diff, "Opportunity": opp_all, "Quotation": quot_all, "Order": ord_all, "Invoice": inv_all, "Tender": tnd_all, "Customer": bp_all, "Leads": lead_all, "Leads_Product": lead_prod, "Leads_Project": lead_proj, "Over": ord_over, "Open": ord_open, "Close": ord_close, "CampaignSet": campset_all}]})
            else:
                return Response({"message": "Unsuccess", "status": 201, "data": [{"error": "Not Found"}]})
            #return Response({"message": "Success","status": 201,"data":[{"emp":SalesEmployeeCode}]})
        else:
            return Response({"message": "Unsuccess", "status": 201, "data": [{"error": "SalesEmployeeCode?"}]})
    else:
        return Response({"message": "Unsuccess", "status": 201, "data": [{"error": "SalesEmployeeCode?"}]})


@api_view(["POST"])
def invoice_counter(request):
    json_data = request.data

    if "SalesEmployeeCode" in json_data:
        print("yes")

        if json_data['SalesEmployeeCode'] != "":
            SalesEmployeeCode = json_data['SalesEmployeeCode']

            emp_obj = Employee.objects.get(SalesEmployeeCode=SalesEmployeeCode)
            if emp_obj.role == 'admin' or emp_obj.role == 'ceo':
                emps = Employee.objects.filter(SalesEmployeeCode__gt=0)
                SalesEmployeeCode = []
                for emp in emps:
                    SalesEmployeeCode.append(str(emp.SalesEmployeeCode))
            elif emp_obj.role == 'manager':
                # .values('id', 'SalesEmployeeCode')
                emps = Employee.objects.filter(reportingTo=SalesEmployeeCode)
                SalesEmployeeCode = [str(SalesEmployeeCode)]
                for emp in emps:
                    SalesEmployeeCode.append(str(emp.SalesEmployeeCode))
            else:
                SalesEmployeeCode = [str(SalesEmployeeCode)]
                # emps = Employee.objects.filter(reportingTo=emp_obj.reportingTo)#.values('id', 'SalesEmployeeCode')
                # SalesEmployeeCode=[]
                # for emp in emps:
                # SalesEmployeeCode.append(emp.SalesEmployeeCode)

            print(SalesEmployeeCode)

            r = requests.post(settings.BASEURL+'/Login',
                              data=json.dumps(settings.SAPDB), verify=False)
            token = json.loads(r.text)['SessionId']
            print(token)

            ps = []
            for s in SalesEmployeeCode:
                print("SalesPersonCode eq "+str(s))
                ps.append("SalesPersonCode eq "+str(s))

            param = " or ".join(ps)
            # addr = settings.BASEURL+"/Invoices/$count?$filter="
            addr = settings.BASEURL+"/Invoices/$count?$filter="
            url = addr+param
            print(url)
            #{"SalesEmployeeCode":"1"}
            #http://103.234.187.35:50001/b1s/v1/Invoices/$count?$filter=SalesPersonCode eq 3 or SalesPersonCode eq 4
            res = requests.get(url, cookies=r.cookies, verify=False)
            live = json.loads(res.text)
            if type(live) == int:
                return Response({"message": "Success", "status": 200, "data": [{"Invoice": live}]})
            else:
                print(live['error']['message']['value'])
                return Response({"message": "Success", "status": 201, "data": [{"SAP_error": live['error']['message']['value']}]})
        else:
            return Response({"message": "Unsuccess", "status": 201, "data": [{"error": "SalesEmployeeCode?"}]})
    else:
        return Response({"message": "Unsuccess", "status": 201, "data": [{"error": "SalesEmployeeCode?"}]})

#Employee Create API


@api_view(['POST'])
def create(request):
    try:
        if request.data['userName']=='' or request.data['userName']== None :
            return Response({"message": "UserName Can't be Empty", "status": 201, "data": []})
        elif request.data['Email']=='' or request.data['Email']== None :
            return Response({"message": "Email Can't be Empty", "status": 201, "data": []})
        elif request.data['Mobile']=='' or request.data['Mobile']== None :
            return Response({"message": "Mobile Number Can't be Empty", "status": 201, "data": []})
        else:
            if Employee.objects.filter(userName=request.data['userName']).exists():
                return Response({"message": "UserName Already Exists", "status": 201, "data": []})
            elif Employee.objects.filter(Email=request.data['Email']).exists():
                return Response({"message": "Email Already Exists", "status": 201, "data": []})
            elif Employee.objects.filter(Mobile=request.data['Mobile']).exists():
                return Response({"message": "Mobile Number Already Exists", "status": 201, "data": []})
            else:
                companyID = request.data['companyID']
                SalesEmployeeName = request.data['SalesEmployeeName']
                EmployeeID = request.data['EmployeeID']
                userName = request.data['userName']
                password = request.data['password']
                firstName = request.data['firstName']
                middleName = request.data['middleName']
                lastName = request.data['lastName']
                Email = request.data['Email']
                Mobile = request.data['Mobile']
                role = request.data['role']
                position = request.data['position']
                branch = request.data['branch']
                Active = request.data['Active']
                salesUnit = request.data['salesUnit']
                #passwordUpdatedOn = request.data['passwordUpdatedOn']
                #lastLoginOn = request.data['lastLoginOn']
                #logedIn = request.data['logedIn']
                reportingTo = request.data['reportingTo']
                div = request.data['div']
                timestamp = request.data['timestamp']

            try:
                model = Employee(companyID=companyID, SalesEmployeeName=SalesEmployeeName, EmployeeID=EmployeeID, userName=userName, password=password, firstName=firstName, middleName=middleName,lastName=lastName, Email=Email, Mobile=Mobile, role=role, position=position, branch=branch, Active=Active, salesUnit=salesUnit, reportingTo=reportingTo, timestamp=timestamp, div=div)

                model.save()

                sp = Employee.objects.latest('id')

                if settings.SAPSP == True:
                    r = requests.post(settings.BASEURL+'/Login',
                                    data=json.dumps(settings.SAPDB), verify=False)
                    token = json.loads(r.text)['SessionId']
                    print(token)

                    sp_data = {
                    "SalesEmployeeName": request.data['SalesEmployeeName'],
                    "EmployeeID": request.data['EmployeeID'],
                    "Active": "tYES",
                    "Mobile": request.data['Mobile'],
                    "Email": request.data['Email']
                }

                    #print(sp_data)
                    #print(json.dumps(sp_data))

                    res = requests.post(settings.BASEURL+'/SalesPersons', data=json.dumps(sp_data), cookies=r.cookies, verify=False)
                    live = json.loads(res.text)

                    fetchid = sp.id

                    if "SalesEmployeeCode" in live:
                        print(live['SalesEmployeeCode'])

                        model = Employee.objects.get(pk=fetchid)
                        model.SalesEmployeeCode = live['SalesEmployeeCode']
                        model.save()

                        return Response({"message": "successful", "status": 200, "data": [{"Sp_Id": sp.id, "SalesEmployeeCode": live['SalesEmployeeCode']}]})
                    else:
                        SAP_MSG = live['error']['message']['value']
                        print(SAP_MSG)
                    if "already exists" in SAP_MSG:
                        fetchdata = Employee.objects.filter(pk=fetchid).delete()
                        return Response({"message": live['error']['message']['value'], "SAP_error": SAP_MSG, "status": 202, "data": []})
                    else:
                        fetchdata = Employee.objects.filter(pk=fetchid).delete()
                        return Response({"message": SAP_MSG, "SAP_error": SAP_MSG, "status": 202, "data": []})
                else:
                    model = Employee.objects.get(pk=sp.id)
                    model.SalesEmployeeCode = sp.id
                    model.save()
                    return Response({"message": "successful", "status": 200, "data": [{"Sp_Id": sp.id, "SalesEmployeeCode": sp.id}]})

            except Exception as e:
                return Response({"message": str(e), "status": 200, "data": []})

    except Exception as e:
        return Response({"message": str(e), "status": 200, "data": []})


#Employee All API


@api_view(["GET"])
def all(request):
    emps_obj = Employee.objects.all().order_by("-id")
    emps_json = EmployeeSerializer(emps_obj, many=True)
    emps_json = json.loads(json.dumps(emps_json.data))

    for employee_obj in emps_json:
        print(employee_obj['div'])
        if employee_obj['div'] != "":
            div_arr = employee_obj['div'].split(",")
            div_obj = Category.objects.filter(Number__in=div_arr)
            div_json = CategorySerializer(div_obj, many=True).data
            employee_obj['div'] = div_json
        else:
            employee_obj['div'] = []
    return Response({"message": "Success", "status": 200, "data": emps_json})


@api_view(["POST"])
def all_filter(request):
    json_data = request.data

    if "SalesEmployeeCode" in json_data:
        print("yes")

        if json_data['SalesEmployeeCode'] != "":
            SalesEmployeeCode = json_data['SalesEmployeeCode']

            emp_obj = Employee.objects.get(SalesEmployeeCode=SalesEmployeeCode)
            if emp_obj.role == 'admin' or emp_obj.role == 'ceo':
                emps = Employee.objects.filter(SalesEmployeeCode__gt=0).order_by("-id")
                SalesEmployeeCode = []
                for emp in emps:
                    SalesEmployeeCode.append(emp.SalesEmployeeCode)
            elif emp_obj.role == 'manager':
                # .values('id', 'SalesEmployeeCode')
                emps = Employee.objects.filter(reportingTo=SalesEmployeeCode).order_by("-id")
                SalesEmployeeCode = [SalesEmployeeCode]
                for emp in emps:
                    SalesEmployeeCode.append(emp.SalesEmployeeCode)
            else:
                SalesEmployeeCode = [SalesEmployeeCode]
                # emps = Employee.objects.filter(reportingTo=emp_obj.reportingTo)#.values('id', 'SalesEmployeeCode')
                # SalesEmployeeCode=[]
                # for emp in emps:
                # SalesEmployeeCode.append(emp.SalesEmployeeCode)

            print(SalesEmployeeCode)

            emps_all = Employee.objects.filter(
                SalesEmployeeCode__in=SalesEmployeeCode, Active="tYES").order_by("-id")
            emps_json = EmployeeSerializer(emps_all, many=True)

            emps_json = json.loads(json.dumps(emps_json.data))

            for employee_obj in emps_json:
                print(employee_obj['div'])
                if employee_obj['div'] != "":
                    div_arr = employee_obj['div'].split(",")
                    div_obj = Category.objects.filter(Number__in=div_arr)
                    div_json = CategorySerializer(div_obj, many=True).data
                    employee_obj['div'] = div_json
                else:
                    employee_obj['div'] = []

            return Response({"message": "Success", "status": 200, "data": emps_json})
            #return Response({"message": "Success","status": 201,"data":[{"emp":SalesEmployeeCode}]})
        else:
            return Response({"message": "Unsuccess", "status": 201, "data": [{"error": "SalesEmployeeCode?"}]})
    else:
        print("no")
        return Response({"message": "Unsuccess", "status": 201, "data": [{"error": "SalesEmployeeCode?"}]})

#All Employee by reportingTo


@api_view(["POST"])
def all_filter_reportingto(request):
    json_data = request.data

    if "SalesEmployeeCode" in json_data:
        if json_data['SalesEmployeeCode'] != "":
            SalesEmployeeCode = json_data['SalesEmployeeCode']
            emps_all1 = []
            # .values('id', 'SalesEmployeeCode')
            emps_all = Employee.objects.filter(reportingTo=SalesEmployeeCode)
            print(len(emps_all))
            print(SalesEmployeeCode)

            if len(emps_all) == 0:
                print(SalesEmployeeCode)
                return Response({"message": "Success", "status": 200, "data": []})
            else:
                emps_json = EmployeeSerializer(emps_all, many=True)
            return Response({"message": "Success", "status": 200, "data": emps_json.data})
        else:
            return Response({"message": "Unsuccess", "status": 201, "data": [{"error": "SalesEmployeeCode?"}]})
    else:
        print("no")
        return Response({"message": "Unsuccess", "status": 201, "data": [{"error": "SalesEmployeeCode?"}]})


@api_view(["POST"])
def all_filter_assignto(request):
    json_data = request.data

    if "SalesEmployeeCode" in json_data:
        print("yes")

        if json_data['SalesEmployeeCode'] != "":
            SalesEmployeeCode = json_data['SalesEmployeeCode']
            emps_all1 = []
            # .values('id', 'SalesEmployeeCode')
            emps_all = Employee.objects.filter(
                reportingTo=SalesEmployeeCode, Active="tYES")
            print(len(emps_all))
            print(SalesEmployeeCode)

            if len(emps_all) == 0:
                print(SalesEmployeeCode)
                emp_obj = Employee.objects.get(
                    SalesEmployeeCode=SalesEmployeeCode)
                # .values('id', 'SalesEmployeeCode')
                emps_all = Employee.objects.filter(
                    reportingTo=emp_obj.reportingTo, Active="tYES")
                emps_json = EmployeeSerializer(emps_all, many=True)
            else:
                #emps_json = EmployeeSerializer(emps_all, many=True)
                print("come")
                emp_obj = Employee.objects.get(
                    SalesEmployeeCode=SalesEmployeeCode)
                siblings = Employee.objects.filter(
                    reportingTo=emp_obj.reportingTo, Active="tYES")
                if len(siblings) != 0:
                    for sibling in siblings:
                        emps_all1.append(sibling)
                else:
                    emps_all1.append(emp_obj)

                for emps in emps_all:
                    emps_all1.append(emps)
                    emps_all_tree = Employee.objects.filter(
                        reportingTo=emps.SalesEmployeeCode, Active="tYES")  # .values('id',
                    print(emps.SalesEmployeeCode)
                    print("Code" + str(emps.SalesEmployeeCode))
                    print("Len" + str(len(emps_all_tree)))
                    if len(emps_all_tree) != 0:
                        for all_tree in emps_all_tree:
                            emps_all_tree1 = Employee.objects.filter(
                                reportingTo=all_tree.SalesEmployeeCode, Active="tYES")
                            if len(emps_all_tree1) != 0:
                                print("Code" + str(all_tree.SalesEmployeeCode))
                                print("Len" + str(len(emps_all_tree1)))
                                for all_tree1 in emps_all_tree1:
                                    print(
                                        "Code" + str(all_tree1.SalesEmployeeCode))
                                    emps_all1.append(all_tree1)
                            emps_all1.append(all_tree)
                emps_json = EmployeeSerializer(emps_all1, many=True)
            return Response({"message": "Success", "status": 200, "data": emps_json.data})

            #return Response({"message": "Success","status": 201,"data":[{"emp":SalesEmployeeCode}]})
        else:
            return Response({"message": "Unsuccess", "status": 201, "data": [{"error": "SalesEmployeeCode?"}]})
    else:
        print("no")
        return Response({"message": "Unsuccess", "status": 201, "data": [{"error": "SalesEmployeeCode?"}]})


#Employee All Filter API
@api_view(["POST"])
def all_filter_old(request):
    json_data = request.data

    if len(json_data) == 0:
        emps_obj = Employee.objects.all().order_by("-id")
        emps_json = EmployeeSerializer(emps_obj, many=True)
        return Response({"message": "Success", "status": 200, "data": emps_json.data})
    else:
        #print(json_data.keys()[0])
        #if json_data['U_FAV']
        for ke in json_data.keys():
            if ke == 'reportingTo':
                if json_data['reportingTo'] != '':
                    emps_obj = Employee.objects.filter(
                        reportingTo=json_data['reportingTo']).order_by("-id")
                    if len(emps_obj) == 0:
                        return Response({"message": "Not Available", "status": 201, "data": []})
                    else:
                        emps_json = EmployeeSerializer(emps_obj, many=True)
                        return Response({"message": "Success", "status": 200, "data": emps_json.data})
            elif ke == 'role':
                if json_data['role'] != '':
                    emps_obj = Employee.objects.filter(
                        role=json_data['role']).order_by("-id")
                    if len(emps_obj) == 0:
                        return Response({"message": "Not Available", "status": 201, "data": []})
                    else:
                        emps_json = EmployeeSerializer(emps_obj, many=True)
                        return Response({"message": "Success", "status": 200, "data": emps_json.data})
            else:
                return Response({"message": "Not Available", "status": 201, "data": []})

#Employee One API


@api_view(["POST"])
def one(request):
    id = request.data['id']
    #{"id":2}
    employee_obj = Employee.objects.get(id=id)
    employee_json = json.loads(json.dumps(
        EmployeeSerializer(employee_obj).data))
    if employee_obj.div != "":
        div_arr = employee_obj.div.split(",")
        div_obj = Category.objects.filter(Number__in=div_arr)
        div_json = CategorySerializer(div_obj, many=True).data
        employee_json['div'] = div_json
    else:
        employee_json['div'] = []

    return Response({"message": "Success", "status": 200, "data": [employee_json]})

#Employee Login API


@api_view(["POST"])
def login(request):

    try:
        #added by millan for showing active users only
        if Employee.objects.filter(userName=request.data['userName'], Active="tYES").exists():
            userName = request.data['userName']
            password = request.data['password']
            FCM = request.data['FCM']

            if Employee.objects.filter(userName=userName, password=password).exists():
                print("uname")
                employee_obj = Employee.objects.get(
                    userName=userName, password=password)
            elif Employee.objects.filter(Email=userName, password=password).exists():
                print("email")
                employee_obj = Employee.objects.get(
                    Email=userName, password=password)
            else:
                print("incorrect")
                return Response({"message": "Username or password is incorrect", "status": 200, "data": [], "SAP": []})
            if FCM != "":
                employee_obj.FCM = FCM
                employee_obj.save()
            employee_json = EmployeeSerializer(employee_obj)

            if employee_obj.reportingTo == "0" or employee_obj.reportingTo == "":
                print("if")
                print(employee_obj.reportingTo)
                repoto = "Cinntra"
                print(repoto)
            else:
                print(employee_obj.reportingTo)
                print("else")
                repoto = Employee.objects.get(
                    SalesEmployeeCode=employee_obj.reportingTo).SalesEmployeeName
                print(repoto)

            lev = tree(employee_obj.SalesEmployeeCode)
            #lev = tree_role(employee_obj)
            print(lev)
            json_ob = json.dumps(employee_json.data)
            json_obj = json.loads(json_ob)
            #print(json_obj)
            slave_obj = AppSlave.objects.filter(Level=lev)
            #print(slave_obj[0].Max)

            levdis = {"reportingName": repoto, "level": int(
                lev), "discount": slave_obj[0].Max}
            #print(levdis)
            json_obj.update(levdis)
            #print(json_obj)
            #print(employee_obj.div)
            if employee_obj.role == 'admin' or employee_obj.role == 'ceo':
                div_obj = Category.objects.all()
                div_json = CategorySerializer(div_obj, many=True).data
                print(div_json)
                json_obj['div'] = div_json
            else:  # employee_obj.div !="":
                div_arr = employee_obj.div.split(",")
                div_obj = Category.objects.filter(Number__in=div_arr)
                div_json = CategorySerializer(div_obj, many=True).data
                print(div_json)
                json_obj['div'] = div_json
            return Response({"message": "Success", "status": 200, "data": json_obj, "SAP": settings.SAPDB})
        else:
            return Response({"message": "User is InActive", "status": 201, "data": []})
    except Exception as e:
        return Response({"message": str(e), "status": "201", "data": [{"Error": str(e)}]})

#Employee Update API


@api_view(['POST'])
def update(request):
    fetchid = request.data['id']
    try:
        model = Employee.objects.get(pk=fetchid)

        model.companyID = request.data['companyID']
        model.SalesEmployeeName = request.data['SalesEmployeeName']
        model.EmployeeID = request.data['EmployeeID']
        model.userName = request.data['userName']
        model.password = request.data['password']
        model.firstName = request.data['firstName']
        model.middleName = request.data['middleName']
        model.lastName = request.data['lastName']
        model.Email = request.data['Email']
        model.Mobile = request.data['Mobile']
        model.role = request.data['role']
        model.position = request.data['position']
        model.branch = request.data['branch']
        model.Active = request.data['Active']
        model.salesUnit = request.data['salesUnit']
        model.reportingTo = request.data['reportingTo']
        model.div = 100  # request.data['div']

        model.save()
        if settings.SAPSP == True:
            context = {
                "id": request.data['id'],
                'companyID': request.data['companyID'],
                'SalesEmployeeCode': request.data['SalesEmployeeCode'],
                'SalesEmployeeName': request.data['SalesEmployeeName'],
                'EmployeeID': request.data['EmployeeID'],
                'userName': request.data['userName'],
                'password': request.data['password'],
                'firstName': request.data['firstName'],
                'middleName': request.data['middleName'],
                'lastName': request.data['lastName'],
                'Email': request.data['Email'],
                'Mobile': request.data['Mobile'],
                'role': request.data['role'],
                'position': request.data['position'],
                'branch': request.data['branch'],
                'Active': request.data['Active'],
                'salesUnit': request.data['salesUnit'],
                'reportingTo': request.data['reportingTo']
            }

            r = requests.post(settings.BASEURL+'/Login',
                              data=json.dumps(settings.SAPDB), verify=False)
            token = json.loads(r.text)['SessionId']
            print(token)

            sp_data = {
                "SalesEmployeeName": request.data['SalesEmployeeName'],
                "EmployeeID": request.data['EmployeeID'],
                "Active": request.data['Active'],
                "Mobile": request.data['Mobile'],
                "Email": request.data['Email']
            }

            print(sp_data)
            print(json.dumps(sp_data))

            print(settings.BASEURL+'/SalesPersons(' +
                  request.data['SalesEmployeeCode']+')')

            res = requests.patch(settings.BASEURL+'/SalesPersons(' +
                                 request.data['SalesEmployeeCode']+')', data=json.dumps(sp_data), cookies=r.cookies, verify=False)

            if len(res.content) != 0:
                res1 = json.loads(res.content)
                SAP_MSG = res1['error']['message']['value']
                print(SAP_MSG)
                return Response({"message": "Partely successful", "status": 202, "SAP_error": SAP_MSG, "data": [context]})
            else:
                return Response({"message": "successful", "status": 200, "data": [context]})
        else:
            return Response({"message": "successful", "status": 200, "data": []})
    except Exception as e:
        return Response({"message": str(e), "status": "201", "data": []})

#Employee delete


@api_view(['POST'])
def delete(request):
    try:
        fetchid = request.data['id']
        emp = Employee.objects.get(pk=fetchid)
        SalesEmployeeCode = emp.SalesEmployeeCode

        fetchdata = Employee.objects.filter(pk=fetchid).delete()
        if settings.SAPSP == True:
            # print(data)

            try:
                r = requests.post(settings.BASEURL+'/Login',
                                  data=json.dumps(settings.SAPDB), verify=False)
                token = json.loads(r.text)['SessionId']
                print(token)
                res = requests.delete(
                    settings.BASEURL+'/SalesPersons('+SalesEmployeeCode+')', cookies=r.cookies, verify=False)
                return Response({"message": "successful", "status": "200", "data": []})
            except:
                return Response({"message": "successful", "status": "200", "data": []})
        else:
            return Response({"message": "successful", "status": "200", "data": []})
    except:
        return Response({"message": "Id wrong", "status": "201", "data": []})


def months_check(months, qt1, qt2, qt3, qt4):
    q1 = q2 = q3 = q4 = 0
    for mo in months:
        if mo['qtr'] == 1:
            q1 = q1 + int(mo['amount'])
        elif mo['qtr'] == 2:
            q2 = q2 + int(mo['amount'])
        elif mo['qtr'] == 3:
            q3 = q3 + int(mo['amount'])
        elif mo['qtr'] == 4:
            q4 = q4 + int(mo['amount'])

    if q1 != qt1:
        return {"message": "The months total of Qtr 1 should be equal to Q1 value", "data": q1}
    elif q2 != qt2:
        return {"message": "The months total of Qtr 2 should be equal to Q2 value", "data": q2}
    elif q3 != qt3:
        return {"message": "The months total of Qtr 3 should be equal to Q3 value", "data": q3}
    elif q4 != qt4:
        return {"message": "The months total of Qtr 4 should be equal to Q4 value", "data": q4}
    else:
        return "ok"

#Target Create API


@api_view(['POST'])
def targetqtm_create(request):

    try:
        if request.data['id'] != "":
            #StartYear = int(request.data['StartYear'])
            #EndYear = int(request.data['EndYear'])
            SalesPersonCode = request.data['SalesPersonCode']
            #Department = request.data['Department']
            reportingTo = request.data['reportingTo'].strip()
            YearTarget = request.data['YearTarget']
            q1 = int(request.data['q1'])
            q2 = int(request.data['q2'])
            q3 = int(request.data['q3'])
            q4 = int(request.data['q4'])

            CreatedDate = request.data['CreatedDate']
            UpdatedDate = request.data['UpdatedDate']

            if Targetqty.objects.filter(pk=request.data['id']).exists():
                qtymodel = Targetqty.objects.get(pk=request.data['id'])
            else:
                return Response({"message": "Qtr info does not exists", "status": "201", "data": []})

            YearTargetAmount = Targetyr.objects.get(pk=YearTarget).YearTarget
            print(YearTargetAmount)
            print(q1+q2+q3+q4)

            if YearTargetAmount != (q1+q2+q3+q4):
                return Response({"message": "YearTarget should be equal to all quater", "status": "201", "data": []})
            elif (q1 < 1 or q2 < 1 or q3 < 1 or q4 < 1):
                return Response({"message": "All Qtr should be fill", "status": "201", "data": []})
            elif SalesPersonCode == reportingTo:
                return Response({"message": "SalesPersonCode and reportingTo are same", "status": "201", "data": []})
            else:

                if reportingTo == "" or reportingTo == "0":
                    qtymodel.SalesPersonCode_id = SalesPersonCode
                    qtymodel.YearTarget_id = YearTarget
                    qtymodel.q1 = q1
                    qtymodel.q2 = q2
                    qtymodel.q3 = q3
                    qtymodel.q4 = q4
                    qtymodel.CreatedDate = CreatedDate
                    qtymodel.UpdatedDate = CreatedDate
                else:
                    qtymodel.SalesPersonCode_id = SalesPersonCode
                    qtymodel.reportingTo_id = reportingTo
                    qtymodel.YearTarget_id = YearTarget
                    qtymodel.q1 = q1
                    qtymodel.q2 = q2
                    qtymodel.q3 = q3
                    qtymodel.q4 = q4
                    qtymodel.CreatedDate = CreatedDate
                    qtymodel.UpdatedDate = CreatedDate
                qtymodel.save()
                tgt = Targetqty.objects.latest('id')
                #print(tgt.id)
                if len(request.data['monthly']) == 12:
                    months = request.data['monthly']
                    if months[0]['amount'] < 1 or months[1]['amount'] < 1 or months[2]['amount'] < 1 or months[3]['amount'] < 1 or months[4]['amount'] < 1 or months[5]['amount'] < 1 or months[6]['amount'] < 1 or months[7]['amount'] < 1 or months[8]['amount'] < 1 or months[9]['amount'] < 1 or months[10]['amount'] < 1 or months[11]['amount'] < 1:
                        return Response({"message": "Quaterley saved but monthly try again after fill all months", "status": "201", "data": []})
                    else:

                        chk = months_check(
                            request.data['monthly'], request.data['q1'], request.data['q2'], request.data['q3'], request.data['q4'])

                        if chk == "ok":
                            if request.data['monthly'][0]["id"] != "":
                                for mo in months:
                                    mont = Target.objects.get(pk=mo['id'])
                                    print(mo['id'])
                                    print(mont)
                                    mont.YearTarget_id = YearTarget
                                    mont.amount = mo['amount']
                                    mont.monthYear = mo['monthYear']
                                    mont.SalesPersonCode_id = SalesPersonCode
                                    mont.qtr = mo['qtr']
                                    mont.CreatedDate = mo['CreatedDate']
                                    mont.UpdatedDate = mo['CreatedDate']
                                    mont.save()
                            else:
                                for mo in months:
                                    mont = Target(YearTarget_id=YearTarget, amount=mo['amount'], monthYear=mo['monthYear'],
                                                  SalesPersonCode_id=SalesPersonCode, qtr=mo['qtr'], CreatedDate=mo['CreatedDate'], UpdatedDate=mo['CreatedDate'])
                                    mont.save()
                            return Response({"message": "Success", "status": "200", "data": []})
                        else:
                            print(chk)
                            return Response({"message": chk['message'], "status": "201", "data": chk['data']})

                else:
                    return Response({"message": "Quaterley saved but monthly try again after fill all months", "status": "201", "data": []})
        else:
            #StartYear = int(request.data['StartYear'])
            #EndYear = int(request.data['EndYear'])
            SalesPersonCode = request.data['SalesPersonCode']
            #Department = request.data['Department']
            reportingTo = request.data['reportingTo'].strip()
            YearTarget = request.data['YearTarget']
            q1 = int(request.data['q1'])
            q2 = int(request.data['q2'])
            q3 = int(request.data['q3'])
            q4 = int(request.data['q4'])

            CreatedDate = request.data['CreatedDate']
            UpdatedDate = request.data['UpdatedDate']

            if len(Targetqty.objects.filter(YearTarget=YearTarget, SalesPersonCode=SalesPersonCode)) > 0:
                return Response({"message": "Already exist with this Financial Year", "status": "201", "data": []})
            YearTargetAmount = Targetyr.objects.get(pk=YearTarget).YearTarget
            print(YearTargetAmount)
            print(q1+q2+q3+q4)

            if YearTargetAmount != (q1+q2+q3+q4):
                return Response({"message": "YearTarget should be equal to all quater", "status": "201", "data": []})
            elif (q1 < 1 or q2 < 1 or q3 < 1 or q4 < 1):
                return Response({"message": "All Qtr should be fill", "status": "201", "data": []})
            elif SalesPersonCode == reportingTo:
                return Response({"message": "SalesPersonCode and reportingTo are same", "status": "201", "data": []})
            else:

                if reportingTo == "" or reportingTo == "0":
                    model = Targetqty(SalesPersonCode_id=SalesPersonCode, YearTarget_id=YearTarget,
                                      q1=q1, q2=q2, q3=q3, q4=q4, CreatedDate=CreatedDate, UpdatedDate=CreatedDate)
                else:
                    model = Targetqty(SalesPersonCode_id=SalesPersonCode, reportingTo_id=reportingTo, YearTarget_id=YearTarget,
                                      q1=q1, q2=q2, q3=q3, q4=q4, CreatedDate=CreatedDate, UpdatedDate=CreatedDate)

                    #print("reportingTo_id="+str(reportingTo))

                model.save()
                tgt = Targetqty.objects.latest('id')
                #print(tgt.id)
                if len(request.data['monthly']) == 12:
                    months = request.data['monthly']
                    if months[0]['amount'] < 1 or months[1]['amount'] < 1 or months[2]['amount'] < 1 or months[3]['amount'] < 1 or months[4]['amount'] < 1 or months[5]['amount'] < 1 or months[6]['amount'] < 1 or months[7]['amount'] < 1 or months[8]['amount'] < 1 or months[9]['amount'] < 1 or months[10]['amount'] < 1 or months[11]['amount'] < 1:
                        return Response({"message": "Quaterley saved but monthly try again after fill all months", "status": "201", "data": []})
                    else:
                        chk = months_check(
                            request.data['monthly'], request.data['q1'], request.data['q2'], request.data['q3'], request.data['q4'])

                        if chk == "ok":
                            for mo in months:
                                mont = Target(YearTarget_id=YearTarget, amount=mo['amount'], monthYear=mo['monthYear'],
                                              SalesPersonCode_id=SalesPersonCode, qtr=mo['qtr'], CreatedDate=mo['CreatedDate'], UpdatedDate=mo['CreatedDate'])
                                mont.save()
                            return Response({"message": "Success", "status": "200", "data": []})
                        else:
                            print(chk)
                            return Response({"message": chk['message'], "status": "201", "data": chk['data']})
                else:
                    return Response({"message": "Quaterley saved but monthly try again after fill all months", "status": "201", "data": []})
    except Exception as e:
        return Response({"message": str(e), "status": "201", "data": [{"Error": str(e)}]})


def check_year(yeardata):
    StartYear = yeardata[0]['StartYear']
    EndYear = yeardata[0]['EndYear']
    Department = yeardata[0]['Department']
    reportingTo = yeardata[0]['reportingTo']

    if Targetyr.objects.filter(StartYear=StartYear, EndYear=EndYear, SalesPersonCode=reportingTo, Department=Department).exists():
        YearTarget = Targetyr.objects.get(
            StartYear=StartYear, EndYear=EndYear, SalesPersonCode=reportingTo, Department=Department).YearTarget
        ttl = 0
        for dt in yeardata:
            ttl = ttl+int(dt['YearTarget'])
        if YearTarget >= ttl:
            return "ok"
        else:
            return "Team distribution total should be equal to Target Goal"
    else:
        return "ok"

#Target yr Create API


@api_view(['POST'])
def targetyr_create(request):
    try:
        yrs = request.data
        chk = check_year(yrs)
        if chk == "ok":
            for yr in yrs:
                StartYear = int(yr['StartYear'])
                EndYear = int(yr['EndYear'])
                SalesPersonCode = yr['SalesPersonCode']
                Department = yr['Department']
                reportingTo = yr['reportingTo'].strip()
                YearTarget = int(yr['YearTarget'])

                CreatedDate = yr['CreatedDate']
                UpdatedDate = yr['UpdatedDate']

                if len(Targetyr.objects.filter(StartYear=StartYear, EndYear=EndYear, SalesPersonCode=SalesPersonCode, Department=Department)) > 0:
                    return Response({"message": "Already exist with this Financial Year", "status": "201", "data": []})
                print(YearTarget)
                if SalesPersonCode == reportingTo:
                    return Response({"message": "SalesPersonCode and reportingTo are same", "status": "201", "data": []})
                elif StartYear == EndYear:
                    return Response({"message": "StartYear and EndYear are same", "status": "201", "data": []})
                else:

                    if reportingTo == "":
                        model = Targetyr(StartYear=StartYear, EndYear=EndYear, SalesPersonCode_id=SalesPersonCode,
                                         Department=Department, YearTarget=YearTarget, CreatedDate=CreatedDate, UpdatedDate=CreatedDate)
                    else:
                        model = Targetyr(StartYear=StartYear, EndYear=EndYear, SalesPersonCode_id=SalesPersonCode, Department=Department,
                                         reportingTo_id=reportingTo, YearTarget=YearTarget, CreatedDate=CreatedDate, UpdatedDate=CreatedDate)

                    model.save()
                    #tgt = Targetyr.objects.latest('id')
                    #print(tgt.id)
            return Response({"message": "Success", "status": "200", "data": []})
        else:
            return Response({"message": chk, "status": "201", "data": []})
    except Exception as e:
        return Response({"message": str(e), "status": "201", "data": [{"Error": str(e)}]})

#targetqty all API


@api_view(["POST"])
def target_all(request):
    SalesPersonCode = request.data['SalesPersonCode']
    target_obj = Target.objects.filter(SalesPersonCode=SalesPersonCode)
    target_json = TargetSerializer(target_obj, many=True)
    return Response({"message": "Success", "status": 200, "data": target_json.data})

#targetqty all API


@api_view(["POST"])
def targetqtm_all(request):
    YearTarget = request.data['YearTarget']
    targetqty_obj = Targetqty.objects.filter(YearTarget=YearTarget)
    if len(targetqty_obj) > 0:
        targetqty_json = TargetqtySerializer(targetqty_obj, many=True)
        m_obj = Target.objects.filter(YearTarget=YearTarget)
        m_json = TargetSerializer(m_obj, many=True)

        targetqty_json.data[0]["monthly"] = m_json.data

        return Response({"message": "Success", "status": 200, "data": targetqty_json.data})
    else:
        return Response({"message": "Success", "status": 200, "data": []})

#targetqty all API


@api_view(["POST"])
def targetyr_all(request):
    SalesPersonCode = request.data['SalesPersonCode']
    targetyr_obj = Targetyr.objects.filter(SalesPersonCode=SalesPersonCode)
    targetyr_json = TargetyrSerializer(targetyr_obj, many=True)
    return Response({"message": "Success", "status": 200, "data": targetyr_json.data})

#All Employee by reportingTo


@api_view(["POST"])
def targetyr_all_filter(request):
    try:
        dt = request.data
        tgt_obj = Targetyr.objects.filter(
            StartYear=dt['StartYear'], EndYear=dt['EndYear'], Department=dt['Department'], reportingTo=dt['reportingTo'])
        tgt_json = TargetyrSerializer(tgt_obj, many=True)
        return Response({"message": "success", "status": 200, "data": tgt_json.data})
    except Exception as e:
        return Response({"message": str(e), "status": 201, "data": []})

#targetqty close


@api_view(["POST"])
def targetqty_close(request):
    id = request.data["id"]
    try:
        model = Targetqty.objects.filter(pk=id).update(status=1)
        return Response({"message": "Success", "Status": 200, "data": []})
    except Exception as e:
        return Response({"message": str(e), "Status": 200, "data": []})

#targetyr close


@api_view(["POST"])
def targetyr_close(request):
    id = request.data["id"]
    try:
        model = Targetyr.objects.filter(pk=id).update(status=1)
        return Response({"message": "Success", "Status": 200, "data": []})
    except Exception as e:
        return Response({"message": str(e), "Status": 200, "data": []})

@api_view(["POST"])
def ProductLead(request):
    try:
        SalesPersonCode = request.data['SalesPersonCode']

        emp_obj = Employee.objects.get(SalesEmployeeCode=SalesPersonCode)

        if emp_obj.role == 'manager':
            # .values('id', 'SalesEmployeeCode')
            emps = Employee.objects.filter(reportingTo=SalesPersonCode)
            SalesPersonCode = [SalesPersonCode]
            for emp in emps:
                SalesPersonCode.append(emp.SalesEmployeeCode)

        elif emp_obj.role == 'admin' or emp_obj.role == 'ceo':
            emps = Employee.objects.filter(SalesEmployeeCode__gt=0)
            SalesPersonCode = []
            #{"SalesPersonCode":1}
            for emp in emps:
                SalesPersonCode.append(emp.SalesEmployeeCode)
        else:
            SalesPersonCode = request.data['SalesPersonCode']

        print(SalesPersonCode)

        BFS = Lead.objects.filter(
            assignedTo__in=SalesPersonCode, intProdCat="Bottle Filling Stations").count()
        DWF = Lead.objects.filter(
            assignedTo__in=SalesPersonCode, intProdCat="Drinking Water Fountains").count()
        WC = Lead.objects.filter(
            assignedTo__in=SalesPersonCode, intProdCat="Water Coolers").count()
        WCH = Lead.objects.filter(
            assignedTo__in=SalesPersonCode, intProdCat="Water Chillers").count()
        DWS = Lead.objects.filter(
            assignedTo__in=SalesPersonCode, intProdCat="Drinking Water Stations").count()
        DWT = Lead.objects.filter(
            assignedTo__in=SalesPersonCode, intProdCat="Drinking Water Taps").count()
        WD = Lead.objects.filter(
            assignedTo__in=SalesPersonCode, intProdCat="Water Dispenser").count()
        OZO = Lead.objects.filter(
            assignedTo__in=SalesPersonCode, intProdCat="Ozonators").count()
        return Response({"message": "Success", "Status": 200, "data": [{
            "Bottle Filling Stations": str(BFS), "Drinking Water Fountains": str(DWF), "Water Coolers": str(WC), "Water Chillers": str(WCH), "Drinking Water Stations": str(DWS), "Drinking Water Taps": str(DWT), "Water Dispenser": str(WD), "Ozonators": str(OZO)
        }]})
    except Exception as e:
        return Response({"message": str(e), "Status": 201, "data": []})

@api_view(["POST"])
def ProjectLead(request):
    try:
        SalesPersonCode = request.data['SalesPersonCode']

        emp_obj = Employee.objects.get(SalesEmployeeCode=SalesPersonCode)

        if emp_obj.role == 'manager':
            # .values('id', 'SalesEmployeeCode')
            emps = Employee.objects.filter(reportingTo=SalesPersonCode)
            SalesPersonCode = [SalesPersonCode]
            for emp in emps:
                SalesPersonCode.append(emp.SalesEmployeeCode)

        elif emp_obj.role == 'admin' or emp_obj.role == 'ceo':
            emps = Employee.objects.filter(SalesEmployeeCode__gt=0)
            SalesPersonCode = []
            for emp in emps:
                SalesPersonCode.append(emp.SalesEmployeeCode)
        else:
            SalesPersonCode = request.data['SalesPersonCode']

        print(SalesPersonCode)
        WTP = Lead.objects.filter(
            assignedTo__in=SalesPersonCode, intProjCat="Water Treatment Plant").count()
        STP = Lead.objects.filter(
            assignedTo__in=SalesPersonCode, intProjCat="Sewage Treatment Plant").count()
        WS = Lead.objects.filter(
            assignedTo__in=SalesPersonCode, intProjCat="Water Softner").count()
        ETP = Lead.objects.filter(
            assignedTo__in=SalesPersonCode, intProjCat="Effluent Treatment Plant").count()
        ROP = Lead.objects.filter(
            assignedTo__in=SalesPersonCode, intProjCat="Reverse Osmosis Plant").count()
        UFP = Lead.objects.filter(
            assignedTo__in=SalesPersonCode, intProjCat="Ultra Filtration Plant").count()
        return Response({"message": "Success", "Status": 200, "data": [{
            "Water Treatment Plant": str(WTP), "Sewage Treatment Plant": str(STP), "Water Softner": str(WS), "Effluent Treatment Plant": str(ETP), "Reverse Osmosis Plant": str(ROP), "Ultra Filtration Plant": str(UFP)
        }]})
    except Exception as e:
        return Response({"message": str(e), "Status": 201, "data": []})


################# CODE ADDED BY DIPANSHU FORM STANDALONE SUPPORT #############

# All Employee filter by role, dep, subdep
@api_view(["POST"])
def all_filter_multi(request):    
    dep_ids = request.data['Department']
    subdep_ids = request.data['Subdepartment']
    role_ids = request.data['Role']
    emps_all = Employee.objects.filter(dep__in = dep_ids, subdep__in = subdep_ids, role__in=role_ids, Active = "tYES").order_by('-id')
    emps_all.filter(subdep__in = subdep_ids).order_by('-id')
    emps_json = EmployeeSerializer(emps_all, many=True)
    return Response({"message": "Success","status": 200,"data":emps_json.data})            

#Employee reporting Lowerto API
@api_view(["POST"])
def reportingto_lower(request):
    SalesPersonID = request.data['SalesPerson']
    Team = request.data['Team']
    print("request data : ", request.data)
    ids = getAllReportingToIdsSubdep(SalesPersonID, Team)
    obj = Employee.objects.filter(SalesEmployeeCode__in=ids) 
    ojson = EmployeeSerializer(obj, many=True)
    return Response({"message": "Success","status": 200,"data":ojson.data})

#Employee reporting to API
@api_view(["POST"])
def reportingto_upper(request):
    dep = request.data['dep']
    subdep = request.data['subdep']
    level = request.data['level']
    branch = request.data['branch']    
    obj = reptoUpper(dep,subdep,level,branch)    
    ojson = EmployeeSerializer(obj, many=True)
    return Response({"message": "Success","status": 200,"data":ojson.data})

#Employee reporting Lowerto API
@api_view(["POST"])
def reportingto_lower_all(request):
    SalesPersonID = request.data['SalesPerson']
    ids = getAllReportingToIds(SalesPersonID)
    obj = Employee.objects.filter(SalesEmployeeCode__in=ids)    
    ojson = EmployeeSerializer(obj, many=True)
    return Response({"message": "Success","status": 200,"data":ojson.data})

#Employee Help Team API for Ticket assign change
@api_view(["POST"])
def get_help(request):
    SalesPersonID = request.data['SalesPerson']
    Team = request.data['Team']    
    ids = HelpTeam(SalesPersonID, Team)
    obj = Employee.objects.filter(SalesEmployeeCode__in=ids)    
    ojson = EmployeeSerializer(obj, many=True)
    return Response({"message": "Success","status": 200,"data":ojson.data})

#Department All API
@api_view(["GET"])
def department(request):
    obj = EmpDepartment.objects.all()
    ojson = EmpDepartmentSerializer(obj, many=True)
    return Response({"message": "Success","status": 200,"data":ojson.data})

#Sub Department All API
@api_view(["GET"])
def subdepartment(request):
    obj = Subdepartment.objects.all()
    ojson = SubdepartmentSerializer(obj, many=True)
    return Response({"message": "Success","status": 200,"data":ojson.data})

#role filter API
@api_view(["POST"])
def subdepartment_filter(request):
    department = request.data['department']
    if department =="Management":
        obj = Subdepartment.objects.filter(Name="Management")
    elif department =="Installation":
        obj = Subdepartment.objects.filter(Name="Operation")
    else:
        obj = Subdepartment.objects.all().exclude(Name="Management")
        
    ojson = SubdepartmentSerializer(obj, many=True)
    return Response({"message": "Success","status": 200,"data":ojson.data})

#Subdepartment filter multiple API
@api_view(["POST"])
def subdepartment_filter_multi(request):
    department = request.data['department']
    #{"department":[2,3]}
    #{"department":[1,4]}
    ids =[]
    subd = Subdepartment.objects.all() 
    for dep in department:
        for sub in subd:
            arr = sub.Department#.split(',')
            if str(dep) in arr:
                ids.append(sub.id)            
    #print("ids",ids)
    obj = Subdepartment.objects.filter(id__in=ids)        
    ojson = SubdepartmentSerializer(obj, many=True)
    return Response({"message": "Success","status": 200,"data":ojson.data})

#role All API
@api_view(["GET"])
def role(request):
    obj = Role.objects.all()
    ojson = RoleSerializer(obj, many=True)
    return Response({"message": "Success","status": 200,"data":ojson.data})

#role filter API
@api_view(["POST"])
def role_filter(request):
    Subdepartment = request.data['Subdepartment']
    obj = Role.objects.filter(Subdepartment=Subdepartment).exclude(Name="Admin")
    ojson = RoleSerializer(obj, many=True)
    return Response({"message": "Success","status": 200,"data":ojson.data})

#role filter multiple API
@api_view(["POST"])
def role_filter_multi(request):
    Subdepartment = request.data['Subdepartment']
    #{"Subdepartment":[2,3]}
    obj = Role.objects.filter(Subdepartment__in=Subdepartment).exclude(Name="Admin")
    ojson = RoleSerializer(obj, many=True)
    
@api_view(["POST"])
def employee_target_sell(request):
        SalesPersonCode = request.data['SalesPersonCode']        
        SalesPersonCode_arr = getAllReportingToIds(SalesPersonCode)
        SalesPersonCode_list = ",".join(SalesPersonCode_arr)
        todays_date = date.today()
        CurrYr = todays_date.year
        NextYr = todays_date.year +1
        FinanYr = str(CurrYr) + '-' + str(NextYr)        
        fyTarget =[
                {
                    "MonthlyTargetSales": 0,
                    "Month":  str("Jan") + "-" + str(NextYr),
                    "MonthlyAchievedSales": 0,
                    "FinancialYear": FinanYr
                },
                {
                    "MonthlyTargetSales": 0,
                    "Month": str("Feb") + "-" + str(NextYr),
                    "MonthlyAchievedSales": 0,
                    "FinancialYear": FinanYr
                },
                {
                    "MonthlyTargetSales": 0,
                    "Month": str("Mar") + "-" + str(NextYr),
                    "MonthlyAchievedSales": 0,
                    "FinancialYear": FinanYr
                },        
                {
                    "MonthlyTargetSales": 0,
                    "Month": str("Apr") + "-" + str(CurrYr),
                    "MonthlyAchievedSales": 0,
                    "FinancialYear": FinanYr
                },
                {
                    "MonthlyTargetSales": 0,
                    "Month": str("May") + "-" + str(CurrYr),
                    "MonthlyAchievedSales": 0,
                    "FinancialYear": FinanYr
                },
                {
                    "MonthlyTargetSales": 0,
                    "Month": str("Jun") + "-" + str(CurrYr),
                    "MonthlyAchievedSales": 0,
                    "FinancialYear": FinanYr
                },
                {
                    "MonthlyTargetSales": 0,
                    "Month": str("Jul") + "-" + str(CurrYr),
                    "MonthlyAchievedSales": 0,
                    "FinancialYear": FinanYr
                },
                {
                    "MonthlyTargetSales": 0,
                    "Month": str("Aug") + "-" + str(CurrYr),
                    "MonthlyAchievedSales": 0,
                    "FinancialYear": FinanYr
                },
                {
                    "MonthlyTargetSales": 0,
                    "Month": str("Sep") + "-" + str(CurrYr) ,
                    "MonthlyAchievedSales": 0,
                    "FinancialYear": FinanYr
                },
                {
                    "MonthlyTargetSales": 0,
                    "Month": str("Oct") + "-" + str(CurrYr),
                    "MonthlyAchievedSales": 0,
                    "FinancialYear": FinanYr
                },
                {
                    "MonthlyTargetSales": 0,
                    "Month": str("Nov") + "-" + str(CurrYr),
                    "MonthlyAchievedSales": 0,
                    "FinancialYear": FinanYr
                },
                {
                    "MonthlyTargetSales": 0,
                    "Month": str("Dec") + "-" + str(CurrYr),
                    "MonthlyAchievedSales": 0,
                    "FinancialYear": FinanYr
                }                
            ]        
        if Target.objects.filter(SalesPersonCode_id = SalesPersonCode).exists():            
            sql_query = f"SELECT id, amount, Concat(SUBSTR(monthYear,6,7), '-', SUBSTR(monthYear,1,4)) as monYr, monthYear FROM Employee_target where SalesPersonCode_id = {SalesPersonCode} and (SUBSTR(monthYear,1,4) IN ({CurrYr}, {NextYr}) ) "            
            fytgt = Target.objects.raw(sql_query)
            for fyt in fytgt:
                month = int(fyt.monthYear.split('-')[1])
                fyTarget[month-1]['MonthlyTargetSales'] = fyt.amount                    
        if Order.objects.filter(SalesPersonCode__in = SalesPersonCode_arr).exists():
            sql_query_ord = f"SELECT id, sum(DocTotal) as OrderAchieved, SUBSTR(CreateDate,1,7) as monYr, SUBSTR(CreateDate,6,2) as month FROM Order_order where SalesPersonCode IN ({SalesPersonCode_list}) and (SUBSTR(CreateDate,1,4) IN ({CurrYr}, {NextYr})) and CancelStatus = 'csNo' group by SUBSTR(CreateDate,6,2);"
            ord_sl = Order.objects.raw(sql_query_ord)        
            for ord in ord_sl:
                fyTarget[int(ord.month)-1]['MonthlyAchievedSales'] = ord.OrderAchieved
                
            fyTarget = ser(fyTarget)
            return Response({"message": "success","status": 200,"data":fyTarget})
        else:
            fyTarget = ser(fyTarget)
            return Response({"message": "SalesPersonCode Not Found","status": 201,"data":fyTarget})  

@api_view(["POST"])
def target_anu_ach(request):
    try:
        SalesPersonCode = request.data['SalesPersonCode']        
            
        emp_obj = Employee.objects.get(SalesEmployeeCode=SalesPersonCode)
        #print(emp_obj.role)
        if emp_obj.role == 'manager':
            emps = Employee.objects.filter(reportingTo=SalesPersonCode)#.values('id', 'SalesEmployeeCode')
            SalesPersonCode_arr=[]
            SalesPersonCode_arr.append(str(SalesPersonCode))
            for emp in emps:
                SalesPersonCode_arr.append(emp.SalesEmployeeCode)
            
        elif emp_obj.role == 'admin' or emp_obj.role == 'ceo':
            emps = Employee.objects.filter(SalesEmployeeCode__gt=0)
            SalesPersonCode_arr=[]
            for emp in emps:
                SalesPersonCode_arr.append(emp.SalesEmployeeCode)
        else:
            SalesPersonCode_arr=[]
            SalesPersonCode_arr.append(str(SalesPersonCode))
        
        #print("SalesPersonCode")
        #print(SalesPersonCode_arr)
        SalesPersonCode_list = ",".join(SalesPersonCode_arr)
        #print(SalesPersonCode_list)
        
        #{"SalesPersonCode":105}
        todays_date = date.today()
        CurrYr = todays_date.year
        NextYr = todays_date.year +1
        FinanYr = str(CurrYr) + '-' + str(NextYr)
        
        TargetFyYr = []
        if Targetyr.objects.filter(SalesPersonCode_id = SalesPersonCode).exists():
            sql_query = f"SELECT id, Sum(YearTarget) YearTarget FROM Employee_targetyr where SalesPersonCode_id = {SalesPersonCode} and StartYear={CurrYr} and EndYear={NextYr}"
            #print(sql_query)
            fysl = Targetyr.objects.raw(sql_query)
            #print(fysl)
            
            sql_query_ord = f"SELECT id, SUM(NetTotal) AchievedTarget,  Count(CancelStatus) ConfirmedOrder FROM Order_order where SalesPersonCode in ({SalesPersonCode_list}) and (SUBSTR(CreateDate,1,4) IN ({CurrYr})) and CancelStatus = 'csNo' "
            ord_sl = Order.objects.raw(sql_query_ord)
            
            #for fy in fysl:
                
            finalfy = {
                "AnnualTarget": fysl[0].YearTarget,
                "AchievedTarget": 0,
                "ConfirmedOrder": 0,
                "FinancialYear": FinanYr,
            }
                
            for ord in ord_sl:
                finalfy['AchievedTarget'] = ord.AchievedTarget
                finalfy['ConfirmedOrder'] = ord.ConfirmedOrder
                    
                TargetFyYr.append(finalfy)
            return Response({"message": "success","status": 200,"data":TargetFyYr})
        else:
            TargetFyYr = [ 
                {
                    "AnnualTarget": 0,
                    "AchievedTarget": 0,
                    "ConfirmedOrder": 0,
                    "FinancialYear": FinanYr
                }
            ]       
            return Response({"message": "SalesPersonCode Not Found","status": 200,"data":TargetFyYr})
    except Exception as e:
        return Response({"message": "Error","status": 201,"data":str(e)})

#Sync Employee
@api_view(["POST"])
def sync(request):
    try:
        Date=request.data['Date']
        Time=request.data['Time']        
        filename ="Employee/SP-sync.py"
        exec(compile(open(filename, "rb").read(), filename, 'exec'), {"Date":Date, "Time":Time})
        return Response({"message": "Success","status": 200,"data":[]})
    except Exception as e:
        return Response({"message": str(e), "API_err": str(e), "status": 201, "data":{"Leads":0}})

#Employee Login API
@api_view(["POST"])
def logout(request):
    try:
        userName=request.data['userName']
        password=request.data['password']
        FCM = request.data['FCM']

        if Employee.objects.filter(userName=userName, password=password).exists():
            #print("uname")
            employee_obj = Employee.objects.get(userName=userName, password=password)
        elif Employee.objects.filter(Email=userName, password=password).exists():
            #print("email")
            employee_obj = Employee.objects.get(Email=userName, password=password)
        else:
            #print("incorrect")
            return Response({"message": "Username or password is incorrect","status": 201,"data":[]})

        employee_obj.FCM=""
        employee_obj.save()
        
        return Response({"message": "Success","status": 200,"data":[]})
            
    except Exception as e:
        return Response({"message":str(e),"status":"201","data":[{"Error":str(e)}]})

#Employee login api for service and support employee
@api_view(['POST'])
def login_support(request):
    try:
        userName=request.data['userName']
        password=request.data['password']
        FCM = request.data['FCM']

        employee_obj = ""
        if Employee.objects.filter(userName=userName, password=password).exists():
            #print("login with username")
            employee_obj = Employee.objects.get(userName=userName, password=password)

        elif Employee.objects.filter(Email=userName, password=password).exists():
            #print("login with email id")
            employee_obj = Employee.objects.get(Email=userName, password=password)
        else:
            #print("Username or password is incorrect")
            return Response({"message": "Username or password is incorrect","status": 201,"data":[], "SAP":[]})
        
        if employee_obj.Active != "tYES":
            return Response({"message": "User is InActive","status": 201,"data":[], "SAP":[]})
        
        if employee_obj.role == "salesman" or employee_obj.role == "manager" or employee_obj.role == "":
            return Response({"message": "Access Denied! Only Admin, Support Manager, Support and Engineer can have login access","status": 201,"data":[], "SAP":[]})
        
        if FCM !="":
            employee_obj.FCM = FCM
            employee_obj.save()
        employee_json = EmployeeSerializer(employee_obj)

        repoto = ""
        if employee_obj.reportingTo =="0" or employee_obj.reportingTo =="":
            repoto = "Cinntra"
            #print("User reporting to: Admin")
        else:
            repoto = str(Employee.objects.get(SalesEmployeeCode=employee_obj.reportingTo).SalesEmployeeName)
            #print(f"User reporting to: {repoto}")
        
        #print('----------- Tree ----------')
        lev = tree(employee_obj.SalesEmployeeCode)
        #print('tree: ', lev)        
        json_ob = json.dumps(employee_json.data)
        json_obj = json.loads(json_ob)

        #print('-----------Appslave----------')
        discount = 0.0
        if AppSlave.objects.filter(Level=lev).exists():
            slave_obj =  AppSlave.objects.get(Level=lev)
            #print(slave_obj.Max)
            discount = slave_obj.Max

        levdis = {
            "reportingName":repoto,
            "level":int(lev), 
            "discount": discount
        }
        json_obj.update(levdis)

        #print('-----------Items Category----------')
        if employee_obj.role == 'admin':
            div_obj = Category.objects.all() 
            div_json = CategorySerializer(div_obj, many=True).data
            #print(div_json)
            json_obj['div'] = div_json
        else:
            if employee_obj.div !="":
                div_arr = employee_obj.div.split(",")
                div_obj = Category.objects.filter(Number__in=div_arr) 
                div_json = CategorySerializer(div_obj, many=True).data
                json_obj['div'] = div_json
            else:
                json_obj['div'] = []

        with open("bridge/db.json") as f:
            db = f.read()
            data = json.loads(db)
        sapdb = data
        #sapdb = settings.SAPSESSION("api")

        return Response({"message": "Success","status": 200,"data":json_obj, "SAP":sapdb})
    except Exception as e:
        return Response({"message":str(e),"status":"201","data":[]})  

@api_view(["POST"])
def service_employee_list(request):
    try:
        SalesEmployeeCode = request.data['SalesEmployeeCode']
        if Employee.objects.filter(SalesEmployeeCode = SalesEmployeeCode, Active = "tYES").exists():
            empids = getAllReportingToIds(SalesEmployeeCode)
            emps_all = Employee.objects.filter(SalesEmployeeCode__in=empids, Active = "tYES").order_by('-id')
            emps_json = EmployeeSerializer(emps_all, many=True)
            emps_json = json.loads(json.dumps(emps_json.data))
            for employee_obj in emps_json:
                if employee_obj['div'] !="":
                    div_arr = employee_obj['div'].split(",")
                    div_obj = Category.objects.filter(Number__in=div_arr) 
                    div_json = CategorySerializer(div_obj, many=True).data
                    employee_obj['div'] = div_json
                else:
                    employee_obj['div'] = []

            return Response({"message": "Successfull","status": 200,"data":emps_json})
        else:
            return Response({"message": "error","status": 201,"data":[{"error": "Invalid or inactive Employee"}]})
    except Exception as e:
        return Response({"message": "error","status": 201,"data":[{"error": str(e)}]})


def reptoUpper(dep,subdep,level,branch):
    if int(level) ==5:
        obj = Employee.objects.filter(level=int(level)-1,branch=branch)
    elif int(level) <=4:
        obj = Employee.objects.filter(level=int(level)-1)
    else:
        obj = Employee.objects.filter(dep=dep, subdep=subdep, level=int(level)-1,branch=branch)
    return obj

#{"SalesPerson":131, "Team":"Operation"}
def HelpTeam(SalesPersonID, Team):
	subdep = GetSubdep(Team)
	emp_obj =  Employee.objects.get(SalesEmployeeCode=SalesPersonID)				
	emps = Employee.objects.filter(branch=emp_obj.branch, subdep=subdep).values('id', 'SalesEmployeeCode')
	SalesPersonID=[]
	for emp in emps:
		SalesPersonID.append(emp['SalesEmployeeCode'])
	return SalesPersonID

def ser(arr):
    """x = arr[3:]
    y = arr[:3]
    z = x+y"""
    return arr[3:] + arr[:3]


def GetTeam(SalesPersonID, Team):
	Admins = ["Admin", "Managing Director", "General Manager", "admin"]
	subdep = GetSubdep(Team)
	emp_obj =  Employee.objects.get(SalesEmployeeCode=SalesPersonID)
	print("emp_obj.role.Name :", emp_obj.role)			
	if emp_obj.role in "Sales Manager" or emp_obj.role in "Line Manager" or emp_obj.role in "Supervisor":
		emps = Employee.objects.filter(reportingTo=SalesPersonID, subdep=subdep).values('id', 'SalesEmployeeCode')
		SalesPersonID=[SalesPersonID]
		for emp in emps:
			SalesPersonID.append(emp['SalesEmployeeCode'])

	elif emp_obj.role in "Branch Manager":
		emps = Employee.objects.filter(branch=emp_obj.branch, subdep=subdep).values('id', 'SalesEmployeeCode')
		SalesPersonID=[SalesPersonID]
		for emp in emps:
			SalesPersonID.append(emp['SalesEmployeeCode'])
		
	elif emp_obj.role in Admins:
		emps = Employee.objects.filter(SalesEmployeeCode__gt=0, subdep=subdep).values('id', 'SalesEmployeeCode')
		SalesPersonID=[]
		for emp in emps:
			SalesPersonID.append(emp['SalesEmployeeCode'])
	else:
		SalesPersonID = [SalesPersonID]	
	return SalesPersonID   