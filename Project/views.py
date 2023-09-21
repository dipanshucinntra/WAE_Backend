from django.shortcuts import render, redirect  
from django.http import JsonResponse, HttpResponse
from BusinessPartner.models import BusinessPartner

from Employee.models import Employee
from Tickets.models import SubType, Tickets
from global_fun import CreateInAppNotification, getAllReportingToIds, getAllReportingToIdsSubdep
from .forms import ProjectForm  
from .models import MasterProject, Project, ProjectItem, ProjectStage, ProjectStaticstage  
import json
from django.contrib import messages
import os
from django.core.files.storage import FileSystemStorage
from Tickets import views as Tick
from rest_framework.decorators import api_view    
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import MasterProjectSerializer, ProjectItemSerializer, ProjectSerializer, ProjectStageSerializer, ProjectStaticstageSerializer
from rest_framework.parsers import JSONParser
from Attachment.models import Attachment
from Attachment.serializers import AttachmentSerializer
from django.db.models import Q
from Employee import views as EmpView

# Create your views here.  

#Project Create API
@api_view(['POST'])
def create(request):
    try:
        name = request.data['name']
        
        kit_consultant_code = request.data['kit_consultant_code']
        kit_consultant_name = request.data['kit_consultant_name']
        kit_contact_person = request.data['kit_contact_person']
        
        mep_consultant_code = request.data['mep_consultant_code']
        mep_consultant_name = request.data['mep_consultant_name']
        mep_contact_person = request.data['mep_contact_person']
        
        pm_consultant_code = request.data['pm_consultant_code']
        pm_consultant_name = request.data['pm_consultant_name']
        pm_contact_person = request.data['pm_contact_person']
        
        customer_group_type = request.data['customer_group_type']
        contact_person = request.data['contact_person']
        start_date = request.data['start_date']
        target_date = request.data['target_date']
        completion_date = request.data['completion_date']
        details = request.data['details']        
        #cardcode = request.data['cardcode']
        CardCode = request.data['CardCode']        
        sector = request.data['sector']
        type = request.data['type']
        location = request.data['location']
        project_owner = request.data['project_owner']
        project_cost = request.data['project_cost']
        project_status = request.data['project_status']
        address = request.data['address']
        
        Attach = request.data['Attach']
        Caption = request.data['Caption']
        CreateDate = request.data['CreateDate']
        CreateTime = request.data['CreateTime']
        
        GroupType = request.data['GroupType'] #added by millan on 10 October 2022
        
        #added by millan on 11-10-2022
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
        #added by millan on 11-10-2022

        model=Project(name = name, kit_consultant_code = kit_consultant_code, kit_consultant_name = kit_consultant_name, kit_contact_person=kit_contact_person, mep_consultant_code = mep_consultant_code, mep_consultant_name = mep_consultant_name, mep_contact_person=mep_contact_person, pm_consultant_code = pm_consultant_code, pm_consultant_name = pm_consultant_name, pm_contact_person=pm_contact_person, customer_group_type = customer_group_type, contact_person = contact_person, start_date = start_date, target_date = target_date, completion_date = completion_date, details = details, CardCode = CardCode, sector = sector, type = type, location = location, project_owner = project_owner, project_cost = project_cost, project_status = project_status, address = address, CreatedDate = CreateDate, CreatedTime=CreateTime, GroupType = GroupType, cli_consultant_code = cli_consultant_code, cli_consultant_name = cli_consultant_name, cli_contact_person = cli_contact_person, contr_consultant_code = contr_consultant_code, contr_consultant_name = contr_consultant_name, contr_contact_person = contr_contact_person, fcm_consultant_code = fcm_consultant_code, fcm_consultant_name = fcm_consultant_name, fcm_contact_person = fcm_contact_person, arch_consultant_code = arch_consultant_code, arch_consultant_name = arch_consultant_name, arch_contact_person = arch_contact_person, oth_consultant_code = oth_consultant_code, oth_consultant_name = oth_consultant_name, oth_contact_person=oth_contact_person)
        
        model.save()
        qt = Project.objects.latest('id')
        fetchid = qt.id
        
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

            att=Attachment(File=attachmentsImage_url, Caption=Caption, LinkType="Project", LinkID=fetchid, CreateDate=CreateDate, CreateTime=CreateTime, UpdateDate=CreateDate, UpdateTime=CreateTime)
            
            att.save()
        return Response({"message":"successful","status":"200","data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":"201","data":[]})

