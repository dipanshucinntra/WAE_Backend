from rest_framework.decorators import api_view  
from rest_framework.response import Response
from rest_framework import status

from Tickets.models import ServiceCheckList
from Tickets.serializers import ServiceCheckListSerializer

# Create your views here.
@api_view(['POST'])
def createServiceCheckList(request):
    try:
        ServiceCheckList(
            TicketId_id = request.data['TicketId'],
            TaskName = request.data['TaskName'],
            Comment = request.data['Comment'],
            Status = request.data['Status'],
            Duration = request.data['Duration'],
        ).save()
            
        ServiceCheckListObj = ServiceCheckList.objects.latest('id')

        return Response({"message":"Successfull","status":200 ,"data":[{'TicketServiceCheckListId': ServiceCheckListObj.id}]})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})


@api_view(['Get'])
def allServiceCheckList(request):
    try:
        ServiceCheckListObj = ServiceCheckList.objects.all().order_by('-id')
        ServiceCheckListJson = ServiceCheckListSerializer(ServiceCheckListObj, many=True)
        return Response({"message":"Successfull","status":200 ,"data":ServiceCheckListJson.data})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

@api_view(['POST'])
def filter_all_ServiceCheckList(request):
    try:
        TicketId = request.data['TicketId']
        ticketsObj = ServiceCheckList.objects.filter(TicketId = TicketId)
        ticketsJson = ServiceCheckListSerializer(ticketsObj, many=True)
        return Response({"message":"Successfull","status":200 ,"data":ticketsJson.data})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

@api_view(['POST'])
def oneServiceCheckList(request):
    try:
        TicketId = request.data['TicketId']
        if ServiceCheckList.objects.filter(TicketId_id = TicketId).exists():
            ticketsObj = ServiceCheckList.objects.filter(TicketId_id = TicketId)
            ticketsJson = ServiceCheckListSerializer(ticketsObj, many=True)
            return Response({"message":"Successfull","status":200 ,"data":ticketsJson.data})
        else:
            return Response({"message":"Error","status":201 ,"data":['id invalid']})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})


@api_view(['POST'])
def updateServiceCheckList(request):
    try:
        ServiceCheckListId = request.data['id']
        if ServiceCheckList.objects.filter(pk = ServiceCheckListId).exists():
            fetchObj = ServiceCheckList.objects.get(pk = ServiceCheckListId)
            fetchJson = ServiceCheckListSerializer(fetchObj, data = request.data)
            if fetchJson.is_valid():
                fetchJson.save()
                return Response({"status":"200","message":"successfully","data":[fetchJson.data]})
            return Response(fetchJson.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"Error","status":201 ,"data":['Ticket ServiceCheckList invalid']})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})
