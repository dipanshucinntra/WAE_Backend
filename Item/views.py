from datetime import datetime, timezone
from django.conf import settings
from django.shortcuts import render, redirect  
from django.http import JsonResponse, HttpResponse

from Employee.models import Employee
from Notification.models import Notification
import Order
from .models import *
import requests, json

from rest_framework.decorators import api_view    
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import JSONParser
from django.db.models import Q
# Create your views here.  

# date = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d')
# yearmonth = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m')
# time = datetime.now(timezone("Asia/Kolkata")).strftime('%H:%M %p')

#Item All API
@api_view(["POST"])
def all(request):
    ItemsGroupCode = request.data['ItemsGroupCode']
    if ItemsGroupCode !="":
        item_obj = Item.objects.filter(Q(ItemsGroupCode=ItemsGroupCode), Q(approval_status="Approved"))
        item_list = []
        for obj in item_obj:
            item_json = ItemSerializer(obj, many=False).data
            cat_obj = Category.objects.filter(id=obj.ItemsGroupCode.id).first()
            cat_name = cat_obj.GroupName
            item_json["Category_name"] = cat_name
            item_list.append(item_json)
        return Response({"message": "Success","status": 200,"data":item_list})
    else:
        item_obj = Item.objects.all()
        item_list = []
        for obj in item_obj:
            item_json = ItemSerializer(obj, many=False).data
            cat_obj = Category.objects.filter(id=obj.ItemsGroupCode.id).first()
            cat_name = cat_obj.GroupName
            item_json["Category_name"] = cat_name
            item_list.append(item_json)
        return Response({"message": "Success","status": 200,"data":item_list})
    
@api_view(['POST'])    
def all_pending(request):
    try:
        item_obj=""
        approval_status =  request.data['approval_status']
        if approval_status == "All":
            item_obj = Item.objects.all().order_by('-id')    
            print(item_obj)      
        else:
            item_obj = Item.objects.filter(approval_status=approval_status).order_by('-id')          
        item_json = ItemPendingSerializer(item_obj, many=True)         
        return Response({"message": "Success","status": 200,"data":item_json.data})
    except Exception as e:
        return Response({"message": str(e),"status": 500})


#Item All API
@api_view(["GET"])
def all1(request):
    #item_obj = Item.objects.filter(pk=10,ItemsGroupCode=110).values("id","ItemCode","ItemName")
    item_obj = Item.objects.all().values("ItemCode","ItemName")
    print(item_obj)
    item_json = ItSerializer(item_obj, many=True)
    return Response({"message": "Success","status": 200,"data":item_json.data})

#Item One API
@api_view(["POST"])
def one(request):
    id=request.data['id']
    item_obj = Item.objects.get(id=id)
    item_json = ItemSerializer(item_obj, many=False)
    return Response({"message": "Success","status": 200,"data":item_json.data})

#Tax All API
@api_view(["GET"])
def tax_all(request):
    tax_obj = Tax.objects.all()
    tax_json = TaxSerializer(tax_obj, many=True)
    return Response({"message": "Success","status": 200,"data":tax_json.data})


# function created by abhishek
@api_view(["GET"])
def distributionlist(Request):
    obj = Department.objects.all()
    json = DepartmentSerializer(obj, many=True)
    return Response({"message": "Success","status": 200,"data":json.data})

# function created by abhishek
@api_view(["GET"])
def distributionlist_old(Request):
    try:
        # with open("./bridge/db.json") as f:
            
            # 

            


        # Loin to create session variable
        loginResponse = requests.post(settings.BASEURL+'/Login', data=json.dumps(settings.SAPDB), verify=False, timeout=3)
        token = json.loads(loginResponse.text)['SessionId']
        print(token)

        # get number of data exist in Distribution table
        dlist = requests.get(settings.BASEURL+'/DistributionRules?$select=FactorCode,FactorDescription&$filter=InWhichDimension eq 2', cookies=loginResponse.cookies, verify=False)
        print(dlist.json())
        totalRow = dlist.json()
        return Response({"message":"successful","status":"200","data":totalRow['value']})
    except Exception as e:
        return Response({"message":"Error","status":"201","data":[str(e)]})


