import calendar
import json
from unittest import result
from django.shortcuts import render
from rest_framework.decorators import api_view  
from rest_framework.response import Response
from rest_framework import status
from BusinessPartner.models import BPAddresses, BPBranch, BPEmployee, BusinessPartner
from BusinessPartner.serializers import BPAddressesSerializer, BPBranchSerializer, BPEmployeeSerializer, BusinessPartnerSerializer
from Category.models import Category
from Employee.models import Employee
from Employee import views as EmpView
from DropDown.models import *
from ServiceContract.models import *
from Employee.serializers import EmployeeSerializer
from ItemsPIR.models import CheckList

from Tickets.models import *
from Tickets.serializers import *

from global_fun import *
import os
from django.core.files.storage import FileSystemStorage

from pytz import timezone
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

now = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')

# currentDate = date.today()
# currentDay = calendar.day_name[currentDate.weekday()]  # this will return the day of a week
# currentTime = datetime.today().strftime("%I:%M %p")
# currentDateTime = f"{currentDate} {currentTime}"

# serverDateTime = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

from django.db.models import Q

# Create your views here.
@api_view(['POST'])
def create(request):
    try:
        if request.data['CreatedBy'] =="":
            return Response({"message":"CreatedBy is Required","status":201 ,"data":[]})
        
        
        
        if request.data['Data'] =="":
            DataVal = {"Status":"0","CorrectIssueType":"","ScheduledVisitDate":"","CorrectiveActions":"","RepairRequestNeeded":"","MaterialUsed":""}
        else:
            try:
                print("try convert")
                DataVal = json.dumps(request.data['Data'])
            except:
                print("already convert")
                DataVal = request.data['Data']
        
        Tickets(
            DeliveryID = request.data['DeliveryID'],
            AssignTo = request.data['AssignTo'],
            CreatedBy = request.data['CreatedBy'],
            Type = request.data['Type'],
            SubType = request.data['SubType'],
            Title = request.data['Title'],
            BpCardCode = request.data['BpCardCode'],
            BpBranch = request.data['BpBranch'],
            ContactName = request.data['ContactName'],
            ContactPhone = request.data['ContactPhone'],
            CountryCode = request.data['CountryCode'],
            AlternatePhone = request.data['AlternatePhone'],
            CountryCode1 = request.data['CountryCode1'],
            ContactEmail = request.data['ContactEmail'],
            ContactAddress = request.data['ContactAddress'],
            ProductSerialNo = request.data['ProductSerialNo'],
            ProductName = request.data['ProductName'],
            ProductCategory = request.data['ProductCategory'],
            ProductModelNo = request.data['ProductModelNo'],
            Zone = request.data['Zone'],
            Priority = request.data['Priority'],
            Status = 'Pending',
            Description = request.data['Description'],
            DurationOfService = request.data['DurationOfService'],
            SignatureStatus = request.data['SignatureStatus'],
            WarrantyStartDate = request.data['WarrantyStartDate'],
            WarrantyDueDate = request.data['WarrantyDueDate'],
            ExtWarrantyStartDate = request.data['ExtWarrantyStartDate'],
            ExtWarrantyDueDate = request.data['ExtWarrantyDueDate'],
            AMCStartDate = request.data['AMCStartDate'],
            AMCDueDate = request.data['AMCDueDate'],
            CMCStartDate = request.data['CMCStartDate'],
            CMCDueDate = request.data['CMCDueDate'],
            ManufacturingDate = request.data['ManufacturingDate'],
            ExpiryDate = request.data['ExpiryDate'],
            Datetime = now,
            UpdatedDatetime = now,
            DueDate = request.data['DueDate'],
            CreateDate = request.data['CreateDate'],
            ClosedDate = request.data['ClosedDate'],
            Data = DataVal,
        ).save()

        ticketObj = Tickets.objects.latest('id')
        print("new",ticketObj.id)

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        """
        if CheckList.objects.filter(CategoryId = request.data['ProductCategory'], Type =  request.data['Type'], ListFor = 1).exists():
            print('-----check list found----')
            checklistObj = CheckList.objects.filter(CategoryId = request.data['ProductCategory'], Type =  request.data['Type'], ListFor = 1)
            if len(checklistObj) != 0:
                for obj in checklistObj:
                    ServiceCheckList(
                        TicketId = ticketObj,
                        TaskName = obj.Name,
                        Comment = "",
                        Duration = ""
                    ).save()
                    # print('-----check created found----')
                    tempObj = ServiceCheckList.objects.latest('id')
                    print(f'checklistid:- {tempObj.id}')
        """
        if DropDown.objects.filter(DropDownName="Checklist", Field1 =  request.data['Type'], Field2 =  request.data['SubType']).exists():
            print('-----check list found----')
            checklistObj = DropDown.objects.filter(DropDownName="Checklist", Field1 =  request.data['Type'], Field2 =  request.data['SubType'])
            for obj in checklistObj:
                TicketChecklist(
                    TicketId = ticketObj.id,
                    Name = obj.DropDownValue,
                    Description = obj.DropDownDescription,
                    Data = obj.Data,
                    Comment = "",
                    Duration = "",
                    Field1 =  request.data['Type'],
                    Field2 =  request.data['SubType']
                ).save()
                # print('-----check created found----')
                tempObj = TicketChecklist.objects.latest('id')
                print(f'checklistid:- {tempObj.id}')
            
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        ticketType = request.data['Type']
        History(
            TicketId = ticketObj,
            Type = ticketType,
            Remarks = f'New Ticket {ticketType} created'
        ).save()
        print("---ok--")
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        CreatedBy = request.data['CreatedBy']
        AssignTo = request.data['AssignTo']
        
        assignByName = "Admin/Manager"

        if Employee.objects.filter(SalesEmployeeCode = CreatedBy).exists():
            empobj = Employee.objects.get(SalesEmployeeCode = CreatedBy)
            CreatedByName = empobj.SalesEmployeeName

        if Employee.objects.filter(SalesEmployeeCode = AssignTo).exists():
            empobj = Employee.objects.get(SalesEmployeeCode = AssignTo)
            assignByName = empobj.SalesEmployeeName

        # In App Notificition
        Title = "New Ticket"
        Description = f"New Ticket is created by {CreatedByName} assign to {assignByName}"
        Type = "Ticket Create"
        SourceType = "Ticket"
        SourceID = ticketObj.id
        Emp = AssignTo
        result = CreateInAppNotification(Title = Title, Description = Description, Type = Type, SourceType = SourceType, SourceID = SourceID, Emp = Emp)
        print("##########CreateInAppNotification", result)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        

        return Response({"message":"Successfull","status":200 ,"data":[{'TicketId': ticketObj.id}]})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})