#Project All API
@api_view(["POST"])
def all(request):
    try:
        allProject = []
        #cardcode=request.data['cardcode']
        CardCode=request.data['CardCode']
        #Projects_objs = Project.objects.filter(Q(CardCode=CardCode) | Q(kit_consultant_code=cardcode) | Q(mep_consultant_code=cardcode) | Q(pm_consultant_code=cardcode) | Q(cli_consultant_code=cardcode) | Q(contr_consultant_code=cardcode) | Q(fcm_consultant_code=cardcode) | Q(arch_consultant_code=cardcode) | Q(oth_consultant_code=cardcode)).order_by("-id")
        Projects_objs = Project.objects.filter(Q(CardCode=CardCode) | Q(kit_consultant_code=CardCode) | Q(mep_consultant_code=CardCode) | Q(pm_consultant_code=CardCode) | Q(cli_consultant_code=CardCode) | Q(contr_consultant_code=CardCode) | Q(fcm_consultant_code=CardCode) | Q(arch_consultant_code=CardCode) | Q(oth_consultant_code=CardCode)).order_by("-id")
        for Obj in Projects_objs:            
            ObjJson = ProjectSerializer(Obj, many=False)
            ObjJson = json.loads(json.dumps(ObjJson.data))
            #print(ObjJson)

            Attach = Attachment.objects.filter(LinkType="Project", LinkID=Obj.id)
            AttachJson = AttachmentSerializer(Attach, many=True)
            
            ObjJson['Attach'] = AttachJson.data
            print(ObjJson)
            allProject.append(ObjJson)
        return Response({"message": "Success","status": 200,"data":allProject})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})

#Project All API
@api_view(["POST"])
def allbycp(request):
    try:
        allProject = []
        contact_person=request.data['contact_person']
        Projects_objs = Project.objects.filter(Q(contact_person=contact_person) | Q(kit_contact_person=contact_person) | Q(mep_contact_person=contact_person) | Q(pm_contact_person=contact_person) | Q(cli_contact_person=contact_person) | Q(contr_contact_person=contact_person) | Q(fcm_contact_person=contact_person) | Q(arch_contact_person=contact_person) | Q(oth_contact_person=contact_person)).order_by("-id")
        for Obj in Projects_objs:            
            ObjJson = ProjectSerializer(Obj, many=False)
            ObjJson = json.loads(json.dumps(ObjJson.data))
            #print(ObjJson)

            Attach = Attachment.objects.filter(LinkType="Project", LinkID=Obj.id)
            AttachJson = AttachmentSerializer(Attach, many=True)
            
            ObjJson['Attach'] = AttachJson.data
            print(ObjJson)
            allProject.append(ObjJson)
        return Response({"message": "Success","status": 200,"data":allProject})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})
        
#Project One API
@api_view(["POST"])
def one(request):
    try:
        id=request.data['id']
        Project_obj = Project.objects.get(id=id)
        Project_json = ProjectSerializer(Project_obj)
        return Response({"message": "Success","status": 200,"data":[Project_json.data]})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})