#added by millan for item create on 11-10-2022        
@api_view(['POST'])
def create(request):
    # try:
        UnitPrice = request.data['UnitPrice']
        Currency = request.data['Currency']
        DiscountPercent = request.data['DiscountPercent']
        ItemCode = request.data['ItemCode']
        ItemName = request.data['ItemName']
        TaxCode = request.data['TaxCode']
        U_DIV = request.data['U_DIV']
        InStock = request.data['InStock']
        ItemsGroupCode = request.data['ItemsGroupCode']
        UomNo = request.data['UomNo']
        ################New Fields Add [DK]##############
        Tap_Qty = request.data['Tap_Qty']
        Tap_Type = request.data['Tap_Type']
        Ht_Capacity = request.data['Ht_Capacity']
        Ct_Capacity = request.data['Ct_Capacity']
        At_Capacity = request.data['At_Capacity']
        Pro_Capacity = request.data['Pro_Capacity']
        Machine_Dimension = request.data['Machine_Dimension']
        Machine_Colour = request.data['Machine_Colour']
        Type_of_Machine = request.data['Type_of_Machine']
        Machine_Body_Material = request.data['Machine_Body_Material']
        Special_Remark = request.data['Special_Remark']

        ItemsGroupMasterCode = request.data['ItemsGroupMasterCode']
        ItemsGroupMasterCode_obj = ItemGroupMaster.objects.filter(Number=ItemsGroupMasterCode).first()
        ItemsGroupCode_obj = Category.objects.filter(id=ItemsGroupCode).first()

        print("xx",ItemsGroupMasterCode_obj)
        print("yy",ItemsGroupCode_obj, ItemsGroupCode)

        if not Item.objects.filter(ItemName=ItemName, Pro_Capacity=Pro_Capacity).exists():
            ################New Fields Add [DK]##############
            model = Item(UnitPrice = UnitPrice, Currency = Currency, DiscountPercent = DiscountPercent, ItemCode = ItemCode, ItemName = ItemName, TaxCode = TaxCode, U_DIV = U_DIV, InStock = InStock, ItemsGroupCode = ItemsGroupCode_obj, UomNo = UomNo
                        , Tap_Qty=Tap_Qty, Tap_Type=Tap_Type, Ht_Capacity=Ht_Capacity, Ct_Capacity=Ct_Capacity, At_Capacity=At_Capacity,
                        Pro_Capacity=Pro_Capacity, Machine_Dimension=Machine_Dimension, Machine_Colour=Machine_Colour, 
                        Type_of_Machine=Type_of_Machine, Machine_Body_Material=Machine_Body_Material, Special_Remark=Special_Remark,ItemsGroupMasterCode=ItemsGroupMasterCode_obj)
            
            model.save()
            
            itm_id = Item.objects.latest('id')
            # cat_obj = Category.objects.get(id=ItemsGroupCode)
            ItCode = "IT"+str(format(itm_id.id, '04'))
            # ItCode = cat_obj.GroupName[:2].upper() +"."+ ItemName[:2].upper() + "." + Pro_Capacity + "." + str(format(itm_id.id, '04'))
            itm_id.ItemCode = ItCode
            itm_id.save()
            
            return Response({"message":"success","status":200,"data":[]}) 
        else:
            return Response({"message":"Duplicate Item","status":400,"data":[]}) 
        
    # except Exception as e:
    #     return Response({"message":str(e),"status":201,"data":[]})    
    
#Item Update API created by millan on 03-November-2022
@api_view(['POST'])
def update(request):
    try:
        fetchid = request.data['id']
        model = Item.objects.get(pk = fetchid)
        model.UnitPrice = request.data['UnitPrice']
        model.Currency = request.data['Currency']
        model.DiscountPercent = request.data['DiscountPercent']
        model.ItemCode = request.data['ItemCode']
        model.ItemName = request.data['ItemName']
        model.TaxCode = request.data['TaxCode']
        model.U_DIV = request.data['U_DIV']
        model.InStock = request.data['InStock']
        model.ItemsGroupCode_id = request.data['ItemsGroupCode']
        model.UomNo = request.data['UomNo']
        ################New Fields Add [DK]##############
        model.Tap_Qty = request.data['Tap_Qty']
        model.Tap_Type = request.data['Tap_Type']
        model.Ht_Capacity = request.data['Ht_Capacity']
        model.Ct_Capacity = request.data['Ct_Capacity']
        model.At_Capacity = request.data['At_Capacity']
        model.Pro_Capacity = request.data['Pro_Capacity']
        model.Machine_Dimension = request.data['Machine_Dimension']
        model.Machine_Colour = request.data['Machine_Colour']
        model.Type_of_Machine = request.data['Type_of_Machine']
        model.Machine_Body_Material = request.data['Machine_Body_Material']
        model.Special_Remark = request.data['Special_Remark']
        model.approval_status = "Pending"
        ################New Fields Add [DK]##############
        model.save()
        
        context = {
            "UnitPrice"   : request.data['UnitPrice'],
            "Currency"    : request.data['Currency'],
            "DiscountPercent" : request.data['DiscountPercent'],
            "ItemCode"    : request.data['ItemCode'],
            "ItemName"    : request.data['ItemName'],
            "TaxCode" : request.data['TaxCode'],
            "U_DIV"   : request.data['U_DIV'],
            "InStock" : request.data['InStock'],
            "ItemsGroupCode"  : request.data['ItemsGroupCode'],
            "UomNo"   : request.data['UomNo'],            
        }
        
        return Response({"message":"success","status":200,"data":[context]}) 
    
    except Exception as e:
        return Response({"message":str(e),"status":201,"data":[]}) 

