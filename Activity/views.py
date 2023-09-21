from django.shortcuts import render, redirect  
from django.http import JsonResponse, HttpResponse

from Notification.models import Notification
from global_fun import getAllReportingToPks
from .forms import ActivityForm  
from .models import *
from Employee.models import Employee
from BusinessPartner.models import BPBranch

from django.contrib import messages

from rest_framework.decorators import api_view    
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import JSONParser
from pytz import timezone
from datetime import datetime as dt

######################BY DIPANSHU#################
from geopy.distance import geodesic

date = dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d')
yearmonth = dt.now(timezone("Asia/Kolkata")).strftime('%Y-%m')
time = dt.now(timezone("Asia/Kolkata")).strftime('%H:%M %p')
# Create your views here.  

@api_view(['POST'])
def followup(request):
    try:
        SourceID = request.data['SourceID']
        Comment = request.data['Comment']
        Subject = request.data['Subject']
        Emp = request.data['Emp']
        From = request.data['From']
        To = request.data['From']
        Time = request.data['Time']
        Type = request.data['Type']
        leadType = request.data['leadType']        
        SourceType = request.data['SourceType']
        CreateDate = request.data['CreateDate']
        CreateTime = request.data['CreateTime']
        
        model = Activity(SourceID=SourceID, Subject=Subject, Comment=Comment, Emp=Emp, From=From, To=To, Time=Time, Type=Type, SourceType=SourceType, CreateDate=CreateDate, CreateTime=CreateTime, leadType=leadType)        
        
        model.full_clean()
        
        model.save()
        act = Activity.objects.latest('id')
        print(act.id)
        
        SourceID = request.data['SourceID']
        Message = request.data['Comment']
        Emp = request.data['Emp']
        Emp_Name = request.data['Emp_Name']
        Mode = request.data['Mode']
        SourceType = request.data['SourceType']
        UpdateDate = request.data['CreateDate']
        UpdateTime = request.data['CreateTime']

        chat = Chatter(Message=Message, SourceID=SourceID, SourceType=SourceType, Emp=Emp, Emp_Name=Emp_Name, Mode=Mode, UpdateDate=UpdateDate, UpdateTime=UpdateTime)
        
        chat.save()

        return Response({"message":"Success","status":200,"data":[]})
    except Exception as e:
        return Response({"message":"Can not create","status":201,"data":[{"Error":str(e)}]})


#Opp Activity Create API
@api_view(['POST'])
def create(request):
    try:
        SourceID = request.data['SourceID']
        Subject = request.data['Subject']
        Comment = request.data['Comment']
        Name = request.data['Name']
        RelatedTo = request.data['RelatedTo']
        Emp = request.data['Emp']
        Title = request.data['Title']
        Description = request.data['Description']
        From = request.data['From']
        To = request.data['To']
        Time = request.data['Time']
        Allday = request.data['Allday']
        Location = request.data['Location']
        Host = request.data['Host']
        Participants = request.data['Participants']
        Document = request.data['Document']
        Repeated = request.data['Repeated']
        Priority = request.data['Priority']
        ProgressStatus = request.data['ProgressStatus']
        Type = request.data['Type']
        leadType = request.data['leadType']
        SourceType = request.data['SourceType']
        CreateDate = request.data['CreateDate']
        CreateTime = request.data['CreateTime']
        
        model = Activity(SourceID=SourceID, Subject=Subject, Comment=Comment, Name=Name, RelatedTo=RelatedTo, Emp=Emp, Title=Title, Description=Description, From=From, To=To, Time=Time, Allday=Allday, Location=Location, Host=Host, Participants=Participants, Document=Document, Repeated=Repeated, Priority=Priority, ProgressStatus=ProgressStatus, Type=Type, SourceType=SourceType, CreateDate=CreateDate, CreateTime=CreateTime, leadType=leadType)
        
        model.save()
        act = Activity.objects.latest('id')
        print(act.id)
        return Response({"message":"Success","status":"200","data":[]})
    except Exception as e:
        return Response({"message":"Can not create","status":"201","data":[{"Error":str(e)}]})


#Opp Map Create API
@api_view(['POST'])
def maps(request):
    try:
        Lat = request.data['Lat']
        Long = request.data['Long']
        Address = request.data['Address']
        Emp_Id = request.data['Emp_Id']
        Emp_Name = request.data['Emp_Name']
        UpdateDate = request.data['UpdateDate']
        UpdateTime = request.data['UpdateTime']
        
        model = Maps(Lat=Lat, Long=Long, Address=Address, Emp_Id=Emp_Id, Emp_Name=Emp_Name, UpdateDate=UpdateDate, UpdateTime=UpdateTime)
        
        model.save()
        mp = Maps.objects.latest('id')
        print(mp.id)
        return Response({"message":"Success","status":200,"data":[{"id":mp.id}]})
    except:
        return Response({"message":"Can not create","status":201,"data":[]})