#Project Update API
@api_view(['POST'])
def update(request):
    try:
        fetchid = request.data['id']
        model = Project.objects.get(pk = fetchid)

        model.kit_consultant_code = request.data['kit_consultant_code']
        model.kit_consultant_name = request.data['kit_consultant_name']
        model.kit_contact_person = request.data['kit_contact_person']

        model.mep_consultant_code = request.data['mep_consultant_code']
        model.mep_consultant_name = request.data['mep_consultant_name']
        model.mep_contact_person = request.data['mep_contact_person']

        model.pm_consultant_code = request.data['pm_consultant_code']
        model.pm_consultant_name = request.data['pm_consultant_name']
        model.pm_contact_person = request.data['pm_contact_person']

        model.customer_group_type = request.data['customer_group_type']
        model.contact_person = request.data['contact_person']
        model.start_date = request.data['start_date']
        model.target_date = request.data['target_date']
        model.completion_date = request.data['completion_date']
        model.details = request.data['details']
        #model.cardcode = request.data['cardcode']
        model.CardCode = request.data['CardCode']
        model.sector = request.data['sector']
        model.type = request.data['type']
        model.location = request.data['location']
        model.project_owner = request.data['project_owner']
        model.project_cost = request.data['project_cost']
        model.project_status = request.data['project_status']
        model.address = request.data['address']

        model.GroupType = request.data['GroupType'] #added by millan on 10 October 2022
        
        #added by millan on 11-10-2022
        model.cli_consultant_code = request.data['cli_consultant_code']
        model.cli_consultant_name = request.data['cli_consultant_name']
        model.cli_contact_person = request.data['cli_contact_person']
        
        model.contr_consultant_code = request.data['contr_consultant_code']
        model.contr_consultant_name = request.data['contr_consultant_name']
        model.contr_contact_person = request.data['contr_contact_person']
        
        model.fcm_consultant_code = request.data['fcm_consultant_code']
        model.fcm_consultant_name = request.data['fcm_consultant_name']
        model.fcm_contact_person = request.data['fcm_contact_person']
        
        model.arch_consultant_code = request.data['arch_consultant_code']
        model.arch_consultant_name = request.data['arch_consultant_name']
        model.arch_contact_person = request.data['arch_contact_person']
        
        model.oth_consultant_code = request.data['oth_consultant_code']
        model.oth_consultant_name = request.data['oth_consultant_name']
        model.oth_contact_person =  request.data['oth_contact_person']
        #added by millan on 11-10-2022
        
        model.save()
        return Response({"message":"successful","status":"200","data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":"201","data":[]})

#Project delete
@api_view(['POST'])
def delete(request):
    try:
        fetchid=request.data['id']
        fetchdata=Project.objects.filter(pk=fetchid).delete()
        return Response({"message":"successful","status":"200","data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":"201","data":[]})

#Project Listing Without Condition Added by millan on 01-November-2022
@api_view(["GET"])
def project_all(request):
    try:
        allProject = []
        Projects_objs = Project.objects.all().order_by("-id")
        for Obj in Projects_objs:            
            ObjJson = ProjectSerializer(Obj, many=False)
            ObjJson = json.loads(json.dumps(ObjJson.data))

            Attach = Attachment.objects.filter(LinkType="Project", LinkID=Obj.id)
            AttachJson = AttachmentSerializer(Attach, many=True)
            
            ObjJson['Attach'] = AttachJson.data
            allProject.append(ObjJson)
        return Response({"message": "Success","status": 200,"data":allProject})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})

############## CODE ADDED BY DIPANSHU FROM STANDALONE SUPPORT ################