#Item Delete API by millan on 03-November-2022
@api_view(['POST'])
def delete(request):
    fetchid= request.data['id']
    try:
        Item.objects.filter(pk=fetchid).delete()
             
        return Response({"message":"successful","status":"200","data":[]})   
    except:
        return Response({"message":"Id wrong","status":"201","data":[]})


@api_view(["POST"])
def itemremarksHistory(request):
    try:
        qtid = request.data['id']
        allRemarks = []
        if ItemOrderStatusRemarks.objects.filter(item_id = qtid).exists():
            remarkObj = ItemOrderStatusRemarks.objects.filter(item_id = qtid)
            print(remarkObj)
            # remarkJson = QuotStatusRemarksSerializer(remarkObj, many=True)
            for obj in remarkObj:
                SalesEmployeeCode = obj.SalesEmployeeCode
                remarkJson = ItemOrderStatusRemarksSerializer(obj)
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


@api_view(['POST'])
def approve(request):
    SalesEmployeeCode = request.data['SalesEmployeeCode']
    Item_id = request.data['id']
    FinalStatus = request.data['FinalStatus']
    Remarks = request.data['Remarks']
    iten_obj = Item.objects.filter(id=Item_id).first()
    iten_obj.approval_status = FinalStatus
    iten_obj.approved_by = SalesEmployeeCode
    iten_obj.save()
    ItemOrderStatusRemarks(item_id = Item_id, SalesEmployeeCode = SalesEmployeeCode, Status = FinalStatus, Remarks = Remarks).save()
    # if FinalStatus == "Approved":        
    #     Item.objects.filter(id=Item_id).update(approval_status="Approved")
    # elif FinalStatus == "Rejected":   
    #     Item.objects.filter(id=Item_id).update(approval_status="Rejected")
    # send_notify = Notification(Title="Item status", Description="Click To Check", Type="Action", Read="0", SourceType="Item", SourceID=Item_id, Emp=order_obj.SalesPersonCode, SourceTime=time, CreatedDate=date, CreatedTime=time)    
    # send_notify.save()          
    return Response({"message":"Success","status":200,"data":[]})



# #Item All Filter API
# @api_view(["POST"])
# def all_filter(request):
#     PageNo = request.data['PageNo']
#     MaxItem = request.data['MaxItem']
#     ItemsGroupCode = request.data['ItemsGroupCode']
#     ItemsGroupMasterCode = request.data['ItemsGroupMasterCode']

#     if MaxItem != "All":
#         endWith = (PageNo * int(MaxItem))
#         startWith = (endWith - int(MaxItem))

#     if MaxItem != "All":
#         if ItemsGroupCode!="":
#             item_obj = Item.objects.filter(ItemsGroupCode=ItemsGroupCode, ItemsGroupMasterCode=ItemsGroupMasterCode).order_by('ItemName')[startWith:endWith]
#             item_count = Item.objects.filter(ItemsGroupCode=ItemsGroupCode, ItemsGroupMasterCode=ItemsGroupMasterCode).count()
#         else:
#             item_obj = Item.objects.filter(ItemsGroupMasterCode=ItemsGroupMasterCode).order_by('ItemName')[startWith:endWith]
#             item_count = Item.objects.filter(ItemsGroupMasterCode=ItemsGroupMasterCode).count()
#     else:
#         if ItemsGroupCode!="":
#             item_obj = Item.objects.filter(ItemsGroupCode=ItemsGroupCode, ItemsGroupMasterCode=ItemsGroupMasterCode).order_by('ItemName')
#             item_count = item_obj.count()
#         else:
#             item_obj = Item.objects.filter(ItemsGroupMasterCode=ItemsGroupMasterCode).order_by('ItemName')
#             item_count = item_obj.count()
#     item_list = []
#     for obj in item_obj:
#         item_json = ItemSerializer(obj, many=False).data
#         cat_obj = Category.objects.filter(id=obj.ItemsGroupCode.id).first()
#         cat_name = cat_obj.GroupName
#         item_json["Category_name"] = cat_name
#         item_list.append(item_json)
#     return Response({"message": "Success","status": 200,"data":item_list, "extra":{"total_count":item_count}})