#Opp Map Create API
@api_view(['POST'])
def chatter(request):
    try:
        Message = request.data['Message']
        SourceID = request.data['SourceID']
        SourceType = request.data['SourceType']
        Emp = request.data['Emp']
        Emp_Name = request.data['Emp_Name']
        Mode = request.data['Mode']
        UpdateDate = request.data['UpdateDate']
        UpdateTime = request.data['UpdateTime']

        model = Chatter(Message=Message, SourceID=SourceID, SourceType=SourceType, Emp=Emp, Emp_Name=Emp_Name, UpdateDate=UpdateDate, UpdateTime=UpdateTime,Mode=Mode)
        
        model.save()
        chat = Chatter.objects.latest('id')
        print(chat.id)
        return Response({"message":"Success","status":200,"data":[{"id":chat.id}]})
    except Exception as e:
        return Response({"message":"Can not create","status":201,"data":[str(e)]})


#Activity All API
@api_view(["POST"])
def all(request):
    Emp=request.data['Emp']
    act_obj = Activity.objects.filter(Emp=Emp).order_by("-id")
    act_json = ActivitySerializer(act_obj, many=True)
    return Response({"message": "Success","status": 200,"data":act_json.data})

#Activity All Filter API
@api_view(["POST"])
def all_filter(request):
    Emp=request.data['Emp']
    date=request.data['date']
    #"SELECT * FROM `Activity_activity` WHERE `From` <= '"+date+"' and `To` >= '"+date+"'"
    act_obj = Activity.objects.filter(Emp=Emp, From__lte=date, To__gte=date).order_by("-id")
    act_json = ActivitySerializer(act_obj, many=True)
    return Response({"message": "Success","status": 200,"data":act_json.data})

#Activity All Filter by Date API
@api_view(["POST"])
def all_filter_by_date(request):
    try:
        Emp=request.data['Emp']
        date=request.data['date']
        act_obj = Activity.objects.filter(Emp=Emp, To = date).order_by("-id")
        act_json = ActivitySerializer(act_obj, many=True)
        return Response({"message": "Success","status": 200,"data":act_json.data})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":""})

#Chatter All API
@api_view(["POST"])
def chatter_all(request):
    Emp=request.data['Emp']
    SourceID=request.data['SourceID']
    SourceType=request.data['SourceType']
    chat_obj = Chatter.objects.filter(Emp=Emp, SourceType=SourceType, SourceID=SourceID).order_by("id")
    chat_json = ChatterSerializer(chat_obj, many=True)
    return Response({"message": "Success","status": 200,"data":chat_json.data})


#Activity Delete API
@api_view(['POST'])
def delete(request):
    fetchid=request.data['id']
    try:
        Activity.objects.get(pk=fetchid).delete()
        return Response({"message":"successful","status":200,"data":[]})
    except Exception as e:
         return Response({"message":"Id wrong","status":201,"data":[str(e)]})


#Activity One API
@api_view(["POST"])
def one(request):
    id=request.data['id']    
    act_obj = Activity.objects.get(id=id)
    act_json = ActivitySerializer(act_obj)
    return Response({"message": "Success","status": 200,"data":[act_json.data]})

#maps One API
@api_view(["POST"])
def map_one(request):
    Emp_Id=request.data['Emp_Id']    
    map_obj = Maps.objects.filter(Emp_Id=Emp_Id)
    map_json = MapsSerializer(map_obj, many=True)
    return Response({"message": "Success","status": 200,"data":[map_json.data]})

#Map Filter API
@api_view(["POST"])
def map_filter(request):
    Emp=request.data['Emp_Id']
    date=request.data['UpdateDate']
    act_obj = Maps.objects.filter(Emp_Id=Emp, UpdateDate=date).order_by("-id")
    act_json = MapsSerializer(act_obj, many=True)
    return Response({"message": "Success","status": 200,"data":act_json.data})


#Map all
@api_view(["POST"])
def map_all(request):

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
            mps = []
            print(SalesEmployeeCode)
            for scode in SalesEmployeeCode:
                emp = Employee.objects.get(SalesEmployeeCode=scode)
                mp_obj = Maps.objects.filter(Emp_Id=emp.id).order_by("-id")[:1]
                if len(mp_obj) !=0:
                    mp_json = MapsSerializer(mp_obj, many=True)
                    print(mp_json.data[0])
                    mps.append(mp_json.data[0])
            return Response({"message": "Success","status": 200,"data":mps})
            
            #return Response({"message": "Success","status": 201,"data":[{"emp":SalesEmployeeCode}]})
        else:
            return Response({"message": "Unsuccess","status": 201,"data":[{"error":"SalesEmployeeCode?"}]})
    else:
        return Response({"message": "Unsuccess","status": 201,"data":[{"error":"SalesEmployeeCode?"}]})

#Activity Status Update API
@api_view(['POST'])
def status(request):
    fetchid = request.data['id']
    try:
        model = Activity.objects.get(pk = fetchid)        
        if int(model.Status) == 0:
            model.Status = 1
            model.save()
            print("if")
        else:
            model.Status = 0
            model.save()
            print("else")
        return Response({"message":"successful","status":200,"data":[]})
    except Exception as e:
        return Response({"message":"unsuccess","status":201,"data":[{"Error":str(e)}]})