#Project Create API
@api_view(['POST'])
def master_create(request):
    try:
        
        name = request.data['name']
        contact_person = request.data['contact_person']
        start_date = request.data['start_date']
        target_date = request.data['target_date']
        details = request.data['details']        
        CardCode = request.data['CardCode']        
        location = request.data['location']
        project_owner = request.data['project_owner']
        project_cost = request.data['project_cost']
        project_status = request.data['project_status']
        address = request.data['address']        
        Attach = request.data['Attach']
        Caption = request.data['Caption']
        CreatedDate = request.data['CreatedDate']
        CreatedTime = request.data['CreatedTime']
        
        order_id = request.data['order_id']
        
        CreateDate = CreatedDate
        CreateTime = CreatedTime
        UpdateDate = CreatedDate
        UpdateTime = CreatedTime
        
        DepName = request.data['DepName']
        CreatedBy = request.data['CreatedBy']

        model=MasterProject(name = name, contact_person = contact_person, start_date = start_date, target_date = target_date, details = details, CardCode = CardCode, location = location, project_owner = project_owner, project_cost = project_cost, project_status = project_status, address = address, CreatedDate = CreateDate, CreatedTime=CreateTime, order_id=order_id,DepName=DepName,UpdateDate=UpdateDate,UpdateTime=UpdateTime,CreatedBy=CreatedBy)
        
        model.save()
        qt = MasterProject.objects.latest('id')
        fetchid = qt.id
        if len(request.FILES.getlist('Attach'))!=0:
            try:
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

                    att=Attachment(File=attachmentsImage_url, Caption=Caption, LinkType="MasterProject", LinkID=fetchid, CreateDate=CreateDate, CreateTime=CreateTime, UpdateDate=CreateDate, UpdateTime=CreateTime)
                    
                    att.save()                        
                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                assignByName = "Admin/Manager"

                if Employee.objects.filter(SalesEmployeeCode = CreatedBy).exists():
                    empobj = Employee.objects.get(SalesEmployeeCode = CreatedBy)
                    CreatedByName = empobj.SalesEmployeeName

                if Employee.objects.filter(SalesEmployeeCode = project_owner).exists():
                    empobj = Employee.objects.get(SalesEmployeeCode = project_owner)
                    assignByName = empobj.SalesEmployeeName

                # In App Notificition
                Title = "New Master Project"
                Description = f"New Master Project is created by {CreatedByName} assign to {assignByName}"
                Type = "Master Project Create"
                SourceType = "MasterProject"
                SourceID = fetchid
                Emp = project_owner
                result = CreateInAppNotification(Title = Title, Description = Description, Type = Type, SourceType = SourceType, SourceID = SourceID, Emp = Emp)
                print("##########CreateInAppNotification", result)
                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

                return Response({"message":"successful","status":"200","data":[]})
            except Exception as e:
                MasterProject.objects.filter(pk=fetchid).delete()
                return Response({"message":str(e),"status":"201","data":[]})
        else:
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            assignByName = "Admin/Manager"

            if Employee.objects.filter(SalesEmployeeCode = CreatedBy).exists():
                empobj = Employee.objects.get(SalesEmployeeCode = CreatedBy)
                CreatedByName = empobj.SalesEmployeeName

            if Employee.objects.filter(SalesEmployeeCode = project_owner).exists():
                empobj = Employee.objects.get(SalesEmployeeCode = project_owner)
                assignByName = empobj.SalesEmployeeName

            # In App Notificition
            Title = "New Master Project"
            Description = f"New Master Project is created by {CreatedByName} assign to {assignByName}"
            Type = "Master Project Create"
            SourceType = "MasterProject"
            SourceID = fetchid
            Emp = project_owner
            result = CreateInAppNotification(Title = Title, Description = Description, Type = Type, SourceType = SourceType, SourceID = SourceID, Emp = Emp)
            print("##########CreateInAppNotification", result)
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            return Response({"message":"successful","status":"200","data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":"201","data":[]})

#Project All API
@api_view(["POST"])
def master_all(request):
    try:
        allProject = []
        CardCode=request.data['CardCode']
        Projects_objs = MasterProject.objects.filter(Q(CardCode=CardCode)).order_by("-id")
        for Obj in Projects_objs:            
            ObjJson = MasterProjectSerializer(Obj, many=False)
            ObjJson = json.loads(json.dumps(ObjJson.data))
            #print(ObjJson)

            Attach = Attachment.objects.filter(LinkType="MasterProject", LinkID=Obj.id)
            AttachJson = AttachmentSerializer(Attach, many=True)
            
            ObjJson['Attach'] = AttachJson.data
            #print(ObjJson)
            allProject.append(ObjJson)
        return Response({"message": "Success","status": 200,"data":allProject})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})

