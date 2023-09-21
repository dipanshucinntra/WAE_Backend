from django.shortcuts import render, redirect  
from django.http import JsonResponse, HttpResponse

from datetime import datetime
from pytz import timezone
from Employee.models import *
from Notification.models import Notification
from Order.models import Order
from .models import *
from .serializers import *
from django.contrib import messages

import requests, json
from rest_framework.decorators import api_view    
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from pytz import timezone
from datetime import datetime as dt

date = dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d')
yearmonth = dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m')
time = dt.now(timezone("Asia/Kolkata")).strftime('%H:%M %p')
# Create your views here.  

#Branch Create API
@api_view(['POST'])
def create(request):
    order_id = request.data["order_id"]
    ops_revision = request.data["ops_revision"]
    client_name = request.data["client_name"]
    ops_number = request.data["ops_number"]
    amendment = request.data["amendment"]
    reason = request.data["reason"]
    open_date = request.data["open_date"]
    close_date = request.data["close_date"]
    created_by = request.data["created_by"]
    machine_sp_type= request.data['machine_sp_type']
    amd = Amendment(order_id=order_id,ops_revision=ops_revision,client_name=client_name,ops_number=ops_number,amendment=amendment,reason=reason,open_date=open_date,close_date=close_date,created_by=created_by, machine_sp_type=machine_sp_type)
    amd.save()
    
    order_obj = Order.objects.filter(id=order_id).first()
    emp_objj = Employee.objects.filter(SalesEmployeeCode=order_obj.SalesPersonCode).first()
    send_notify = Notification(Title="Amendment created", Description="Click To Check", Type="Action", Read="0", SourceType="Amendment", SourceID=amd.id, Emp=emp_objj.reportingTo, SourceTime=time, CreatedDate=date, CreatedTime=time)    
    send_notify.save()

    apprvl_emp = Employee.objects.filter(role="ceo").first()
    send_notify = Notification(Title="Amendment created", Description="Click To Check", Type="Action", Read="0", SourceType="Amendment", SourceID=amd.id, Emp=apprvl_emp.SalesEmployeeCode, SourceTime=time, CreatedDate=date, CreatedTime=time)    
    send_notify.save()

    return Response({"message":"successful","status":"200","data":[]})


@api_view(['POST'])
def all_filter_page(request):
    emp_id = request.data["Emp_id"]
    PageNo = request.data["PageNo"]
    MaxItem = request.data["MaxItem"]
    if MaxItem!="All":
        endWith = (PageNo * int(MaxItem))
        startWith = (endWith - int(MaxItem))
    SalesPersonID = emp_id
            
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
        SalesPersonID = [SalesPersonID]
        
    amd_count = Amendment.objects.filter(created_by__in=SalesPersonID).count()
    if MaxItem!="All":
        amd_data = Amendment.objects.filter(created_by__in=SalesPersonID).order_by('-id')[startWith:endWith]
    else:
        amd_data = Amendment.objects.filter(created_by__in=SalesPersonID).order_by('-id')
    amd_list = []
    for obj in amd_data:
        amd_serializer = AmendmentSerializer(obj).data
        if obj.approved_by:
            emp_name = Employee.objects.get(SalesEmployeeCode=obj.approved_by).SalesEmployeeName
        else:
            emp_name = ""
        amd_serializer["created_by_name"] = emp_name
        amd_list.append(amd_serializer)
    return Response({"message":"successful","status":"200","data":amd_list, "extra":{"total_count":amd_count}})

@api_view(['POST'])
def update(request):
    id = request.data["id"]
    order_id = request.data["order_id"]
    ops_revision = request.data["ops_revision"]
    client_name = request.data["client_name"]
    ops_number = request.data["ops_number"]
    amendment = request.data["amendment"]
    reason = request.data["reason"]
    open_date = request.data["open_date"]
    close_date = request.data["close_date"]
    created_by = request.data["created_by"]
    machine_sp_type= request.data["machine_sp_type"]
    Amendment.objects.filter(id=id).update(order_id=order_id,ops_revision=ops_revision,client_name=client_name,ops_number=ops_number,amendment=amendment,reason=reason,open_date=open_date,close_date=close_date,created_by=created_by, machine_sp_type=machine_sp_type)
    return Response({"message":"successful","status":"200","data":[]})