#Item All Filter API
@api_view(["POST"])
def all_filter(request):
    PageNo = request.data['PageNo']
    MaxItem = request.data['MaxItem']
    ItemsGroupCode = request.data['ItemsGroupCode']
    ItemsGroupMasterCode = request.data['ItemsGroupMasterCode']
    Search = request.data["SearchText"]
    if MaxItem != "All":
        endWith = (PageNo * int(MaxItem))
        startWith = (endWith - int(MaxItem))

    if MaxItem != "All":
        if ItemsGroupCode!="":
            item_obj = Item.objects.filter(Q(ItemsGroupCode=ItemsGroupCode, ItemsGroupMasterCode=ItemsGroupMasterCode, ItemsGroupCode__GroupName__icontains=Search, approval_status="Approved")|Q(ItemsGroupCode=ItemsGroupCode, ItemsGroupMasterCode=ItemsGroupMasterCode, ItemCode__icontains=Search, approval_status="Approved")|Q(ItemsGroupCode=ItemsGroupCode, ItemsGroupMasterCode=ItemsGroupMasterCode, ItemName__icontains=Search, approval_status="Approved")|Q(ItemsGroupCode=ItemsGroupCode, ItemsGroupMasterCode=ItemsGroupMasterCode, UnitPrice__icontains=Search, approval_status="Approved")).order_by('ItemName')[startWith:endWith]
            item_count = Item.objects.filter(Q(ItemsGroupCode=ItemsGroupCode, ItemsGroupMasterCode=ItemsGroupMasterCode, ItemsGroupCode__GroupName__icontains=Search, approval_status="Approved")|Q(ItemsGroupCode=ItemsGroupCode, ItemsGroupMasterCode=ItemsGroupMasterCode, ItemCode__icontains=Search, approval_status="Approved")|Q(ItemsGroupCode=ItemsGroupCode, ItemsGroupMasterCode=ItemsGroupMasterCode, ItemName__icontains=Search, approval_status="Approved")|Q(ItemsGroupCode=ItemsGroupCode, ItemsGroupMasterCode=ItemsGroupMasterCode, UnitPrice__icontains=Search, approval_status="Approved")).count()
            # item_count = Item.objects.filter(ItemsGroupCode=ItemsGroupCode, ItemsGroupMasterCode=ItemsGroupMasterCode).count()
        else:
            item_obj = Item.objects.filter(Q(ItemsGroupMasterCode=ItemsGroupMasterCode, ItemsGroupCode__GroupName__icontains=Search, approval_status="Approved")|Q(ItemsGroupMasterCode=ItemsGroupMasterCode, ItemCode__icontains=Search, approval_status="Approved")|Q(ItemsGroupMasterCode=ItemsGroupMasterCode, ItemName__icontains=Search, approval_status="Approved")|Q(ItemsGroupMasterCode=ItemsGroupMasterCode, UnitPrice__icontains=Search, approval_status="Approved")).order_by('ItemName')[startWith:endWith]
            item_count = Item.objects.filter(Q(ItemsGroupMasterCode=ItemsGroupMasterCode, ItemsGroupCode__GroupName__icontains=Search, approval_status="Approved")|Q(ItemsGroupMasterCode=ItemsGroupMasterCode, ItemCode__icontains=Search, approval_status="Approved")|Q(ItemsGroupMasterCode=ItemsGroupMasterCode, ItemName__icontains=Search, approval_status="Approved")|Q(ItemsGroupMasterCode=ItemsGroupMasterCode, UnitPrice__icontains=Search, approval_status="Approved")).count()
            # item_count = Item.objects.filter(ItemsGroupMasterCode=ItemsGroupMasterCode).count()
    else:
        if ItemsGroupCode!="":
            item_obj = Item.objects.filter(Q(ItemsGroupCode=ItemsGroupCode, ItemsGroupMasterCode=ItemsGroupMasterCode, ItemsGroupCode__GroupName__icontains=Search, approval_status="Approved")|Q(ItemsGroupCode=ItemsGroupCode, ItemsGroupMasterCode=ItemsGroupMasterCode, ItemCode__icontains=Search, approval_status="Approved")|Q(ItemsGroupCode=ItemsGroupCode, ItemsGroupMasterCode=ItemsGroupMasterCode, ItemName__icontains=Search, approval_status="Approved")|Q(ItemsGroupCode=ItemsGroupCode, ItemsGroupMasterCode=ItemsGroupMasterCode, UnitPrice__icontains=Search, approval_status="Approved")).order_by('ItemName')
            # item_obj = Item.objects.filter(ItemsGroupCode=ItemsGroupCode, ItemsGroupMasterCode=ItemsGroupMasterCode).order_by('ItemName')
            item_count = item_obj.count()
        else:
            item_obj = Item.objects.filter(Q(ItemsGroupMasterCode=ItemsGroupMasterCode, ItemsGroupCode__GroupName__icontains=Search, approval_status="Approved")|Q(ItemsGroupMasterCode=ItemsGroupMasterCode, ItemCode__icontains=Search, approval_status="Approved")|Q(ItemsGroupMasterCode=ItemsGroupMasterCode, ItemName__icontains=Search, approval_status="Approved")|Q(ItemsGroupMasterCode=ItemsGroupMasterCode, UnitPrice__icontains=Search, approval_status="Approved")).order_by('ItemName')
            # item_obj = Item.objects.filter(ItemsGroupMasterCode=ItemsGroupMasterCode).order_by('ItemName')
            item_count = item_obj.count()
            
    item_list = []
    for obj in item_obj:
        item_json = ItemSerializer(obj, many=False).data
        cat_obj = Category.objects.filter(id=obj.ItemsGroupCode.id).first()
        cat_name = cat_obj.GroupName
        item_json["Category_name"] = cat_name
        item_list.append(item_json)
    return Response({"message": "Success","status": 200,"data":item_list, "extra":{"total_count":item_count}})