#Project One API
@api_view(["POST"])
def master_one(request):
    try:
        id=request.data['id']
        Project_obj = MasterProject.objects.get(id=id)
        Project_json = MasterProjectSerializer(Project_obj)
        return Response({"message": "Success","status": 200,"data":[Project_json.data]})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})

#Project Update API
@api_view(['POST'])
def master_update(request):
    try:
        fetchid = request.data['id']
        model = MasterProject.objects.get(pk = fetchid)
        model.name = request.data['name']
        model.contact_person = request.data['contact_person']
        model.order_id = request.data['order_id']
        model.start_date = request.data['start_date']
        model.target_date = request.data['target_date']
        model.details = request.data['details']
        model.CardCode = request.data['CardCode']
        model.location = request.data['location']
        model.project_owner = request.data['project_owner']
        model.project_cost = request.data['project_cost']
        model.project_status = request.data['project_status']
        model.address = request.data['address']
        model.save()            
        return Response({"message":"successful","status":"200","data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":"201","data":[]})

#Project Update API
@api_view(['POST'])
def stage_update(request):
    try:
        fetchid = request.data['id']
        request.data._mutable = True
        #request.data['Data'] = json.dumps(request.data['Data'])
        request.data['Data'] = request.data['Data']
        dd = ProjectStage.objects.get(pk=fetchid)
        data = ProjectStageSerializer(instance=dd, data=request.data)     
        attMsg="Success"
        if data.is_valid():
            data.save()
        
            UpdateDate = request.data['UpdateDate']
            UpdateTime = request.data['UpdateTime']
            
            if len(request.FILES.getlist('Attach')) > 0:
                try:
                    for File in request.FILES.getlist('Attach'):
                        attachmentsImage_url = ""
                        target ='./bridge/static/image/Attachment'
                        os.makedirs(target, exist_ok=True)
                        fss = FileSystemStorage()
                        file = fss.save(target+"/"+File.name, File)
                        productImage_url = fss.url(file)
                        attachmentsImage_url = productImage_url.replace('/bridge', '')
                        print(attachmentsImage_url)

                        att=Attachment(File=attachmentsImage_url, Caption=File.name, LinkType="ProjectStage", LinkID=fetchid, CreateDate=UpdateDate, CreateTime=UpdateTime, UpdateDate=UpdateDate, UpdateTime=UpdateTime)
                        
                        att.save() 
                except Exception as e:
                    attMsg = str(e)
            
            if Tickets.objects.filter(DeliveryID=fetchid, Stageno=float(dd.Stageno)).exists():
                tkt = Tickets.objects.get(DeliveryID=fetchid, Stageno=float(dd.Stageno))
                tkt.Data = request.data['Data']
                tkt.save()
            return Response({"message":"successful","status":"200","data":[{"AttachmentMsg":str(attMsg)}]})
        else:
            return Response({"message":"ID Wrong","status":"201","data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":"201","data":[]})
        
#Project Update API
@api_view(['POST'])
def stage_complete(request):
    try:
        fetchid = request.data['id']
        cur_stage = ProjectStage.objects.get(pk=fetchid)
        print(cur_stage)
        cur_stage.Status = request.data['Status']
        cur_stage.save()
        project = Project.objects.get(id=cur_stage.ProjectId)
        
        if project.DepName =="New Product":
            ProjectType = "Installation"
        else:
            ProjectType = project.DepName
            
        print("project", project)
        item = ProjectItem.objects.get(ProjectId=project.id)
        print("item",item)
        BP = BusinessPartner.objects.get(CardCode=project.CardCode)
        if int(request.data['Status']) == 1:
            if int(cur_stage.Stageno) !=20:
                stg = int(cur_stage.Stageno)+1
                print("next ", stg)
                next_stg = ProjectStage.objects.get(Stageno=stg, ProjectId=cur_stage.ProjectId)
                if Tickets.objects.filter(DeliveryID=next_stg.id).exists():
                    print('exist')
                else:
                    if "Invoice" not in next_stg.Name:
                        tkt = SubType.objects.get(Type=ProjectType, Stageno=stg)
                        print("tkt ", tkt)
                        print(tkt.id)
                        print(tkt.Type)
                        print(tkt.SubType)
                        Tick.auto_ticket(project,item, BP, cur_stage, next_stg, tkt)
        
        return Response({"message":"successful","status":"200","data":[]})
    except Exception as e:
        return Response({"message":str(e),"status":"201","data":[]})