# @api_view(['POST'])
# def amendment_status(request):
#     emp_id = request.data["emp_id"]
#     status = request.data["status"]
#     remark = request.data["remark"]
#     id = request.data["id"]
#     amend_obj = Amendment.objects.filter(id=id).first()
#     amend_obj.approval_status = status
#     amend_obj.remark = remark
#     amend_obj.approved_by = emp_id
#     amend_obj.save()
#     return Response({"message":"successful","status":"200","data":[]})



#amendment list for approval chat
@api_view(["POST"])
def amendmentremarksHistory(request):
    try:
        qtid = request.data['id']
        allRemarks = []
        if AmendmentOrderStatusRemarks.objects.filter(Amendment_id = qtid).exists():
            remarkObj = AmendmentOrderStatusRemarks.objects.filter(Amendment_id = qtid)
            print(remarkObj)
            # remarkJson = QuotStatusRemarksSerializer(remarkObj, many=True)
            for obj in remarkObj:
                SalesEmployeeCode = obj.SalesEmployeeCode
                remarkJson = AmendmentOrderStatusRemarksSerializer(obj)
                remarkData = json.loads(json.dumps(remarkJson.data))

                if Employee.objects.filter(SalesEmployeeCode = SalesEmployeeCode).exists():
                    empObj = Employee.objects.filter(SalesEmployeeCode = SalesEmployeeCode).values_list('firstName', flat=True)[0]
                    remarkData['EmployeeName'] = str(empObj)
                else:
                    remarkData['EmployeeName'] = ""

                allRemarks.append(remarkData)
        else:
            print('nodata')
        return Response({"message":"Success","status":200,"data":allRemarks}) 
    except Exception as e:
        return Response({"message":str(e),"status":201,"data":[]})        




# #Quotation Update API
# @api_view(['POST'])
# def approve(request):
#     SalesEmployeeCode = request.data['SalesEmployeeCode']
#     Amendment_id = request.data['id']
#     FinalStatus = request.data['FinalStatus']
#     Remarks = request.data['Remarks']
#     amend_obj = Amendment.objects.filter(id=Amendment_id).first()
#     amend_obj.approval_status = FinalStatus
#     amend_obj.approved_by = SalesEmployeeCode
#     amend_obj.save()
#     remarkobj = AmendmentOrderStatusRemarks(Amendment_id = Amendment_id, SalesEmployeeCode = SalesEmployeeCode, Status = FinalStatus, Remarks = Remarks).save()
#     return Response({"message":"Success","status":200,"data":[]})


#Quotation Update API
@api_view(['POST'])
def approve(request):
    SalesEmployeeCode = request.data['SalesEmployeeCode']
    Amendment_id = request.data['id']
    FinalStatus = request.data['FinalStatus']
    Remarks = request.data['Remarks']
    amend_obj = Amendment.objects.filter(id=Amendment_id).first()
    amend_obj.approval_status = FinalStatus
    amend_obj.approved_by = SalesEmployeeCode
    amend_obj.save()
    remarkobj = AmendmentOrderStatusRemarks(Amendment_id = Amendment_id, SalesEmployeeCode = SalesEmployeeCode, Status = FinalStatus, Remarks = Remarks).save()
    if FinalStatus == "Approved":
        amendmentIdate = amend_obj.open_date
        amendmentIclosedate = amend_obj.close_date
        d1 = datetime.strptime(amendmentIdate, '%Y-%m-%dT%H:%M')
        datetimeformate = '%Y-%m-%d %H:%M:%S'
        serverDateTime = datetime.now(timezone("Asia/Kolkata")).strftime(datetimeformate)
        d2 = datetime.strptime(serverDateTime, datetimeformate)
        d3 = datetime.strptime(amendmentIclosedate, '%Y-%m-%dT%H:%M')
        if d1<d2 and d2<d3:
            Amendment.objects.filter(id=Amendment_id).update(approval_status="Process")
            Order.objects.filter(id=amend_obj.order_id).update(amendment_status="Active")
    
    order_obj = Order.objects.filter(id=amend_obj.order_id).first()
    # emp_objj = Employee.objects.filter(SalesEmployeeCode=order_obj.SalesPersonCode).first()
    send_notify = Notification(Title="Amendment status", Description="Click To Check", Type="Action", Read="0", SourceType="Amendment", SourceID=Amendment_id, Emp=order_obj.SalesPersonCode, SourceTime=time, CreatedDate=date, CreatedTime=time)    
    send_notify.save()

    return Response({"message":"Success","status":200,"data":[]})

