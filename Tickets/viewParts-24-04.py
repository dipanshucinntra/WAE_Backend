import json
from rest_framework.decorators import api_view  
from rest_framework.response import Response
from rest_framework import status
from Category.models import Category
from Item.models import Item

from Tickets.models import History, PRAttachments, PRItems, PRStatusRemarks, PartRequest, Tickets
from Tickets.serializers import PRAttachmentsSerializer, PRItemsSerializer, PRStatusRemarksSerializer, PartRequestSerializer
from Tickets.serializers import TicketsSerializer
from Employee.models import Employee
from Employee.serializers import EmployeeSerializer
from BusinessPartner.models import BPAddresses, BPBranch, BusinessPartner
from BusinessPartner.serializers import BPAddressesSerializer, BPBranchSerializer, BusinessPartnerSerializer

from pytz import timezone
from datetime import date, datetime, timedelta

import os
from django.core.files.storage import FileSystemStorage

# Create your views here.
@api_view(['POST'])
def createParts(request):
    # try:
        requestData = request.data
        TicketId = requestData['TicketId']
        OwnerId = requestData['OwnerId']
        BillToAddress = requestData['BillToAddress']
        prItems = requestData['PRItems']

        serverDate = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d')
        estimateAmount = 0
        OwnerType = "Employee"
        if "OwnerType" in requestData:
            OwnerType = requestData['OwnerType']

        if Tickets.objects.filter(pk = TicketId).exists():
            if len(prItems) != 0:
                ticketObj = Tickets.objects.get(pk = TicketId)

                # <><><><><><><><><><><><><><>
                PartRequest(
                    TicketId = ticketObj, 
                    OwnerId = OwnerId,
                    OwnerType = OwnerType,
                    BillToAddress = BillToAddress, 
                    RequestedDate = serverDate
                ).save()
                # <><><><><><><><><><><><><><>
                PRID = PartRequest.objects.latest('id')
                # items list
                for item in prItems:
                    # <><><><><><><><><><><><><><>
                    PRItems(
                        PRID = PRID, 
                        ItemCode = item['ItemCode'],
                        ItemQty = item['ItemQty'], 
                        UnitPrice = item['UnitPrice'],
                        Comments = item['Comments'],
                        ProjectCode = item['ProjectCode']
                    ).save()
                    # <><><><><><><><><><><><><><>

                    estimateAmount = estimateAmount+float(item['UnitPrice'])

                # print(type(ticketObj.ExtWarrantyStartDate))
                CreateDate = ""
                if ticketObj.CreateDate != "":
                    if ticketObj.CreateDate != "None":
                        CreateDate = (datetime.strptime(str(ticketObj.CreateDate), '%Y-%m-%d')).date()
                
                WarrantyStartDate = ""
                if ticketObj.WarrantyStartDate != "":
                    if ticketObj.WarrantyStartDate != "None":
                        WarrantyStartDate = (datetime.strptime(str(ticketObj.WarrantyStartDate), '%Y-%m-%d')).date()
                
                WarrantyDueDate = ""
                if ticketObj.WarrantyDueDate != "":
                    if ticketObj.WarrantyDueDate != "None":
                        WarrantyDueDate = (datetime.strptime(str(ticketObj.WarrantyDueDate), '%Y-%m-%d')).date()
                
                ExtWarrantyStartDate = ""
                if ticketObj.ExtWarrantyStartDate != "":
                    if ticketObj.ExtWarrantyStartDate != "None":
                        ExtWarrantyStartDate = (datetime.strptime(str(ticketObj.ExtWarrantyStartDate), '%Y-%m-%d %H:%M:%S')).date()
                
                ExtWarrantyDueDate = ""
                if ticketObj.ExtWarrantyDueDate != "":
                    if ticketObj.ExtWarrantyDueDate != "None":
                        ExtWarrantyDueDate = (datetime.strptime(str(ticketObj.ExtWarrantyDueDate), '%Y-%m-%d %H:%M:%S')).date()

                CMCStartDate = ""
                if ticketObj.CMCStartDate != "":
                    if ticketObj.CMCStartDate != "None":
                        CMCStartDate = (datetime.strptime(str(ticketObj.CMCStartDate), '%Y-%m-%d %H:%M:%S')).date()
                
                CMCDueDate = ""
                if ticketObj.CMCDueDate != "":
                    if ticketObj.CMCDueDate != "None":
                        CMCDueDate = (datetime.strptime(str(ticketObj.CMCDueDate), '%Y-%m-%d %H:%M:%S')).date()
                
                AMCStartDate = ""
                if ticketObj.AMCStartDate != "":
                    if ticketObj.AMCStartDate != "None":
                        AMCStartDate = (datetime.strptime(str(ticketObj.AMCStartDate), '%Y-%m-%d %H:%M:%S')).date()
                
                AMCDueDate = ""
                if ticketObj.AMCDueDate != "":
                    if ticketObj.AMCDueDate != "None":
                        AMCDueDate = (datetime.strptime(str(ticketObj.AMCDueDate), '%Y-%m-%d %H:%M:%S')).date()


                print("------- Warranty ----------")
                warrantyDate = WarrantyDueDate
                warrantyStatus = "Warranty Expired"
                if WarrantyStartDate != "":
                    if CreateDate >= WarrantyStartDate and CreateDate <= WarrantyDueDate:
                        # print(f"CreateDate: {CreateDate}, WarrantyStartDate: {WarrantyStartDate}, WarrantyDueDate: {WarrantyDueDate}")
                        estimateAmount = 0
                        warrantyStatus = "Under Manufacturing  Warranty"
                        warrantyDate = WarrantyDueDate
                        print("under Warranty")
                
                if ExtWarrantyStartDate != "":
                    if CreateDate >= ExtWarrantyStartDate and CreateDate <= ExtWarrantyDueDate:
                        # print(f"CreateDate: {CreateDate}, ExtWarrantyStartDate: {ExtWarrantyStartDate}, ExtWarrantyDueDate: {ExtWarrantyDueDate}")
                        estimateAmount = 0
                        warrantyStatus = "Under Extended Warranty"
                        warrantyDate = ExtWarrantyDueDate
                        print("Under Extended Warranty")
                
                if CMCStartDate != "":    
                    if CreateDate >= CMCStartDate and CreateDate <= CMCDueDate:
                        estimateAmount = 0
                        warrantyStatus = "Under CMC"
                        warrantyDate = CMCDueDate
                        print("under CMC")
                
                if CMCStartDate != "":    
                    if CreateDate >= AMCStartDate and CreateDate <= AMCDueDate:
                        estimateAmount = 0
                        warrantyStatus = "Under AMC"
                        warrantyDate = AMCDueDate
                        print("under CMC")
                
                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                PartRequest.objects.filter(pk = PRID.id).update(
                    WarrantyStatus = warrantyStatus, 
                    EstimateAmt = estimateAmount, 
                    WarrantyDate = warrantyDate
                )
                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                History(
                    TicketId = ticketObj,
                    Type = 'Service',
                    Remarks = f'A new part request has been created with reference number {PRID.id}'
                ).save()
                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                return Response({"message":"Successfull","status":200 ,"data":[{"PRID": PRID.id}]})
            else:
                return Response({"message":"Items Empty","status":201 ,"data":[]})
        else:
          return Response({"message": "Invalid Tickets Id","status":201 ,"data":[]})  
    # except Exception as e:
    #     return Response({"message":str(e),"status":201 ,"data":[]})


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@api_view(['POST'])
def pr_attachments_upload(request):
    try:
        print('><><><><><><><><><>')
        print('pr file uplad call')
        print('><><><><><><><><><>')
        print(request)

        requestData = request.data
        PRID = requestData['PRID']
        # EmployeeId = requestData['EmployeeId']
        Attachment = request.data['Attachment']
        attechmentsImage_url = "" 
        if Attachment:
            print("in attch")
            target ='./bridge/static/image/tickets-pr'
            os.makedirs(target, exist_ok=True)
            fss = FileSystemStorage()
            file = fss.save(target+"/"+Attachment.name, Attachment)
            productImage_url = fss.url(file)
            attechmentsImage_url = productImage_url.replace('/bridge', '')
        else:
            print("no attch")
            return Response({"message":"Please add attachment","status":201 ,"data":[]})
        print(attechmentsImage_url)
        if PRAttachments.objects.filter(PRID_id = PRID).exists():
            print('update attch')
            PRAttachments(PRID_id = PRID, Attachment = attechmentsImage_url).save()
        else:
            print('insert attch')
            PRAttachments(
                PRID_id = PRID,
                Attachment = attechmentsImage_url
            ).save()

        return Response({"message":"Successfull","status":200 ,"data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

@api_view(['POST'])
def pr_approve(request):
    # try:
        PRID = request.data['PRID']
        ApproverId = request.data['ApproverId']
        Status = request.data['Status']
        Remarks = request.data['Remarks']
        serverDate = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d')
        print('==============================')

        if PartRequest.objects.filter(pk = PRID).exists():
            # print('PRID valid')
            partObj = PartRequest.objects.get(pk = PRID)
            ticketObj = Tickets.objects.get(pk = partObj.TicketId.id)
            empObj = Employee.objects.get(SalesEmployeeCode = ticketObj.AssignTo)

            if Employee.objects.filter(SalesEmployeeCode = ApproverId).exists():
                # print('ApproverId valid')
                approverEmpObj = Employee.objects.get(SalesEmployeeCode = ApproverId)
                # print(ApproverId, empObj.reportingTo)

                # if int(approverEmpObj.SalesEmployeeCode) == int(empObj.reportingTo):
                if str(approverEmpObj.role) == 'admin' or int(approverEmpObj.SalesEmployeeCode) == int(empObj.reportingTo):
                    print('reporting manager')
                    partObj.ApproverId = ApproverId
                    partObj.ApprovedDate = serverDate
                    partObj.Status = Status
                    partObj.save()

                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    PRStatusRemarks(
                        PRID = partObj,
                        SalesEmployeeCode = approverEmpObj.SalesEmployeeCode,
                        Status = Status,
                        Remarks = Remarks
                    ).save()

                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    History(
                        TicketId_id = partObj.TicketId.id,
                        Type = "Part Request",
                        Remarks = f'Ticket PR no. `{PRID}` {Status} by {approverEmpObj.firstName}'
                    ).save()

                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    return Response({"message":"Successfull","status":200 ,"data":[]})
                else:
                    print('not reporting manager')
                    return Response({"message":"User does't have access to approve part request","status":201 ,"data":[]})
            else:
                return Response({"message":"Invalid ApproverId","status":201 ,"data":[]})
        else:
            return Response({"message":"Invalid PRID","status":201 ,"data":[]})
    # except Exception as e:
    #     return Response({"message":str(e),"status":201 ,"data":[]})         


@api_view(['POST'])
def pr_remarks_history(request):
    try:
        PRID = request.data['PRID']
        allRemarks = []
        if PRStatusRemarks.objects.filter(PRID = PRID).exists():
            remarkObj = PRStatusRemarks.objects.filter(PRID = PRID)
            for obj in remarkObj:
                SalesEmployeeCode = obj.SalesEmployeeCode
                remarkJson = PRStatusRemarksSerializer(obj)
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
        return Response({"message":str(e),"status":201 ,"data":[]}) 

@api_view(['POST'])
def allParts(request):
    # try:
        PageNo = request.data['PageNo']
        MaxItem = 50
        endWith = (PageNo * MaxItem)
        startWith = (endWith - MaxItem)
        # [startWith:endWith]

        PartsObj = PartRequest.objects.all().order_by('-id')[startWith:endWith]
        # PartsJson = PartsSerializer(PartsObj, many=True)
        result = showParts(PartsObj)
        return Response({"message":"Successfull","status":200 ,"data":result})
    # except Exception as e:
    #     return Response({"message":str(e),"status":201 ,"data":[]})

@api_view(['POST'])
def filter_all_Parts(request):
    try:
        PageNo = request.data['PageNo']
        EmployeeId = request.data['EmployeeId']
        TicketId = request.data['TicketId']
        MaxItem = 50
        endWith = (PageNo * MaxItem)
        startWith = (endWith - MaxItem)

        if EmployeeId != "":
            empObjs = Employee.objects.filter(SalesEmployeeCode = EmployeeId)
            if len(empObjs) != 0 :
                # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
                # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
                # empObj = Employee.objects.get(SalesEmployeeCode = EmployeeId)
                empObj = empObjs[0]
                SalesEmployeeCode = empObj.SalesEmployeeCode
                # empids = ""
                # if str(empObj.role) == 'admin':
                #     print('---admin---')
                #     empids = Employee.objects.filter(SalesEmployeeCode__gt=0).values_list('id', flat=True)
                #     # print("empids", empids)

                # elif str(empObj.role) == 'support manager':
                #     print('---support manager---')
                #     empids = Employee.objects.filter(reportingTo = SalesEmployeeCode).values_list('id', flat=True)
                #     # print("empids", empids)

                # else:
                #     print('---- Employee ------')
                #     empids = [EmployeeId]
                empids = []
                roles = ['manager', 'salesman']
                emp_obj =  Employee.objects.get(SalesEmployeeCode=SalesEmployeeCode)
                if emp_obj.role == 'admin':
                    print('-- Admin --')
                    empids = Employee.objects.filter(SalesEmployeeCode__gt=0).exclude(role__in = roles).values_list('SalesEmployeeCode', flat=True)
                    empids = list(empids)                 
                elif emp_obj.role == 'support manager':
                    print('---support manager---')
                    empids = Employee.objects.filter(reportingTo = SalesEmployeeCode).exclude(role__in = roles).values_list('SalesEmployeeCode', flat=True)
                    empids = list(empids)
                    empids.append(SalesEmployeeCode)
                else:
                    empids=[SalesEmployeeCode]
                
                print(empids)
                # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
                # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
                ticketsObj = PartRequest.objects.filter(OwnerId__in = empids).order_by('-id')[startWith:endWith]
                result = showParts(ticketsObj)
                return Response({"message":"Successfull","status":200 ,"data":result})
            else:
                return Response({"message":"Invalid EmployeeId","status":201 ,"data":result})

        elif TicketId != "":
            # TicketId = request.data['TicketId']
            ticketsObj = PartRequest.objects.filter(TicketId = TicketId).order_by('-id')[startWith:endWith]
            result = showParts(ticketsObj)
            return Response({"message":"Successfull","status":200 ,"data":result})
        else:
            ticketsObj = PartRequest.objects.all().order_by('-id')[startWith:endWith]
            result = showParts(ticketsObj)
            return Response({"message":"Successfull","status":200 ,"data":result})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

@api_view(['POST'])
def oneParts(request):
    try:
        PartId = request.data['PartId']
        if PartRequest.objects.filter(pk = PartId).exists():
            ticketsObj = PartRequest.objects.filter(pk = PartId)
            result = showPartsDetails(ticketsObj)
            return Response({"message":"Successfull","status":200 ,"data":result})
        else:
            return Response({"message":"Error","status":201 ,"data":['id invalid']})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})