#Master Project Listing Without Condition
@api_view(["GET"])
def master_project_all(request):
    try:
        allProject = []
        Projects_objs = MasterProject.objects.all().order_by("-id")
        for Obj in Projects_objs:            
            ObjJson = MasterProjectSerializer(Obj, many=False)
            ObjJson = json.loads(json.dumps(ObjJson.data))

            Attach = Attachment.objects.filter(LinkType="Project", LinkID=Obj.id)
            AttachJson = AttachmentSerializer(Attach, many=True)
            
            ObjJson['Attach'] = AttachJson.data
            allProject.append(ObjJson)
        return Response({"message": "Success","status": 200,"data":allProject})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})

#Project Listing 
@api_view(["POST"])
def master_project_filter(request):
    try:
        SalesPersonID = request.data['SalesPersonCode']
        Team = request.data['Team']
        if Employee.objects.filter(SalesEmployeeCode=SalesPersonID).exists():
            #empids = EmpView.GetTeam(SalesPersonID, Team)            
            empids = getAllReportingToIds(SalesPersonID)            
        
        Projects_objs_ids = MasterProject.objects.filter(Q(project_owner__in=empids) | Q(CreatedBy__in=empids)).values_list("id", flat=True)
        
        ProjectIds = ProjectStage.objects.filter(Q(StageAssign__in=empids) | Q(StageOwner__in=empids)).distinct().order_by("ProjectId").values_list("ProjectId", flat=True)
        
        Projects_objs_ids1 = MasterProject.objects.filter(pk__in=ProjectIds).values_list("id", flat=True)
        
        both = list(Projects_objs_ids)+list(Projects_objs_ids1)
        uniq = set(both)
        uniq_list = list(both)
        print("uniq list",uniq_list)

        allProject = []
        
        Projects_objs = MasterProject.objects.filter(Q(pk__in=uniq_list)).order_by("-id")
        for Obj in Projects_objs:            
            ObjJson = MasterProjectSerializer(Obj, many=False)
            ObjJson = json.loads(json.dumps(ObjJson.data))

            Attach = Attachment.objects.filter(LinkType="MasterProject", LinkID=Obj.id)
            AttachJson = AttachmentSerializer(Attach, many=True)
            
            ObjJson['Attach'] = AttachJson.data
            ObjJson['project_owner_name'] = EmpView.GetSalesEmployeeName(Obj.project_owner)
            ObjJson['contact_person_name'] = EmpView.GetContactPersonName(Obj.contact_person)
            ObjJson['CardName'] = EmpView.GetCardName(Obj.CardCode)
            allProject.append(ObjJson)
        return Response({"message": "Success","status": 200,"data":allProject})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})


#Project Listing 
@api_view(["POST"])
def project_filter(request):
    try:
        SalesPersonID = request.data['SalesPersonCode']
        Team = request.data['Team']
        if Employee.objects.filter(SalesEmployeeCode=SalesPersonID).exists():
            #empids = EmpView.GetTeam(SalesPersonID, Team)            
            empids = getAllReportingToIdsSubdep(SalesPersonID, Team)            
        
        allProject = []
        Projects_objs = Project.objects.filter(project_owner__in=empids).order_by("-id")
        for Obj in Projects_objs:            
            ObjJson = ProjectSerializer(Obj, many=False)
            ObjJson = json.loads(json.dumps(ObjJson.data))

            Attach = Attachment.objects.filter(LinkType="Project", LinkID=Obj.id)
            AttachJson = AttachmentSerializer(Attach, many=True)
            
            ObjJson['Attach'] = AttachJson.data

            Itms = ProjectItem.objects.filter(ProjectId=Obj.id)
            ItmJson = ProjectItemSerializer(Itms, many=True)
            
            ObjJson['ProjectItem'] = ItmJson.data

            allProject.append(ObjJson)
        return Response({"message": "Success","status": 200,"data":allProject})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})