#Item All Filter API
@api_view(["GET"])
def all_item_group(request):
    item_group = ItemGroupMaster.objects.all()
    serializer = ItemGroupMasterSerializer(item_group, many=True)
    return Response({"message": "Success","status": 200,"data":serializer.data})


################ CODE ADDED BY DIPANSHU FROM STANDALONE SUPPORT ##########
#Item Count API
@api_view(["POST"])
def item_count(request):
    try:
        ItemsGroupCode = request.data['ItemsGroupCode']

        item_count = Item.objects.filter(ItemsGroupCode_id = ItemsGroupCode).count()
        context = {
            "Count": item_count
        }
        print(item_count)
        return Response({"message": "Success","status": 200,"data":[context]})
    except Exception as e:
        return Response({"message": "Error", "status": 201, "data":[str(e)]})

@api_view(['POST'])
def searchInItems(request):
    try:
        SearchText = request.data['SearchText']
        PageNo = request.data['PageNo']
        MaxItem = 50
        endWith = (PageNo * MaxItem)
        startWith = (endWith - MaxItem)

        itemsObj = ""
        item_count = 0
        if 'ItemsGroupCode' in request.data:
            ItemsGroupCode = request.data['ItemsGroupCode']
            itemsObj = Item.objects.filter(
                Q(ItemsGroupCode = ItemsGroupCode) &
                Q(
                    Q(ItemCode__icontains = SearchText) |
                    Q(ItemName__icontains = SearchText)
                )
            ).order_by('-id')[startWith:endWith]

            item_count = Item.objects.filter(ItemsGroupCode_id = ItemsGroupCode).count()

        else:
            itemsObj = Item.objects.filter(
                Q(ItemCode__icontains = SearchText) |
                Q(ItemName__icontains = SearchText)
            ).order_by('-id')[startWith:endWith]

            item_count = Item.objects.filter( Q(ItemCode__icontains = SearchText) | Q(ItemName__icontains = SearchText) ).count()
            

        # itemsJson = ItemSerializer(itemsObj, many=True)
        itemData = showItems(itemsObj)
        
        return Response({"message": "Success","status": 200, "count": item_count, "data":itemData})
    except Exception as e:
        return Response({"message": "Error", "status": 201, "count": 0, "data":[str(e)]})


#show items
def showItems(objs):
    allObjs = []
    for obj in objs:
        TaxCode = obj.TaxCode
        ItemsGroupCode = obj.ItemsGroupCode
        itemJson = ItemSerializer(obj)
        finalItems = json.loads(json.dumps(itemJson.data))

        # category details
        cateObj = Category.objects.get(Number = ItemsGroupCode.Number)
        finalItems['CategoryName'] = cateObj.GroupName
        #finalItems['IsService'] = cateObj.IsService

        # tax details
        taxObj = Tax.objects.get(Code = TaxCode)
        finalItems['TaxRate'] = taxObj.Rate

        allObjs.append(finalItems)
    return allObjs