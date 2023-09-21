from django.shortcuts import render
from rest_framework.decorators import api_view    
from rest_framework import status
from rest_framework.response import Response

from ItemsPIR.models import CheckList
from ItemsPIR.serializers import CheckListSerializer

# Create your views here.
@api_view(['POST'])
def create(request):
    try:
        CategoryId = request.data['CategoryId']
        Type = request.data['Type']
        ListFor = request.data['ListFor']
        # LineNo = request.data['LineNo']
        Name = request.data['Name']

        if CheckList.objects.filter(CategoryId = CategoryId, Type = Type, ListFor = ListFor, Name = Name).exists():
            return Response({"message":"Check List name already eixsts", "status":"201", "data":[]})
        else:
            lineCont = CheckList.objects.filter(CategoryId = CategoryId, Type = Type, ListFor = ListFor).count()
            print('itemlineOcunt')
            print(lineCont)
            lineCont = int(lineCont)+1

            _CheckList = CheckList(CategoryId = CategoryId, Type = Type, ListFor = ListFor, LineNo = lineCont, Name = Name).save()
            _CheckListObj = CheckList.objects.latest('id')
            
            return Response({"message":"successful","status":"200","data":[{"CheckListId": _CheckListObj.id}]})

    except Exception as e:
        return Response({"message": str(e),"status":"201","data":[]})


@api_view(['GET'])
def all(request):
    try:
        checkListObj = CheckList.objects.all().order_by('-id')
        ticketsJson = CheckListSerializer(checkListObj, many=True)
        return Response({"message":"Successfull","status":200 ,"data":ticketsJson.data})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

@api_view(['POST'])
def all_filter(request):
    try:
        CategoryId = request.data['CategoryId']
        Type = request.data['Type']
        # ListFor = request.data['ListFor']
        checkListObj = CheckList.objects.filter(CategoryId = CategoryId, Type = Type, ListFor = 1)
        ticketsJson = CheckListSerializer(checkListObj, many=True)
        return Response({"message":"Successfull","status":200 ,"data":ticketsJson.data})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})


@api_view(['POST'])
def update(request):
    try:
        checkListId = request.data['id']
        if CheckList.objects.filter(pk = checkListId).exists():
            fetchObj = CheckList.objects.get(pk = checkListId)
            fetchJson = CheckListSerializer(fetchObj, data = request.data)
            if fetchJson.is_valid():
                fetchJson.save()
                return Response({"status":"200","message":"successfully","data":[fetchJson.data]})
            return Response(fetchJson.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"Error","status":201 ,"data":['Ticket history invalid']})
    except Exception as e:
        return Response({"message":"Error","status":201 ,"data":str(e)})