#Project Listing 
@api_view(["POST"])
def master_project_filter_key(request):
    try:
        res = GetMasterProject(**request.data)
        return Response({"message": "Success","status": 200,"data":res})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})

#Project Listing 
@api_view(["POST"])
def project_filter_key(request):
    try:
        res = GetProject(**request.data)
        return Response({"message": "Success","status": 200,"data":res})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})

def GetMasterProject(**inp):
    print("--",inp['filter'])
    print("*--",*inp['fields'])
    
    if MasterProject.objects.filter(**inp['filter']).exists():
        #{"filter":{"order_id":113, "project_owner":99}, "fields":["id","name","order_id"]}
        Objs = MasterProject.objects.filter(**inp['filter']).values(*inp['fields']).order_by("-id")
        ObjJson = MasterProjectSerializer(Objs, many=True)
        return ObjJson.data
        #return Response({"message": "Success","status": 200,"data":ObjJson.data})
    else:      
        return []
        #return Response({"message": "Success","status": 200,"data":[]})


def GetProject(**inp):
    print("--",inp['filter'])
    print("*--",*inp['fields'])
    
    if Project.objects.filter(**inp['filter']).exists():
        #{"filter":{"order_id":113, "project_owner":99}, "fields":["id","name","order_id"]}
        Objs = Project.objects.filter(**inp['filter']).values(*inp['fields']).order_by("-id")
        ObjJson = ProjectSerializer(Objs, many=True)
        return ObjJson.data
        #return Response({"message": "Success","status": 200,"data":ObjJson.data})
    else:      
        return []
        #return Response({"message": "Success","status": 200,"data":[]})

#Project Satge One API
@api_view(["POST"])
def stage_one(request):
    try:
        id=request.data['id']
        Stage_obj = ProjectStage.objects.get(id=id)
        Stage_json = ProjectStageSerializer(Stage_obj)
        
        ObjJson = json.loads(json.dumps(Stage_json.data))
        print(ObjJson)
        
        if Employee.objects.filter(SalesEmployeeCode=Stage_obj.StageOwner).exists():
                OwnerName = Employee.objects.filter(SalesEmployeeCode=Stage_obj.StageOwner).values('SalesEmployeeName')
                ObjJson['StageOwnerName'] = OwnerName[0]['SalesEmployeeName']
                print(OwnerName[0]['SalesEmployeeName'])
        else:
            ObjJson['StageOwnerName'] = ""
        
        if Employee.objects.filter(SalesEmployeeCode=Stage_obj.StageAssign).exists():
           AssignName = Employee.objects.filter(SalesEmployeeCode=Stage_obj.StageAssign).values('SalesEmployeeName')
           ObjJson['StageAssignName'] = AssignName[0]['SalesEmployeeName']
        else:
           ObjJson['StageAssignName'] = ""
               
        Attach = Attachment.objects.filter(LinkType="ProjectStage", LinkID=id)
        AttachJson = AttachmentSerializer(Attach, many=True)
        
        ObjJson['Attach'] = AttachJson.data

        return Response({"message": "Success","status": 200,"data":[ObjJson]})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})