@api_view(['POST'])
def updateParts(request):
    try:
        PartsId = request.data['id']
        if PartRequest.objects.filter(pk = PartsId).exists():
            fetchObj = PartRequest.objects.get(pk = PartsId)
            fetchJson = PartRequestSerializer(fetchObj, data = request.data)
            if fetchJson.is_valid():
                fetchJson.save()
                return Response({"status":"200","message":"successfully","data":[fetchJson.data]})
            return Response(fetchJson.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"Error","status":201 ,"data":['Ticket Parts invalid']})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})


# <<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>
# <<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>
# <<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>
def showParts(objs):
    allParts = []
    for obj in objs:
        print("----------------")
        # print(obj)

        PRID = obj.id
        partobj = PartRequestSerializer(obj)
        partData = json.loads(json.dumps(partobj.data))

        # print(partData)
        # partItemObj = PRItems.objects.filter(PRID = PRID)
        # # partItemJson = PRItemsSerializer(partItemObj, many=True)
        # partItems = []
        # for itemObj in partItemObj:
        #     ItemCode = itemObj.ItemCode
        #     itemJson = PRItemsSerializer(itemObj)
        #     item = json.loads(json.dumps(itemJson.data))

        #     itemObj = Item.objects.get(ItemCode = ItemCode)
        #     item['ItemName'] = itemObj.ItemName
        #     # item['UnitPrice'] = itemObj.UnitPrice
        #     item['CategoryName'] = str(itemObj.ItemsGroupCode)
        #     item['Discount'] = str(itemObj.DiscountPercent)

        #     partItems.append(item)
        # partData['Items'] = partItems

        # ApproverId = partData['ApproverId']
        # if ApproverId != "":
        #     if Employee.objects.filter(SalesEmployeeCode = ApproverId).exists():
        #         empObj = Employee.objects.get(SalesEmployeeCode = ApproverId)
        #         empJson = EmployeeSerializer(empObj)
        #         partData['ApproverDetails'] = empJson.data
        #     else:
        #         partData['ApproverDetails'] = {}

        # if PRAttachments.objects.filter(PRID = PRID).exists():
        #     attchObj = PRAttachments.objects.filter(PRID = PRID)
        #     attchJson = PRAttachmentsSerializer(attchObj, many=True)
        #     partData['PRAttachments'] = attchJson.data
        # else:
        #     partData['PRAttachments'] = []


        if Tickets.objects.filter(pk = partData['TicketId']).exists():
            ticketobj = Tickets.objects.get(pk = partData['TicketId'])
            # ticketJson = TicketsSerializer(ticketobj)
            # partData['TicketDetails'] = ticketJson.data

            # Employee Details
            if Employee.objects.filter(SalesEmployeeCode = ticketobj.AssignTo).exists():
                empObj = Employee.objects.filter(SalesEmployeeCode = ticketobj.AssignTo).values('id', 'firstName', 'role', 'reportingTo')[0]
                empJson = EmployeeSerializer(empObj)
                partData['EmployeeDetails'] = empJson.data
            else:
                partData['EmployeeDetails'] = {}

            # Customer Details
            if BusinessPartner.objects.filter(CardCode = ticketobj.BpCardCode).exists():
                bpObj = BusinessPartner.objects.filter(CardCode = ticketobj.BpCardCode).values('id', 'CardCode', 'CardName')[0]
                bpJson = BusinessPartnerSerializer(bpObj)
                partData['BusinessPartnerDetails'] = bpJson.data
            else:
                partData['BusinessPartnerDetails'] = {}

        allParts.append(partData)
    return allParts