#Activity Update API
@api_view(['POST'])
def update(request):
    fetchid = request.data['id']
    try:
        model = Activity.objects.get(pk = fetchid)
        
        #model.SourceID = request.data['SourceID']
        #model.SourceType = request.data['SourceType']
        #model.Type = request.data['Type']
        model.Subject = request.data['Subject']
        model.Comment = request.data['Comment']
        model.Name = request.data['Name']
        model.RelatedTo = request.data['RelatedTo']
        model.Emp = request.data['Emp']
        model.Title = request.data['Title']
        model.Description = request.data['Description']
        model.From = request.data['From']
        model.To = request.data['To']
        model.Time = request.data['Time']
        model.Allday = request.data['Allday']
        model.Location = request.data['Location']
        model.Host = request.data['Host']
        model.Participants = request.data['Participants']
        model.Document = request.data['Document']
        model.Priority = request.data['Priority']
        model.ProgressStatus = request.data['ProgressStatus']
        model.Repeated = request.data['Repeated']


        model.save()
        context = {
            #'SourceID':request.data['SourceID'],
            #'SourceType':request.data['SourceType'],
            #'Type':request.data['Type'],
            'Subject':request.data['Subject'],
            'Comment':request.data['Comment'],
            'Name':request.data['Name'],
            'RelatedTo':request.data['RelatedTo'],
            'Emp':request.data['Emp'],
            'Title':request.data['Title'],
            'Description':request.data['Description'],
            'From':request.data['From'],
            'To':request.data['To'],
            'Time':request.data['Time'],
            'Allday':request.data['Allday'],
            'Location':request.data['Location'],
            'Host':request.data['Host'],
            'Participants':request.data['Participants'],
            'Document':request.data['Document'],
            'Priority':request.data['Priority'],
            'ProgressStatus':request.data['ProgressStatus'],
            'Repeated':request.data['Repeated']
            }

        return Response({"message":"successful","status":"200","data":[context]})
    except:
        return Response({"message":"ID Wrong","status":"201","data":[]})

######################### COPIED BY DIPANSHU FROM STANDALONE SUPPORT ###################################

#Map all filter for team
@api_view(["POST"])
def map_all_team(request):

    json_data = request.data
    
    
    if "SalesEmployeeCode" in json_data:
        print("yes")
        
        if json_data['SalesEmployeeCode']!="":
            SalesEmployeeCode = json_data['SalesEmployeeCode']
            
            SalesEmployeeCode = getAllReportingToPks(SalesEmployeeCode)
            
            branch = BPBranch.objects.get(pk=json_data['bpbranch'])
            bp_lat = branch.Lat
            bp_long = branch.Long
            print("bp",bp_lat)
            
            mps = []
            print(SalesEmployeeCode)
            for scode in SalesEmployeeCode:
                EmpCode = Employee.objects.get(pk=scode).SalesEmployeeCode
                print("scode", scode)
                mp_obj = Maps.objects.filter(Emp_Id=scode).order_by("-id")[:1]
                if len(mp_obj) !=0:
                    origin = (bp_lat, bp_long)  # (latitude, longitude) don't confuse
                    dist = (mp_obj[0].Lat, mp_obj[0].Long)
                    dis = geodesic(origin, dist).meters
                    mp_json = MapsSerializer(mp_obj, many=True)
                    mp_json.data[0]["dis"]=dis
                    mp_json.data[0]["SalesEmployeeCode"]=EmpCode

                    mps.append(mp_json.data[0])
                #{"SalesEmployeeCode":116, "bpbranch":30}
                """
                else:                    
                    mp_json = MapsSerializer(mp_obj, many=True)
                    mp_json.data[0]["dis"]=0

                    mps.append(mp_json.data[0])
                """
            mps_st = sorted(mps, key=lambda i: i['dis'])
            return Response({"message": "Success","status": 200,"data":mps_st})
            
            #return Response({"message": "Success","status": 201,"data":[{"emp":SalesEmployeeCode}]})
        else:
            return Response({"message": "Unsuccess","status": 201,"data":[{"error":"SalesEmployeeCode?"}]})
    else:
        return Response({"message": "Unsuccess","status": 201,"data":[{"error":"SalesEmployeeCode?"}]})

#Map all employe with latest lat long
@api_view(["GET"])
def map_emps_last_location(request):
    try:
        empIdsObj = Employee.objects.all().values_list("SalesEmployeeCode", flat=True)
        empIdArr = list(empIdsObj)
        print(empIdArr)
        allMaps = []
        for empId in empIdArr:
            if Maps.objects.filter(Emp_Id = empId).exists():
                act_obj = Maps.objects.filter(Emp_Id = empId).order_by('-id')[0]
                act_json = MapsSerializer(act_obj)
                allMaps.append(act_json.data)

        return Response({"message": "Success","status": 200,"data":allMaps})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})    