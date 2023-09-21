from django.shortcuts import render, redirect  
#from django.http import JsonResponse, HttpResponse
from .forms import BPUser  
from .models import BPUser, BusinessPartner  
from Order.models import Order  
from Invoice.models import Invoice, IncomingPayments  
from Project.models import MasterProject  
from Tickets.models import Tickets  
import requests, json

from rest_framework.decorators import api_view    
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import BPUserSerializer
#from rest_framework.parsers import JSONParser
from django.conf import settings
# Create your views here.  

#BPUser Create API
@api_view(['POST'])
def create(request):
    try:
        BPID = request.data['BPID']
        CardCode = request.data['CardCode']
        EmployeeCode = request.data['EmployeeCode']
        EmployeeName = request.data['EmployeeName']
        EmployeeID = request.data['EmployeeID']
        Username = request.data['Username']
        Password = request.data['Password']
        FirstName = request.data['FirstName']
        MiddleName = request.data['MiddleName']
        LastName = request.data['LastName']
        Email = request.data['Email']
        Mobile = request.data['Mobile']
        CountryCode = request.data['CountryCode']
        Role = request.data['Role']
        Position = request.data['Position']
        Branch = request.data['Branch']
        Active = request.data['Active']
        PasswordUpdatedOn = request.data['PasswordUpdatedOn']
        LastLoginOn = request.data['LastLoginOn']
        LogedIn = request.data['LogedIn']
        FCM = request.data['FCM']
        CreateDate = request.data['CreateDate']
        CreateTime = request.data['CreateTime']
        UpdateDate = request.data['UpdateDate']
        UpdateTime = request.data['UpdateTime']
        
        if BPUser.objects.filter(Username=Username).exists():
            return Response({"message":"Already exists this Username","status":201,"data":[]})
        else:
            model = BPUser(BPID = BPID, CardCode=CardCode, EmployeeCode = EmployeeCode, EmployeeName = EmployeeName, EmployeeID = EmployeeID, Username = Username, Password = Password, FirstName = FirstName, MiddleName = MiddleName, LastName = LastName, Email = Email, Mobile = Mobile, CountryCode = CountryCode, Role = Role, Position = Position, Branch = Branch, Active = Active, PasswordUpdatedOn = PasswordUpdatedOn, LastLoginOn = LastLoginOn, LogedIn = LogedIn, FCM = FCM, CreateDate = CreateDate, CreateTime = CreateTime, UpdateDate = UpdateDate, UpdateTime = UpdateTime)

            model.save()    
            Obj = BPUser.objects.latest('id')
            return Response({"message":"successful","status":200, "data":[{"id":Obj.id}]})
    except Exception as e:
        return Response({"message":str(e),"status":201, "data":[]})

#BPUser All API
@api_view(["GET"])
def all(request):    
    bpemployee_obj = BPUser.objects.all() 
    bpemployee_json = BPUserSerializer(bpemployee_obj, many=True)
    return Response({"message": "Success","status": 200,"data":bpemployee_json.data})


#BPUser One API
@api_view(["POST"])
def one(request):
    id=request.data['id']
    bpemployee_obj = BPUser.objects.get(id=id)
    bpemployee_json = BPUserSerializer(bpemployee_obj)
    return Response({"message": "Success","status": 200,"data":[bpemployee_json.data]})

#BPUser Update API
@api_view(['POST'])
def update(request):
    fetchid = request.data['id']
    try:
        model = BPUser.objects.get(pk = fetchid)
        
        model.BPID = request.data['BPID']
        model.EmployeeCode = request.data['EmployeeCode']
        model.EmployeeName = request.data['EmployeeName']
        model.EmployeeID = request.data['EmployeeID']
        model.Username = request.data['Username']
        model.Password = request.data['Password']
        model.FirstName = request.data['FirstName']
        model.MiddleName = request.data['MiddleName']
        model.LastName = request.data['LastName']
        model.Email = request.data['Email']
        model.Mobile = request.data['Mobile']
        model.CountryCode = request.data['CountryCode']
        model.Role = request.data['Role']
        model.Position = request.data['Position']
        model.Branch = request.data['Branch']
        model.Active = request.data['Active']
        model.PasswordUpdatedOn = request.data['PasswordUpdatedOn']
        model.LastLoginOn = request.data['LastLoginOn']
        model.LogedIn = request.data['LogedIn']
        model.FCM = request.data['FCM']
        model.UpdateDate = request.data['UpdateDate']
        model.UpdateTime = request.data['UpdateTime']
        model.save()

        return Response({"message":"successful","status":"200", "data":[]})
    except:
            return Response({"message":"Id wrong","status":"201","data":[]})

#BPUser delete
@api_view(['POST'])
def delete(request):
    fetchid=request.data['id']
    try:
        fetchdata=BPUser.objects.filter(pk=fetchid).delete()
        return Response({"message":"successful","status":"200","data":[]})
    except:
         return Response({"message":"Id wrong","status":"201","data":[]})

#Employee Login API
@api_view(["POST"])
def login(request):
    try:
        Username=request.data['Username']
        Password=request.data['Password']
        FCM = request.data['FCM']

        if BPUser.objects.filter(Username=Username, Password=Password).exists():
            print("uname")
            employee_obj = BPUser.objects.get(Username=Username, Password=Password)
        elif BPUser.objects.filter(Email=Username, Password=Password).exists():
            print("email")
            employee_obj = BPUser.objects.get(Email=Username, Password=Password)
        else:
            print("incorrect")
            return Response({"message": "Username or password is incorrect","status": 201,"data":[]})
        
        if employee_obj.Active == "tYES":
            if FCM !="":
                employee_obj.FCM = FCM
                employee_obj.save()
            employee_json = BPUserSerializer(employee_obj)
            
            return Response({"message": "Success","status": 200,"data":[employee_json.data]})
        else:
            return Response({"message": "User is InActive", "status": 201,"data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":"201","data":[{"Error":str(e)}]})

@api_view(["POST"])
def dashboard(request):
    json_data = request.data
    try:
        CardCode = json_data['CardCode']
        if BusinessPartner.objects.filter(CardCode = CardCode).exists():

            
            ord_all = Order.objects.filter(CardCode=CardCode).count()
            print(ord_all)
            
            inv_all = Invoice.objects.filter(CardCode=CardCode).count()
            ##print(inv_all)
            
            sale = 0
            orderAmtList = list(Invoice.objects.filter(CardCode=CardCode).values_list('DocTotal', flat=True))
            for amt in orderAmtList:
                sale = sale+float(amt)
            print(sale)
            
            pmt = 0
            pmtAmtList = list(IncomingPayments.objects.filter(CardCode=CardCode).values_list('TransferSum', flat=True))
            for amt in pmtAmtList:
                pmt = pmt+float(amt)
            print(pmt)
            Balance = sale - pmt

            """
            ord_over = Order.objects.filter(SalesPersonCode__in=empList, DocumentStatus="bost_Open", DocDueDate__lt=tdate).count()
            #print(ord_over)
            #print(date)
            
            ord_open = Order.objects.filter(SalesPersonCode__in=empList, DocumentStatus="bost_Open", DocDueDate__gte=tdate).count()
            #print(ord_open)

            ord_close = Order.objects.filter(SalesPersonCode__in=empList, DocumentStatus="bost_Close").count()
            #print(ord_close)

            
            tnd_all = Tender.objects.filter(SalesPersonCode__in=empList).count()
            #print(tnd_all)
            
            """
            pro_all = MasterProject.objects.filter(CardCode=CardCode).count()
            tkt_all = Tickets.objects.filter(BpCardCode=CardCode).count()
            
    
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            context = {
                "Sale":sale, 
                "Order":ord_all, 
                "Invoice":inv_all, 
                "Balance":Balance, 
                "Project":pro_all,
                "Ticket":tkt_all
            }
            return Response({"message": "Success","status": 200,"data":[context]})
        else:
            return Response({"message": "Unsuccess","status": 201,"data":[{"error":"CardCode?"}]})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})