def showPartsDetails(objs):
    allParts = []
    for obj in objs:
        print("----------------")
        # print(obj)

        PRID = obj.id
        print(PRID)
        # ItemCode = obj.ItemCode
        # OwnerId = obj.OwnerId
        # ticketobj = obj.TicketId
        partobj = PartRequestSerializer(obj)
        partData = json.loads(json.dumps(partobj.data))
        # print(partData)


        partItemObj = PRItems.objects.filter(PRID = PRID)
        # partItemJson = PRItemsSerializer(partItemObj, many=True)
        partItems = []
        for itemObj in partItemObj:
            ItemCode = itemObj.ItemCode
            itemJson = PRItemsSerializer(itemObj)
            item = json.loads(json.dumps(itemJson.data))

            itemObj = Item.objects.get(ItemCode = ItemCode)
            item['ItemName'] = itemObj.ItemName
            # item['UnitPrice'] = itemObj.UnitPrice
            item['CategoryName'] = str(itemObj.ItemsGroupCode)
            item['Discount'] = str(itemObj.DiscountPercent)

            partItems.append(item)
        partData['Items'] = partItems

        ApproverId = partData['ApproverId']
        if ApproverId != "":
            if Employee.objects.filter(SalesEmployeeCode = ApproverId).exists():
                empObj = Employee.objects.get(SalesEmployeeCode = ApproverId)
                empJson = EmployeeSerializer(empObj)
                partData['ApproverDetails'] = empJson.data
            else:
                partData['ApproverDetails'] = {}

        if PRAttachments.objects.filter(PRID = PRID).exists():
            attchObj = PRAttachments.objects.filter(PRID = PRID)
            attchJson = PRAttachmentsSerializer(attchObj, many=True)
            partData['PRAttachments'] = attchJson.data
        else:
            partData['PRAttachments'] = []
        
        if PRStatusRemarks.objects.filter(PRID = PRID).exists():
            attchRemarks = PRStatusRemarks.objects.filter(PRID = PRID).order_by('-id')[0]
            partData['PRStatusRemarks'] = attchRemarks.Remarks
        else:
            partData['PRStatusRemarks'] = ""

        if Tickets.objects.filter(pk = partData['TicketId']).exists():
            ticketobj = Tickets.objects.get(pk = partData['TicketId'])
            # ticketJson = TicketsSerializer(ticketobj)
            # partData['TicketDetails'] = ticketJson.data

            # Employee Details
            if Employee.objects.filter(SalesEmployeeCode = ticketobj.AssignTo).exists():
                empObj = Employee.objects.get(SalesEmployeeCode = ticketobj.AssignTo)
                empJson = EmployeeSerializer(empObj)
                partData['EmployeeDetails'] = empJson.data
            else:
                partData['EmployeeDetails'] = {}

            # Customer Details
            if BusinessPartner.objects.filter(CardCode = ticketobj.BpCardCode).exists():
                bpObj = BusinessPartner.objects.get(CardCode = ticketobj.BpCardCode)
                bpJson = BusinessPartnerSerializer(bpObj)
                partData['BusinessPartnerDetails'] = bpJson.data
                if BPAddresses.objects.filter(BPCode=ticketobj.BpCardCode).exists():
                    bpaddr = BPAddresses.objects.filter(BPCode=ticketobj.BpCardCode)
                    bpaddr_json = BPAddressesSerializer(bpaddr, many=True)
                    jss0 = json.loads(json.dumps(bpaddr_json.data))
                    
                    if BPBranch.objects.filter(BPCode=ticketobj.BpCardCode,Default=1).exists():    
                        bpbr = BPBranch.objects.filter(BPCode=ticketobj.BpCardCode,Default=1)
                        bpbr_json = BPBranchSerializer(bpbr, many=True)
                        jss1 = json.loads(json.dumps(bpbr_json.data))
                        jss0 = jss0+jss1
                    partData['BusinessPartnerDetails']['BPAddresses'] = jss0
                else:
                    partData['BusinessPartnerDetails']['BPAddresses'] = {}

            else:
                partData['BusinessPartnerDetails'] = {}

        allParts.append(partData)
    return allParts

# TicketCreateDate   = ticketObj.CreateDate
# WarrantyStartDate   = ticketObj.WarrantyStartDate
# WarrantyDueDate     = ticketObj.WarrantyDueDate
# ExtWarrantyStartDate= ticketObj.ExtWarrantyStartDate
# ExtWarrantyDueDate  = ticketObj.ExtWarrantyDueDate
# AMCStartDate        = ticketObj.AMCStartDate
# AMCDueDate          = ticketObj.AMCDueDate
# CMCStartDate        = ticketObj.CMCStartDate
# CMCDueDate          = ticketObj.CMCDueDate
# datetime = datetime.strptime(strdate, '%Y-%m-%d')
# if TicketCreateDate >= WarrantyStartDate and TicketCreateDate <= WarrantyStartDate: