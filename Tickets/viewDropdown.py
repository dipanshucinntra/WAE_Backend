from rest_framework.decorators import api_view  
from rest_framework.response import Response
from rest_framework import status

from Tickets.models import *
from Tickets.serializers import *


@api_view(['GET'])
def allType(request):
    try:
        TypeObj = Type.objects.all().order_by('id')
        TypeJson = TypeSerializer(TypeObj, many=True)
        return Response({"message":"Successfull","status":200 ,"data":TypeJson.data})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

@api_view(['POST'])
def allSubType(request):
    try:
        SubTypeObj = SubType.objects.filter(Type=request.data['Type']).order_by('id')
        
        if len(SubTypeObj) == 0:
            SubTypeObj = SubType.objects.filter(Type="").order_by('id')
            
        SubTypeJson = SubTypeSerializer(SubTypeObj, many=True)
        return Response({"message":"Successfull","status":200 ,"data":SubTypeJson.data})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

		
@api_view(['GET'])
def allStatus(request):
    try:
        StatusObj = Status.objects.all().order_by('-id')
        StatusJson = StatusSerializer(StatusObj, many=True)
        return Response({"message":"Successfull","status":200 ,"data":StatusJson.data})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

@api_view(['GET'])
def allTicketStatus(request):
    try:
        TicketStatusObj = TicketStatus.objects.all().order_by('-id')
        TicketStatusJson = TicketStatusSerializer(TicketStatusObj, many=True)
        return Response({"message":"Successfull","status":200 ,"data":TicketStatusJson.data})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

@api_view(['GET'])
def allPriority(request):
    try:
        PriorityObj = Priority.objects.all().order_by('-id')
        PriorityJson = PrioritySerializer(PriorityObj, many=True)
        return Response({"message":"Successfull","status":200 ,"data":PriorityJson.data})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

@api_view(['GET'])
def allZone(request):
    try:
        ZoneObj = Zone.objects.all().order_by('-id')
        ZoneJson = ZoneSerializer(ZoneObj, many=True)
        return Response({"message":"Successfull","status":200 ,"data":ZoneJson.data})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})