@api_view(['POST'])
def all(request):
    # try:
        PageNo = int(request.data['PageNo'])
        MaxItem = 30
        endWith = (PageNo * MaxItem)
        startWith = (endWith - MaxItem)
        # [startWith:endWith]

        ticketsObj = Tickets.objects.all().order_by('-id')[startWith:endWith]
        print(ticketsObj)
        # ticketsJson = TicketsSerializer(ticketsObj, many=True)
        result = showTickets(ticketsObj)
        return Response({"message":"Successfull","status":200 ,"data":result})
    # except Exception as e:
    #     return Response({"message":str(e),"status":201 ,"data":[]})


@api_view(['POST'])
def one(request):
    try:
        TicketId = request.data['id']
        if Tickets.objects.filter(pk = TicketId).exists():
            ticketsObj = Tickets.objects.filter(pk = TicketId)
            # ticketsJson = TicketsSerializer(ticketsObj, many=True)
            result = showTickets(ticketsObj)
            return Response({"message":"Successfull","status":200 ,"data":result})
        else:
            return Response({"message":"Error","status":201 ,"data":['id invalid']})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

@api_view(['POST'])
def filter_all(request):
    try:

        PageNo = request.data['PageNo']
        MaxItem = 30
        endWith = (PageNo * MaxItem)
        startWith = (endWith - MaxItem)
        # [startWith:endWith]

        BpCardCode = request.data['BpCardCode']
        ticketsObj = Tickets.objects.filter(BpCardCode = BpCardCode).exclude(Status="Dormant").order_by('-id')[startWith:endWith]
        # ticketsJson = TicketsSerializer(ticketsObj, many=True)
        result = showTickets(ticketsObj)
        return Response({"message":"Successfull","status":200 ,"data":result})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})


# ticket list item seial number wise
@api_view(['POST'])
def item_wise_tickets(request):
    try:
        ProductSerialNo = request.data['ProductSerialNo']
        ticketsObj = Tickets.objects.filter(ProductSerialNo = ProductSerialNo).order_by('-id')
        result = showTickets(ticketsObj)
        return Response({"message":"Successfull","status":200 ,"data":result})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})



@api_view(['POST'])
def update(request):
    try:
        TicketId = request.data['id']
        #request.data['Data'] = json.dumps(request.data['Data'])
        print(type(request.data['Data']))
        if type(request.data['Data']) == dict:
            print("try convert")
            request.data['Data'] = json.dumps(request.data['Data'])

        if Tickets.objects.filter(pk = TicketId).exists():
            fetchObj = Tickets.objects.get(pk = TicketId)
            fetchJson = TicketsSerializer(fetchObj, data = request.data)
            if fetchJson.is_valid():
                fetchJson.save()

                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                ticketType = request.data['Type']
                History(
                    TicketId_id = TicketId,
                    Type = ticketType,
                    Remarks = f'Ticket Update'
                ).save()
                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

                return Response({"status":"200","message":"successfully","data":[fetchJson.data]})
            return Response(fetchJson.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"Error","status":201 ,"data":['TicketId invalid']})        
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})


@api_view(['POST'])
def assign_to(request):
    try:
        TicketId = request.data['TicketId']
        EmployeeId = request.data['EmployeeId']

        if Tickets.objects.filter(pk = TicketId).exists():
            Tickets.objects.filter(pk = TicketId).update(AssignTo = EmployeeId, Status = "Pending", TicketStatus = "Pending")

            employeeObj = Employee.objects.get(SalesEmployeeCode = EmployeeId)
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            History(
                TicketId_id = TicketId,
                Type = "Service",
                Remarks = f'Ticket assign to {employeeObj.firstName}'
            ).save()
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            assignByName = "Admin/Manager"

            if Employee.objects.filter(SalesEmployeeCode = EmployeeId).exists():
                empobj = Employee.objects.get(SalesEmployeeCode = EmployeeId)
                assignByName = empobj.SalesEmployeeName

            # In App Notificition
            Title = "New Ticket"
            Description = f"New Ticket is assign to {assignByName}"
            Type = "Ticket Assign"
            SourceType = "Ticket"
            SourceID = TicketId
            Emp = EmployeeId
            result = CreateInAppNotification(Title = Title, Description = Description, Type = Type, SourceType = SourceType, SourceID = SourceID, Emp = Emp)
            print("##########CreateInAppNotification", result)
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            return Response({"message":"Successfull","status":200 ,"data":[]})
        else:
            return Response({"message":"Error","status":201 ,"data":['TicketId invalid']})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

@api_view(['POST'])
def reassign_to(request):
    try:
        TicketId = request.data['TicketId']
        EmployeeId = request.data['EmployeeId']
        AssignTo = request.data['AssignTo']
        Type = request.data['Type']
        Remarks = request.data['Remarks']

        if Tickets.objects.filter(pk = TicketId).exists():
            PrevType = Tickets.objects.get(pk = TicketId).Type            
            
            Tickets.objects.filter(pk = TicketId).update(AssignTo = AssignTo, Status = "Pending", TicketStatus = "Pending", Type=Type)
            
            #Hold old checklist
            if TicketChecklist.objects.filter(TicketId = TicketId).exists():
                tktChecklist = TicketChecklist.objects.filter(TicketId = TicketId)
                for tc in tktChecklist:
                    print(tc)
                    tc.Status=2
                    tc.save()

            
            if DropDown.objects.filter(DropDownName="Checklist", Field1 =  Type).exists():
                print('-----check list found----')
                checklistObj = DropDown.objects.filter(DropDownName="Checklist", Field1 =  Type)
                for obj in checklistObj:
                    TicketChecklist(
                        TicketId = TicketId,
                        Name = obj.DropDownValue,
                        Description = obj.DropDownDescription,
                        Data = obj.Data,
                        Comment = "",
                        Duration = ""
                    ).save()
                    # print('-----check created found----')
                    tempObj = TicketChecklist.objects.latest('id')
                    print(f'checklistid:- {tempObj.id}')
            Conversation(
                TicketId_id = TicketId,
                OwnerId = EmployeeId,
                OwnerType = "Employee",
                Message = Remarks,
                Type = "Public"
            ).save()


            employeeObj1 = Employee.objects.get(SalesEmployeeCode = EmployeeId)
            employeeObj2 = Employee.objects.get(SalesEmployeeCode = AssignTo)
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            History(
                TicketId_id = TicketId,
                PrevType = PrevType,
                Type = Type,
                Remarks = f'Ticket reassign to {employeeObj2.firstName} by {employeeObj1.firstName}'
            ).save()
            Tickets.objects.filter(pk = TicketId).update(TypeChange="YES")
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            assignByName = "Admin/Manager"

            if Employee.objects.filter(SalesEmployeeCode = EmployeeId).exists():
                empobj = Employee.objects.get(SalesEmployeeCode = EmployeeId)
                CreatedByName = empobj.SalesEmployeeName

            if Employee.objects.filter(SalesEmployeeCode = AssignTo).exists():
                empobj = Employee.objects.get(SalesEmployeeCode = AssignTo)
                assignByName = empobj.SalesEmployeeName

            # In App Notificition
            Title = "New Ticket"
            Description = f"New Ticket is created by {CreatedByName} assign to {assignByName}"
            Type = "Ticket Re-Assign"
            SourceType = "Ticket"
            SourceID = TicketId
            Emp = AssignTo
            result = CreateInAppNotification(Title = Title, Description = Description, Type = Type, SourceType = SourceType, SourceID = SourceID, Emp = Emp)
            print("##########CreateInAppNotification", result)
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            return Response({"message":"Successfull","status":200 ,"data":[]})
        else:
            return Response({"message":"Error","status":201 ,"data":['TicketId invalid']})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@api_view(['POST'])