#get all stage by project id    
@api_view(["POST"])    
def stage_all(request):
    pid = request.data['pid']
    # stg = ProjectStage.objects.filter(ProjectId=pid).order_by('Stageno')
    # stg_json = ProjectStageSerializer(stg, many=True)
    # return Response({"message":"Success", "status":200, "data":stg_json.data})
    
    try:
        allStage = []
        try:
            stg_objs = ProjectStage.objects.filter(ProjectId=pid, Stageno=request.data['Stageno']).order_by('Stageno')
        except:
            stg_objs = ProjectStage.objects.filter(ProjectId=pid).order_by('Stageno')
        for Obj in stg_objs:            
            ObjJson = ProjectStageSerializer(Obj, many=False)
            ObjJson = json.loads(json.dumps(ObjJson.data))
            if Employee.objects.filter(SalesEmployeeCode=Obj.StageOwner).exists():
                OwnerName = Employee.objects.filter(SalesEmployeeCode=Obj.StageOwner).values('SalesEmployeeName')
                ObjJson['StageOwnerName'] = OwnerName[0]['SalesEmployeeName']
                print(OwnerName[0]['SalesEmployeeName'])
            else:
                ObjJson['StageOwnerName'] = ""
            if Employee.objects.filter(SalesEmployeeCode=Obj.StageAssign).exists():
               AssignName = Employee.objects.filter(SalesEmployeeCode=Obj.StageAssign).values('SalesEmployeeName')
               ObjJson['StageAssignName'] = AssignName[0]['SalesEmployeeName']
            else:
               ObjJson['StageAssignName'] = ""
            
            
            ObjJson = json.loads(json.dumps(ObjJson))
            print(ObjJson)
            if Attachment.objects.filter(LinkType="ProjectStage", LinkID=Obj.id).exists():
                Attach = Attachment.objects.filter(LinkType="ProjectStage", LinkID=Obj.id)
                AttachJson = AttachmentSerializer(Attach, many=True)
                
                ObjJson['Attach'] = AttachJson.data
            else:
                ObjJson['Attach'] = []            
            
            allStage.append(ObjJson)
        return Response({"message": "Success","status": 200,"data":allStage})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})

#get all stage by project id    
@api_view(["POST"])    
def stage_all_bytype(request):
    Name = request.data['Type']
    # stg = ProjectStage.objects.filter(ProjectId=pid).order_by('Stageno')
    # stg_json = ProjectStageSerializer(stg, many=True)
    # return Response({"message":"Success", "status":200, "data":stg_json.data})
    
    try:
        allStage = []
        #stg_objs = ProjectStage.objects.filter(Name=Name).order_by('Stageno')
        stg_objs = ProjectStage.objects.filter(Name=Name).order_by('-id')
        for Obj in stg_objs:            
            ObjJson = ProjectStageSerializer(Obj, many=False)
            ObjJson = json.loads(json.dumps(ObjJson.data))
            if Employee.objects.filter(SalesEmployeeCode=Obj.StageOwner).exists():
                OwnerName = Employee.objects.filter(SalesEmployeeCode=Obj.StageOwner).values('SalesEmployeeName')
                ObjJson['StageOwnerName'] = OwnerName[0]['SalesEmployeeName']
                print(OwnerName[0]['SalesEmployeeName'])
            else:
                ObjJson['StageOwnerName'] = ""
            if Employee.objects.filter(SalesEmployeeCode=Obj.StageAssign).exists():
               AssignName = Employee.objects.filter(SalesEmployeeCode=Obj.StageAssign).values('SalesEmployeeName')
               ObjJson['StageAssignName'] = AssignName[0]['SalesEmployeeName']
            else:
               ObjJson['StageAssignName'] = ""
            allStage.append(ObjJson)
        return Response({"message": "Success","status": 200,"data":allStage})
    except Exception as e:
        return Response({"message": str(e),"status": 201,"data":[]})
    
    
#get all StaticStage
@api_view(["POST"])    
def static_stage_all(request):
    stg = ProjectStaticstage.objects.filter(DepName=request.data['DepName']).order_by('Stageno')
    stg_json = ProjectStaticstageSerializer(stg, many=True)
    return Response({"message":"Success", "status":200, "data":stg_json.data})
    
