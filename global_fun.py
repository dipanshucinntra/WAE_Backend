from Employee.models import *
from Notification.models import Notification

import calendar
import requests, json
import time
import math
import mysql.connector
from datetime import datetime, date

currentDate = date.today()
currentDay = calendar.day_name[currentDate.weekday()]  # this will return the day of a week
currentTime = datetime.today().strftime("%I:%M %p")

#@api_view(["POST"])
def tree(SalesEmployeeCode):
        emp_obj =  Employee.objects.filter(SalesEmployeeCode=SalesEmployeeCode)
        print(emp_obj[0].role)
        i=1
        while int(emp_obj[0].reportingTo) !=0:
            emp_obj = Employee.objects.filter(SalesEmployeeCode=emp_obj[0].reportingTo)
            if emp_obj[0].role == 'admin':
                i=i+0
            else:
                i=i+1
        print(str(i))
        return str(i)
    #return Response({"message":"Success", "status":200, "data":[{"Level":str(i)}]})


def tree_role(employee_obj):
    if employee_obj.role == 'admin' or employee_obj.role == 'ceo':
        lev = 1
    elif employee_obj.role == 'manager':
        lev = 2
    else:
        lev = 3
    return str(lev)

######################### COPIED BY DIPANSHU FROM STANDALONE SUPPORT ###################################
# function to get all reporting reporting person
def getAllReportingToPks(code):
    obj =  Employee.objects.get(SalesEmployeeCode=code)
    data = []
    def recrusiveMethod(code, id):
        # print('recursive call')
        # print(id)
        data.append(str(id))
        emp_obj =  Employee.objects.filter(reportingTo=code)
        for obj in emp_obj:
            recrusiveMethod(obj.SalesEmployeeCode, obj.id)
    recrusiveMethod(obj.SalesEmployeeCode, obj.id)
    return data


# function to get all reporting reporting person
def getAllReportingToIds(EmpCode):
    data = []
    def recrusiveMethod(id):
        # print('recursive call')
        # print(id)
        data.append(str(id))
        emp_obj =  Employee.objects.filter(reportingTo=id)
        for obj in emp_obj:
            recrusiveMethod(obj.SalesEmployeeCode)
    recrusiveMethod(EmpCode)
    return data

# function to get all reporting reporting person
def getAllReportingToIdsSubdep(EmpCode, Team):
    data = []
    subdepids = []
    subdepids.append(GetSubdep("Management"))
    subdepids.append(GetSubdep(Team))
    print("subdepid", subdepids)
    def recrusiveMethod(id):
        # print('recursive call')
        #print(id)
        data.append(str(id))
        emp_obj =  Employee.objects.filter(reportingTo=id, subdep__in=subdepids)
        # emp_obj =  Employee.objects.filter(reportingTo=id)
        for obj in emp_obj:
            #print(obj.role.Name)
            recrusiveMethod(obj.SalesEmployeeCode)
    recrusiveMethod(EmpCode)
    return data

def GetSubdep(Team):
    print("Team : ", Team)
    if Subdepartment.objects.filter(Name=Team).exists():
        subdep = Subdepartment.objects.get(Name=Team)
        print("subdep: ", subdep)
        return subdep.id
    else:
        return 0
    
def getAllReportingToIds(EmpCode):
    data = []
    def recrusiveMethod(id):
        # print('recursive call')
        # print(id)
        data.append(str(id))
        emp_obj =  Employee.objects.filter(reportingTo=id)
        for obj in emp_obj:
            recrusiveMethod(obj.SalesEmployeeCode)
    recrusiveMethod(EmpCode)
    return data

# create in app custome notification
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def CreateInAppNotification(Title = "", Description = "", Type = "", SourceType = "", SourceID = "", Emp = ""):
    try:
        Title = Title
        Description = Description
        Type = Type
        SourceType = SourceType
        SourceID = SourceID
        Emp = Emp
        Read = 0
        Push = 0
        SourceTime = currentTime
        CreatedDate = currentDate
        CreatedTime = currentTime
        Notification(Title = Title, Description = Description, Type = Type, SourceType = SourceType, SourceID = SourceID, Emp = Emp, Read = Read, Push = Push, SourceTime = SourceTime, CreatedDate = CreatedDate, CreatedTime = CreatedTime).save()
        obj = Notification.objects.latest('id')
        notiId = obj.id
        return f"Success! Notification id {notiId}"
    except Exception as e:
        # print(str(e))
        return str(e)