def status_update(request):
    try:
        TicketId = request.data['TicketId']
        Status = request.data['Status']
        if Tickets.objects.filter(pk = TicketId).exists():
            Tickets.objects.filter(pk = TicketId).update(Status = Status)

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            History(
                TicketId_id = TicketId,
                Type = "Service",
                Remarks = f'Ticket status update to {Status}'
            ).save()
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            return Response({"message":"Successfull","status":200 ,"data":[]})
        else:
            return Response({"message":"Error","status":201 ,"data":['TicketId invalid']})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@api_view(['POST'])
def accept_reject_ticket(request):
    try:
        TicketId = request.data['TicketId']
        TicketStatus = request.data['TicketStatus']
        EmployeeId = request.data['EmployeeId']
        serverDateTime = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')
        if Tickets.objects.filter(pk = TicketId).exists():
            tkt = Tickets.objects.get(pk = TicketId)
            if TicketStatus == "Accepted":
                print("Ticket accepted")
                Tickets.objects.filter(pk = TicketId).update(TicketStatus = TicketStatus, Status = "Assigned", AcceptedAt=serverDateTime)
            elif TicketStatus == "Rejected":
                Tickets.objects.filter(pk = TicketId).update(TicketStatus = TicketStatus, Status = "Pending")
                print("Ticket Rejcted")
            else:
                print("Ticket still pending")
                
            
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            employeeObj = Employee.objects.get(SalesEmployeeCode = EmployeeId)
            History( TicketId_id = TicketId, Type = tkt.Type, Remarks = f'Ticket {TicketStatus} by {employeeObj.firstName}').save()
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            
            return Response({"message":"Successfull","status":200 ,"data":[]})
        else:
            return Response({"message":"Error","status":201 ,"data":['TicketId invalid']})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@api_view(['POST'])
def ticket_start_end(request):
    try:
        requestData = request.data
        TicketId = requestData['TicketId']
        EmployeeId = requestData['EmployeeId']

        serverDateTime = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')
        
        if Tickets.objects.filter(pk = TicketId).exists():
            tkt = Tickets.objects.get(pk = TicketId)
            # serverDateTime
            if "TicketStartDate" in requestData:
                ticketStartDate = requestData['TicketStartDate']
                if tkt.Type =="Man-Trap":
                    if RescueHistory.objects.filter(TicketId_id=TicketId, Status="Reached").exists():
                        Tickets.objects.filter(pk = TicketId).update(TicketStartDate = serverDateTime, Status= "In Progress")                
                        RescueHistory(TicketId_id=TicketId, Status="Work in Progress").save()
                    else:
                        return Response({"message":"Update Rescue Status","status":201 ,"data":[]})
                else:
                    Tickets.objects.filter(pk = TicketId).update(TicketStartDate = serverDateTime, Status= "In Progress")
                
                employeeObj = Employee.objects.get(SalesEmployeeCode = EmployeeId)
                # History( TicketId_id = TicketId, Type = "Service", Remarks = f'Ticket start at {serverDateTime} by {employeeObj.firstName}').save()
                History( TicketId_id = TicketId, Type = tkt.Type, Remarks = f'Ticket start by {employeeObj.firstName}').save()
                History( TicketId_id = TicketId, Type = tkt.Type, Remarks = f'Ticket is `In Progress` by {employeeObj.firstName}').save()
                return Response({"message":"Successfull","status":200 ,"data":[]})

            elif "TicketEndDate" in requestData:
                ticketEndDate = requestData['TicketEndDate']
                # Tickets.objects.filter(pk = TicketId).update(TicketEndDate = serverDateTime, Status= "Resolved")
                Tickets.objects.filter(pk = TicketId).update(TicketEndDate = serverDateTime)
                employeeObj = Employee.objects.get(SalesEmployeeCode = EmployeeId)
                History( TicketId_id = TicketId, Type = tkt.Type, Remarks = f'Ticket end by {employeeObj.firstName}').save()
                # History( TicketId_id = TicketId, Type = "Service", Remarks = f'Ticket Resolved by {employeeObj.firstName}').save()
                return Response({"message":"Successfull","status":200 ,"data":[]})
            else:
                return Response({"message":"TicketStartDate or TicketEndDate key missing","status":201 ,"data":[]})
        else:
            return Response({"message":"Wrong Ticket Id","status":201 ,"data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@api_view(['POST'])
def ticket_reset(request):
    try:
        requestData = request.data
        TicketId = requestData['TicketId']
        EmployeeId = requestData['EmployeeId']
        if Tickets.objects.filter(pk = TicketId).exists():
            Tickets.objects.filter(pk = TicketId).update(TicketStartDate="", TicketEndDate = "", Status= "Assigned")
            employeeObj = Employee.objects.get(SalesEmployeeCode = EmployeeId)
            # History( TicketId_id = TicketId, Type = "Service", Remarks = f'Ticket start at {serverDateTime} by {employeeObj.firstName}').save()
            History( TicketId_id = TicketId, Type = "Service", Remarks = f'Ticket reset by {employeeObj.firstName}').save()
            return Response({"message":"Successfull","status":200 ,"data":[]})
        else:
            return Response({"message":"Wrong Ticket Id","status":201 ,"data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@api_view(['POST'])
def ticket_signin_confirm(request):
    try:
        requestData = request.data
        TicketId = requestData['TicketId']
        EmployeeId = requestData['EmployeeId']
        Attachments = requestData['SignatureFile']
        CustomerFeedback = requestData['CustomerFeedback']
        Observation = requestData['Observation']
        if Tickets.objects.filter(pk = TicketId).exists():
            if Tickets.objects.filter(pk = TicketId, AssignTo = EmployeeId).exists():
                attechmentsImage_url = ""
                if Attachments:
                    target ='./bridge/static/image/tickets-customer-signature'
                    os.makedirs(target, exist_ok=True)
                    fss = FileSystemStorage()
                    file = fss.save(target+"/"+Attachments.name, Attachments)
                    productImage_url = fss.url(file)
                    attechmentsImage_url = productImage_url.replace('/bridge', '')
            
                Tickets.objects.filter(pk = TicketId).update(
                    SignatureStatus = "Confirm", 
                    Status= "Resolved",
                    SignatureFile = attechmentsImage_url,
                    CustomerFeedback = CustomerFeedback,
                    Observation = Observation
                )
                employeeObj = Employee.objects.get(SalesEmployeeCode = EmployeeId)
                History( TicketId_id = TicketId, Type = "Service", Remarks = f'Ticket sign in confirm and resolve by {employeeObj.firstName}').save()
                return Response({"message":"Successfull","status":200 ,"data":[]})
                
            else:
                return Response({"message":"User does not have access to sign in confirm this ticket","status":201 ,"data":[]})
        else:
            return Response({"message":"Wrong Ticket Id","status":201 ,"data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@api_view(['POST'])
def customer_pir_upload(request):
    try:
        requestData = request.data
        TicketId = requestData['TicketId']
        EmployeeId = requestData['EmployeeId']
        Attachments = request.data['Attachments']
        if Tickets.objects.filter(pk = TicketId).exists():
            if Attachments:
                target ='./bridge/static/image/tickets-pir'
                os.makedirs(target, exist_ok=True)
                fss = FileSystemStorage()
                file = fss.save(target+"/"+Attachments.name, Attachments)
                productImage_url = fss.url(file)
                attechmentsImage_url = productImage_url.replace('/bridge', '')

                Tickets.objects.filter(pk = TicketId).update(CustomerPIR = attechmentsImage_url)

                # >>>> History >>>> History >>>> History >>>> History >>>> History >>>>
                employeeObj = Employee.objects.get(SalesEmployeeCode = EmployeeId)
                History(
                    TicketId_id = TicketId, 
                    Type = "Service", 
                    Remarks = f'Customer PIR {attechmentsImage_url} Uploaded by {employeeObj.firstName}'
                ).save()
                # >>>> History >>>> History >>>> History >>>> History >>>> History >>>>

                return Response({"message":"Successfull","status":200 ,"data":[]})
            else:
                return Response({"message":"Please add attachments","status":201 ,"data":[]})
        else:
            return Response({"message":"Wrong Ticket Id","status":201 ,"data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})
        
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@api_view(['POST'])
def tickets_dashboard(request):
    try:
        EmployeeId = request.data['EmployeeId']
        if Employee.objects.filter(SalesEmployeeCode = EmployeeId).exists():
            # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            print('--- Employee Role ---')
            empids = []
            roles = ['manager', 'salesman']
            emp_obj = Employee.objects.filter(SalesEmployeeCode = EmployeeId)[0]
            SalesEmployeeCode = emp_obj.SalesEmployeeCode
            print(emp_obj.role)
            if emp_obj.role == 'admin':
                print('-- Admin --')
                empids = Employee.objects.filter(SalesEmployeeCode__gt=0).exclude(role__in = roles).values_list('SalesEmployeeCode', flat=True)
                empids = list(empids)
                # empids.append(SalesEmployeeCode)                   
            elif emp_obj.role == 'manager':
                print('---support manager---')
                empids = Employee.objects.filter(reportingTo = SalesEmployeeCode).exclude(role__in = roles).values_list('SalesEmployeeCode', flat=True)
                empids = list(empids)
                empids.append(SalesEmployeeCode)
            else:
                empids=[SalesEmployeeCode]

            print(empids) 
            # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            allticketsCount = Tickets.objects.filter(AssignTo__in = empids).count()
            # newTicketsCount = Tickets.objects.filter(Status = 'New').count()
            pendingTicketsCount = Tickets.objects.filter(AssignTo__in = empids, Status = 'Pending').count()
            assignedTicketsCount = Tickets.objects.filter(AssignTo__in = empids, Status = 'Assigned').count()
            inProgressTicketsCount = Tickets.objects.filter(AssignTo__in = empids, Status = 'In Progress').count()
            resolvedTicketsCount = Tickets.objects.filter(AssignTo__in = empids, Status = 'Resolved').count()
            # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            ticketsCountContext = {
                # "New": newTicketsCount,
                "All": allticketsCount,
                "Pending": pendingTicketsCount,
                "Assigned": assignedTicketsCount,
                "In_Progress": inProgressTicketsCount,
                "Resolved": resolvedTicketsCount,
            }
            # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            return Response({"message":"Successfull","status":200 ,"data":ticketsCountContext})
        else:
            return Response({"message":"Invalid SalesEmployeeCode","status":201 ,"data":[]})

    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

        
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@api_view(['POST'])
def tickets_bp_dashboard(request):
    try:
        CardCode = request.data['CardCode']
        if BusinessPartner.objects.filter(CardCode = CardCode).exists():
            
            # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            allticketsCount = Tickets.objects.filter(BpCardCode = CardCode).count()
            pendingTicketsCount = Tickets.objects.filter(BpCardCode = CardCode, Status = 'Pending', TicketStatus = 'Pending').count()
            inProgressTicketsCount = Tickets.objects.filter(BpCardCode = CardCode, Status = 'In Progress').count()
            resolvedTicketsCount = Tickets.objects.filter(BpCardCode = CardCode, Status = 'Resolved').count()
            assignedTicketsCount = Tickets.objects.filter(BpCardCode = CardCode, Status = 'Assigned').count()
            acceptedTicketsCount = Tickets.objects.filter(BpCardCode = CardCode, Status = 'Assigned', TicketStatus = 'Accepted').count()
            rejctedTicketsCount = Tickets.objects.filter(BpCardCode = CardCode, Status = 'Pending', TicketStatus = 'Rejected').count()
            # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            ticketsCountContext = {
                # "New": newTicketsCount,
                "All": allticketsCount,
                "Pending": pendingTicketsCount,
                "Assigned": assignedTicketsCount,
                "In_Progress": inProgressTicketsCount,
                "Resolved": resolvedTicketsCount,
                "Accepted": acceptedTicketsCount,
                "Rejected": rejctedTicketsCount,
            }
            # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            return Response({"message":"Successfull","status":200 ,"data":ticketsCountContext})
        else:
            return Response({"message":"BP CardCode invalid","status":201 ,"data":[]})

    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@api_view(['POST'])
def filterbykey(request):
    try:
        requestData = request.data

        EmployeeId = requestData['EmployeeId']
        PageNo = requestData['PageNo']
        MaxItem = 10
        endWith = (PageNo * MaxItem)
        startWith = (endWith - MaxItem)
        # [startWith:endWith]

        if Employee.objects.filter(SalesEmployeeCode = EmployeeId).exists():
            #empids = EmpView.GetTeam(EmployeeId,"Operation")            
            #empids = getAllReportingToIdsSubdep(EmployeeId,"Operation")            
            empids = getAllReportingToIds(EmployeeId)            
            # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

            ticketsObj = ""
            if 'Status' in requestData:
                print('--- status key ---')
                Status = requestData['Status']
                if Status != "":
                    ticketsObj = Tickets.objects.filter(AssignTo__in = empids, Status = Status).exclude(Status='Dormant').order_by('-id')[startWith:endWith]
                else:
                    ticketsObj = Tickets.objects.filter(AssignTo__in = empids).exclude(Status='Dormant').order_by('-id')[startWith:endWith]

            elif 'FromDate' in requestData and 'ToDate' in requestData:
                print('--- Date key ---')
                FromDate = requestData['FromDate']
                ToDate = requestData['ToDate']
                ToDate = datetime.strptime(ToDate, '%Y-%m-%d')
                # ToDate = ToDate + timedelta(days=1)
                ticketsObj = Tickets.objects.filter(AssignTo__in = empids, CreateDate__gte = FromDate, CreateDate__lte = ToDate).exclude(Status='Dormant').order_by('-id')[startWith:endWith]
                
            elif 'Priority' in requestData:
                print('--- Priority key ---')
                Priority = requestData['Priority']
                ticketsObj = Tickets.objects.filter(AssignTo__in = empids, Priority = Priority).exclude(Status='Dormant').order_by('-id')[startWith:endWith]
            elif 'Type' in requestData:
                print('--- Type key ---')
                Type = requestData['Type']
                ticketsObj = Tickets.objects.filter(AssignTo__in = empids, Type = Type).exclude(Status='Dormant').order_by('-id')[startWith:endWith]
            else:
                print('--- only by employee id ---')
                ticketsObj = Tickets.objects.filter(AssignTo__in = empids).exclude(Status='Dormant').order_by('-id')[startWith:endWith]
            
            result = showTickets(ticketsObj)
            return Response({"message":"Successfull","status":200 ,"data":result})
        else:
            return Response({"message":"Invalid EmployeeId","status":201 ,"data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]}) 

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@api_view(['POST'])
def searchInTickets(request):
    # try:
        SearchText = request.data['SearchText']
        EmployeeId = request.data['EmployeeId']
        PageNo = request.data['PageNo']

        MaxItem = 10
        endWith = (PageNo * MaxItem)
        startWith = (endWith - MaxItem)
        # [startWith:endWith]
        
        SearchText = str(SearchText).strip()
        if SearchText != "":
            if Employee.objects.filter(SalesEmployeeCode = EmployeeId).exists():
                
                # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
                # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
                empObj = Employee.objects.get(SalesEmployeeCode = EmployeeId)
                SalesEmployeeCode = empObj.SalesEmployeeCode
                
                empids = getAllReportingToIds(EmployeeId)            

                # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
                # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
                # list all the bp CardCode
                bpCardCodeList = BusinessPartner.objects.filter(
                    Q(CardName__icontains = SearchText) |
                    Q(ContactPerson__icontains = SearchText) |
                    Q(Phone1__icontains = SearchText)
                ).values_list('CardCode', flat=True)
                
                employeeCodes = Employee.objects.filter(
                    Q(SalesEmployeeName__icontains = SearchText)
                ).values_list('SalesEmployeeCode', flat=True)

                ticketsObj = Tickets.objects.filter(
                    Q(AssignTo__in = empids) & 
                    Q(
                        Q(id__icontains = SearchText) |
                        Q(BpCardCode__in = bpCardCodeList) |
                        Q(ContactName__icontains = SearchText) |
                        Q(ContactPhone__icontains = SearchText) |
                        Q(ContactAddress__icontains = SearchText) |
                        Q(ContactEmail__icontains = SearchText) |
                        Q(ProductSerialNo__icontains = SearchText) |
                        Q(ProductName__icontains = SearchText) |
                        Q(Type__icontains = SearchText) |
                        Q(Priority__icontains = SearchText) |
                        Q(CreateDate__icontains = SearchText) |
                        Q(AssignTo__in = employeeCodes)
                    )
                ).order_by('-id')[startWith:endWith]

                # print("<><><><><><><><><><><><><><><><")
                # print(ticketsObj.query)
                # print("<><><><><><><><><><><><><><><><")
                result = showTickets(ticketsObj)
                return Response({"message":"Successfull","status":200 ,"data":result})
            else:
                return Response({"message":"Invalid EmployeeId","status":201 ,"data":[]})
        else:
            return Response({"message":"Successfull","status":200 ,"data":[]})
    # except Exception as e:
    #     return Response({"message":str(e),"status":201 ,"data":[]}) 




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# tickets descriptions functions
def showTickets(objs):
    alldata = []
    for obj in objs:
        ticketId = obj.id
        CardCode = obj.BpCardCode
        AssignTo = obj.AssignTo
        MNo = obj.DeliveryID
        ContractType = obj.ContractType
        CreatedBy = obj.CreatedBy
        ticketJson = TicketsSerializer(obj)
        ticketData = json.loads(json.dumps(ticketJson.data))
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        TicketStartDate = obj.TicketStartDate
        TicketEndDate = obj.TicketEndDate
        # DurationOfService = obj.DurationOfService

        datetimeformate = '%Y-%m-%d %H:%M:%S'
        serverDateTime = datetime.now(timezone("Asia/Kolkata")).strftime(datetimeformate)
        if TicketStartDate != "":
            d1 = datetime.strptime(TicketStartDate, datetimeformate)
            d2 = datetime.strptime(serverDateTime, datetimeformate)
            if TicketEndDate !="":
                d2 = datetime.strptime(TicketEndDate, datetimeformate)
                
            diff = d2 - d1
            # diff_minutes = (diff.days * 24 * 60) + (diff.seconds/60)
            ticketData['DurationOfService'] = diff.total_seconds()


        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if obj.ProductCategory != "":
            ProductCategory = obj.ProductCategory
            if Category.objects.filter(Number = ProductCategory).exists():
                catObj = Category.objects.get(Number = ProductCategory)
                ticketData['ProductCategoryName'] = catObj.GroupName
            else:
                ticketData['ProductCategoryName'] = ""
        else:
            ticketData['ProductCategoryName'] = ""
        # >>>>>>>>>>>>>>>>>>>>>>>>>> Assign To Details >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if AssignTo != "":
            if Employee.objects.filter(SalesEmployeeCode = AssignTo).exists():
                empObj = Employee.objects.get(SalesEmployeeCode = AssignTo)
                empJson = EmployeeSerializer(empObj)
                ticketData['AssignToDetails'] = empJson.data
            else:
                ticketData['AssignToDetails'] = {}
        else:
            ticketData['AssignToDetails'] = {}

        # >>>>>>>>>>>>>>>>>>>>>>>>>> MasterServiceContract ID >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if ContractType != "":
            if MasterServiceContract.objects.filter(MNo = MNo).exists():
                MSC = MasterServiceContract.objects.get(MNo = MNo).id
                ticketData['MasterServiceContract'] = MSC
            else:
                ticketData['MasterServiceContract'] = ""
        else:
            ticketData['MasterServiceContract'] = ""

        # >>>>>>>>>>>>>>>>>>>>>>>>>> ServiceContact ID >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if ContractType != "":
            if ServiceContract.objects.filter(MNo = MNo).exists():
                #SC = ServiceContract.objects.get(MNo = MNo).id
                SC = ServiceContract.objects.filter(MNo = MNo).values("id","FromDate", "ToDate")
                ticketData['ServiceContract'] = SC
            else:
                ticketData['ServiceContract'] = ""
        else:
            ticketData['ServiceContract'] = ""
            
        # >>>>>>>>>>>>>>>>>>>>>>>> CreatedBy >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if CreatedBy != "":
            if Employee.objects.filter(SalesEmployeeCode = CreatedBy).exists():
                empObj = Employee.objects.get(SalesEmployeeCode = CreatedBy)
                empJson = EmployeeSerializer(empObj)
                ticketData['CreatedByDetails'] = empJson.data
            else:
                ticketData['CreatedByDetails'] = {}
        else:
            ticketData['CreatedByDetails'] = {}
        # >>>>>>>>>>>>>>>>>>>>>>>>> BP Details >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if BusinessPartner.objects.filter(CardCode = CardCode).exists():
            bpObj = BusinessPartner.objects.get(CardCode = CardCode)
            bpJson = BusinessPartnerSerializer(bpObj)
            ticketData['BusinessPartner'] = json.loads(json.dumps(bpJson.data))
            # bp address
            if BPAddresses.objects.filter(BPCode=CardCode).exists():
                bpaddr = BPAddresses.objects.filter(BPCode=CardCode)
                bpaddr_json = BPAddressesSerializer(bpaddr, many=True)
                jss0 = json.loads(json.dumps(bpaddr_json.data))
                
                if BPBranch.objects.filter(BPCode=CardCode,Default=1).exists():    
                    bpbr = BPBranch.objects.filter(BPCode=CardCode,Default=1)
                    bpbr_json = BPBranchSerializer(bpbr, many=True)
                    jss1 = json.loads(json.dumps(bpbr_json.data))
                    jss0 = jss0+jss1

                ticketData['BusinessPartner']['BPAddresses'] = jss0
            if BPEmployee.objects.filter(CardCode=CardCode).exists():
                bpaddr = BPEmployee.objects.filter(CardCode=CardCode)
                bpaddr_json = BPEmployeeSerializer(bpaddr, many=True)
                ticketData['BusinessPartner']['BPEmployee'] = json.loads(json.dumps(bpaddr_json.data))
        else:
            ticketData['BusinessPartner'] = {}
        alldata.append(ticketData)
    return alldata

def auto_ticket(project, item, BP, cur_stage, next_stage, tkt_type):
    if int(next_stage.StageAssign) > 0:
        assign = next_stage.StageAssign
    elif int(next_stage.StageOwner) > 0:
        assign = next_stage.StageOwner
    else:
        assign = project.project_owner
    print("assign", assign)
    print("data", next_stage.Data)
        
    Tickets(
            DeliveryID = next_stage.id,
            Stageno = next_stage.Stageno,
            Data = next_stage.Data,
            AssignTo = assign,
            CreatedBy = project.project_owner,
            Type = tkt_type.Type,
            SubType = tkt_type.SubType,
            BpCardCode = BP.CardCode,
            ContactName = BP.ContactPerson,
            ContactPhone = BP.Phone1,
            CountryCode = BP.CountryCode,
            ProductName = item.ItemDescription,
            ProductSerialNo = item.ItemSerialNo,
            ProductCategory = item.ProjectCode,            
            ContactEmail = BP.EmailAddress,
            Zone = BP.Zone,
            Priority = "Medium",
            Status = 'Pending',
        ).save()
    ticketObj = Tickets.objects.latest('id')
    
    # >>>>>>>>>>>>>> assign checklist >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    if DropDown.objects.filter(DropDownName="Checklist", Field1 =  tkt_type.Type, Field2 =  tkt_type.SubType).exists():
        print('-----check list found----')
        checklistObj = DropDown.objects.filter(DropDownName="Checklist", Field1 =  tkt_type.Type, Field2 =  tkt_type.SubType)
        print(checklistObj)
        if len(checklistObj) != 0:
            for obj in checklistObj:
                TicketChecklist(
                    TicketId = ticketObj.id,
                    Name = obj.DropDownValue,
                    Description = obj.DropDownDescription,
                    Data = obj.Data,
                    Comment = "",
                    Duration = ""
                ).save()
                # print('-----check created found----')
                tempObj = TicketChecklist.objects.latest('id')
                print(f'checklistid:- {tempObj.id}')
        
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        ticketType = tkt_type.Type
        History(
            TicketId_id = ticketObj.id,
            Type = ticketType,
            Remarks = f'New Ticket {ticketType} created'
        ).save()
        ticketObj = Tickets.objects.latest('id')
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    print(ticketObj)
    return ticketObj

def sc_ticket (request, type):
    
    try:
        print(type['Type'])
        
        fq = get_fq(request.data['Frequency'])
        print("fq",fq)
            
        days = days_between(request.data['FromDate'], request.data['ToDate'])
        yr = round(days/365)
        print("yr",yr)
        fq_loop = fq * yr    
        print("fq_loop",fq_loop)
        
        SysScheduleDate = request.data['FromDate']

        days = days_between(str(date.today()), SysScheduleDate)
        print("days", days)
        if days < 7:    
            Status = "Pending"
            Priority = "High"
        else:
            Status = "Dormant"
            Priority = "Medium"        
        
    
    
        for i in range(0, fq_loop):
            if i ==0:
                FromDate = datetime.strptime(request.data['FromDate'], "%Y-%m-%d")                
                DueDate = FromDate + relativedelta(days=15)
                DueDate = str(DueDate.strftime("%Y-%m-%d"))                    
                Status = Status
                Priority = Priority
                SysScheduleDate = SysScheduleDate
                AppScheduleDate = SysScheduleDate
                print("if AppScheduleDate", AppScheduleDate)
            else:
                Status="Dormant"
                Priority = "Medium"
                
                AppScheduleDate = datetime.strptime(AppScheduleDate, "%Y-%m-%d")                

                #mydate = AppScheduleDate
                print("else AppScheduleDate", str(AppScheduleDate))
                if request.data['Frequency'].lower()=="yearly":                    
                    AppScheduleDate = AppScheduleDate + relativedelta(months=12)
                    DueDate = AppScheduleDate + relativedelta(days=15)
                    DueDate = str(DueDate.strftime("%Y-%m-%d"))                    
                    AppScheduleDate = str(AppScheduleDate.strftime("%Y-%m-%d"))
                    SysScheduleDate = AppScheduleDate
                else:
                    mn = round(12/fq)
                    print("mn",mn)
                    AppScheduleDate = AppScheduleDate + relativedelta(months=mn)
                    DueDate = AppScheduleDate + relativedelta(days=15)
                    DueDate = str(DueDate.strftime("%Y-%m-%d"))                    
                    AppScheduleDate = str(AppScheduleDate.strftime("%Y-%m-%d"))
                    SysScheduleDate = AppScheduleDate

                
            print("save AppScheduleDate", AppScheduleDate)
            
            print("Status",Status)
            item = json.loads(request.data['ServiceContractsItem'])
            
            Tickets(
                    DeliveryID = request.data['MNo'],
                    AssignTo = request.data['SiteEngineerAssigned'],
                    CreatedBy = request.data['ServiceContractOwner'],
                    Type = type['Type'],
                    SubType = type['SubType'],
                    BpCardCode = request.data['CardCode'],
                    ContactName = request.data['ContractPersoneName'],
                    ContactPhone = request.data['ContractPersoneNumber'],                    
                    CountryCode = request.data['CountryCode'],                    
                    ContractType = request.data['ContractType'],                    
                    ProductSerialNo = request.data['ProductSerialNo'],
                    ProductName = item['ItemDescription'],                    
                    ProductCategory = item['ProjectCode'],                    
                    ContactEmail = "",
                    SysScheduleDate = SysScheduleDate,
                    AppScheduleDate = AppScheduleDate,
                    DueDate = DueDate,
                    Zone = "",
                    Priority = Priority,
                    Status = Status
            ).save()
            ticketObj = Tickets.objects.latest('id')
            print('tktid', ticketObj.id)
            # >>>>>>>>>>>>>> assign checklist >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            if DropDown.objects.filter(id__in=request.data['CheckList']).exists():
                    print('-----check list found----')
                    checklistObj = DropDown.objects.filter(id__in=request.data['CheckList'])
                    print(checklistObj)
                    if len(checklistObj) != 0:
                        for obj in checklistObj:
                            TicketChecklist(
                                    TicketId = ticketObj.id,
                                    Name = obj.DropDownValue,
                                    Description = obj.DropDownDescription,
                                    Data = obj.Data,
                                    Comment = "",
                                    Duration = ""
                            ).save()
                            # print('-----check created found----')
                            tempObj = TicketChecklist.objects.latest('id')
                            print(f'checklistid:- {tempObj.id}')
                    
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    ticketType = type['Type']
                    History(
                            TicketId_id = ticketObj.id,
                            Type = ticketType,
                            Remarks = f'New Ticket {ticketType} created'
                    ).save()
            ticketObj = Tickets.objects.latest('id')
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
            print(ticketObj)
        return ticketObj.id
    except Exception as e:
	    return str(e)


@api_view(['POST'])
def checklist_one(request):
    try:
        id = request.data['id']
        if TicketChecklist.objects.filter(pk = id).exists():
            obj = TicketChecklist.objects.filter(pk = id)
            obj_json =  TicketChecklistSerializer(obj, many=True)
            return Response({"message":"Successfull","status":200 ,"data":obj_json.data})
        else:
            return Response({"message":"Error","status":201 ,"data":['id invalid']})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})


@api_view(['GET'])
def checklist_all(request):
    try:
        checkListObj = TicketChecklist.objects.all().order_by('-id')
        ticketsJson =  TicketChecklistSerializer(checkListObj, many=True)
        return Response({"message":"Successfull","status":200 ,"data":ticketsJson.data})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

@api_view(['POST'])
def checklist_filter(request):
    try:
        TicketId = request.data['TicketId']
        checkListObj = TicketChecklist.objects.filter(TicketId = TicketId)
        ticketsJson = TicketChecklistSerializer(checkListObj, many=True)
        return Response({"message":"Successfull","status":200 ,"data":ticketsJson.data})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})


@api_view(['POST'])
def checklist_update(request):
    try:
        checkListId = request.data['id']
        request.data['Data'] = json.dumps(request.data['Data'])
        if  TicketChecklist.objects.filter(pk = checkListId).exists():
            fetchObj =  TicketChecklist.objects.get(pk = checkListId)
            fetchJson =  TicketChecklistSerializer(fetchObj, data = request.data)
            if fetchJson.is_valid():
                fetchJson.save()
                return Response({"status":"200","message":"successfully","data":[fetchJson.data]})
            return Response(fetchJson.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"Error","status":201 ,"data":['Ticket history invalid']})
    except Exception as e:
        return Response({"message":"Error","status":201 ,"data":str(e)})

@api_view(['POST'])
def filter_bystage(request):
    try:
        StageId = request.data['StageId']
        ticketsObj = Tickets.objects.filter(DeliveryID = StageId).exclude(Stageno = "").order_by('-id').values("id","Title")
        result = TicketsSerializer(ticketsObj, many=True)
        return Response({"message":"Successfull","status":200 ,"data":result.data})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

#<<<<<<<<<< AMC CMC Tickets >>>>>>>>>>>>>
@api_view(['POST'])
def filter_amccmc(request):
    try:
        requestData = request.data

        SalesEmployeeCode = requestData['SalesEmployeeCode']
        PageNo = requestData['PageNo']
        MaxItem = 30
        endWith = (PageNo * MaxItem)
        startWith = (endWith - MaxItem)
        # [startWith:endWith]

        if Employee.objects.filter(SalesEmployeeCode = SalesEmployeeCode).exists():
            #empids = EmpView.GetTeam(EmployeeId,"Operation")            
            #empids = getAllReportingToIdsSubdep(EmployeeId,"Operation")            
            empids = getAllReportingToIds(SalesEmployeeCode)            
            # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

            ticketsObj = Tickets.objects.filter(Q(AssignTo__in = empids), Q(ContractType = "AMC")|Q(ContractType = "CMC")).exclude(Status='Dormant').order_by('-id')[startWith:endWith]
            
            result = showTickets(ticketsObj)
            return Response({"message":"Successfull","status":200 ,"data":result})
        else:
            return Response({"message":"Invalid EmployeeId","status":201 ,"data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]}) 

@api_view(['POST'])
def filter_bytype(request):
    try:
        Type = request.data['Type']
        ticketsObj = Tickets.objects.filter(Type = Type).order_by('-id').values("id","TicketStartDate","TicketEndDate","TicketStatus","AssignTo")
        result = TicketsSerializer(ticketsObj, many=True)
        alltkt = []
        for tkt in result.data:
            print(tkt['AssignTo'])
            if int(tkt['AssignTo']) > 0:
                emp = Employee.objects.filter(SalesEmployeeCode = tkt['AssignTo']).values("SalesEmployeeName")[0]['SalesEmployeeName']
                print(emp)
                tkt = json.loads(json.dumps(tkt))
                tkt['AssignName']=emp
            else:
                tkt['AssignName']="N/A"
            alltkt.append(tkt)
       
        return Response({"message":"Successfull","status":200 ,"data":alltkt})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

@api_view(['POST'])
def filter_bydeliveryid(request):
    try:
        DeliveryID = request.data['DeliveryID']
        ticketsObj = Tickets.objects.filter(DeliveryID = DeliveryID)#.order_by('-id')#.values("id","TicketStartDate","TicketEndDate","TicketStatus","AssignTo")
        result = TicketsSerializer(ticketsObj, many=True)
        alltkt = []
        for tkt in result.data:
            print(tkt['AssignTo'])
            if int(tkt['AssignTo']) > 0:
                emp = Employee.objects.filter(SalesEmployeeCode = tkt['AssignTo']).values("SalesEmployeeName")[0]['SalesEmployeeName']
                print(emp)
                tkt = json.loads(json.dumps(tkt))
                tkt['AssignName']=emp
            else:
                tkt['AssignName']="N/A"
            alltkt.append(tkt)
       
        return Response({"message":"Successfull","status":200 ,"data":alltkt})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})
		
@api_view(['POST'])
def filter_ticket_product(request):
    try:
        if len(request.data) != 0:
            alltkt =[]
            ticketsObj = Tickets.objects.filter(**request.data).order_by('-id').values("id","BpCardCode", "DeliveryID","ProductSerialNo","TicketStartDate","TicketEndDate","TicketStatus","CreateDate","AssignTo")            
            
            for obj in ticketsObj:
                tkt = TicketsSerializer(obj)
                obj_json = json.loads(json.dumps(tkt.data))
                if Employee.objects.filter(SalesEmployeeCode=obj['AssignTo']).exists():
                    EmpName = Employee.objects.get(SalesEmployeeCode=obj['AssignTo']).SalesEmployeeName
                    obj_json['AssignName'] = EmpName
                    alltkt.append(obj_json)
                else:
                    obj_json['AssignName'] = ""
                    alltkt.append(obj_json)

            return Response({"message":"Successfull","status":200 ,"data":alltkt})
        else:        
            return Response({"message":"Please send atleast one key for filter","status":201 ,"data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})


def auto_ticket(project, item, BP, cur_stage, next_stage, tkt_type):
    if int(next_stage.StageAssign) > 0:
        assign = next_stage.StageAssign
    elif int(next_stage.StageOwner) > 0:
        assign = next_stage.StageOwner
    else:
        assign = project.project_owner
    print("assign", assign)
    print("data", next_stage.Data)
        
    Tickets(
            DeliveryID = next_stage.id,
            Stageno = next_stage.Stageno,
            Data = next_stage.Data,
            AssignTo = assign,
            CreatedBy = project.project_owner,
            Type = tkt_type.Type,
            SubType = tkt_type.SubType,
            BpCardCode = BP.CardCode,
            ContactName = BP.ContactPerson,
            ContactPhone = BP.Phone1,
            CountryCode = BP.CountryCode,
            ProductName = item.ItemDescription,
            ProductSerialNo = item.ItemSerialNo,
            ProductCategory = item.ProjectCode,            
            ContactEmail = BP.EmailAddress,
            Zone = BP.Zone,
            Priority = "Medium",
            Status = 'Pending',
        ).save()
    ticketObj = Tickets.objects.latest('id')
    
    # >>>>>>>>>>>>>> assign checklist >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    if DropDown.objects.filter(DropDownName="Checklist", Field1 =  tkt_type.Type, Field2 =  tkt_type.SubType).exists():
        print('-----check list found----')
        checklistObj = DropDown.objects.filter(DropDownName="Checklist", Field1 =  tkt_type.Type, Field2 =  tkt_type.SubType)
        print(checklistObj)
        if len(checklistObj) != 0:
            for obj in checklistObj:
                TicketChecklist(
                    TicketId = ticketObj.id,
                    Name = obj.DropDownValue,
                    Description = obj.DropDownDescription,
                    Data = obj.Data,
                    Comment = "",
                    Duration = ""
                ).save()
                # print('-----check created found----')
                tempObj = TicketChecklist.objects.latest('id')
                print(f'checklistid:- {tempObj.id}')
        
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        ticketType = tkt_type.Type
        History(
            TicketId_id = ticketObj.id,
            Type = ticketType,
            Remarks = f'New Ticket {ticketType} created'
        ).save()
        ticketObj = Tickets.objects.latest('id')
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    print(ticketObj)
    return ticketObj