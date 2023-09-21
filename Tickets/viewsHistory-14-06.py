import json
import pytz
from rest_framework.decorators import api_view  
from rest_framework.response import Response
from rest_framework import status

from Tickets.models import History, RescueHistory
from Tickets.serializers import HistorySerializer, RescueHistorySerializer

# importing datetime
from datetime import datetime

# importing timezone from pytz module
from pytz import timezone

# Create your views here.
@api_view(['POST'])
def createHistory(request):
    try:
        History(
            TicketId_id = request.data['TicketId'],
            Type = request.data['Type'], #Ticket create, update or change status
            Remarks = request.data['Remarks'], # work what have done
        ).save()
            
        historyObj = History.objects.latest('id')

        return Response({"message":"Successfull","status":200 ,"data":[{'TicketHistoryId': historyObj.id}]})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})


@api_view(['POST'])
def allHistory(request):
    try:
        # TicketId = request.data['TicketId']
        PageNo = request.data['PageNo']
        MaxItem = 50
        endWith = (PageNo * MaxItem)
        startWith = (endWith - MaxItem)

        historyObj = History.objects.all().order_by('-id')[startWith:endWith]
        # historyJson = HistorySerializer(historyObj, many=True)
        result = showHistory(historyObj)
        return Response({"message":"Successfull","status":200 ,"data":result})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

@api_view(['POST'])
def filter_all_history(request):
    try:
        TicketId = request.data['TicketId']
        PageNo = request.data['PageNo']
        MaxItem = 50
        endWith = (PageNo * MaxItem)
        startWith = (endWith - MaxItem)

        ticketsObj = History.objects.filter(TicketId = TicketId)[startWith:endWith]
        # ticketsJson = HistorySerializer(ticketsObj, many=True)
        result = showHistory(ticketsObj)
        return Response({"message":"Successfull","status":200 ,"data":result})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

@api_view(['POST'])
def filter_all_history_type(request):
    try:
        TicketId = request.data['TicketId']
        ticketsObj = History.objects.filter(TicketId = TicketId, PrevType__gt=0)
        ticketsJson = HistorySerializer(ticketsObj, many=True)
        #result = showHistory(ticketsObj)
        return Response({"message":"Successfull","status":200 ,"data":ticketsJson.data})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

@api_view(['POST'])
def oneHistory(request):
    try:
        TicketId = request.data['TicketId']
        if History.objects.filter(TicketId_id = TicketId).exists():
            ticketsObj = History.objects.filter(TicketId_id = TicketId)
            ticketsJson = HistorySerializer(ticketsObj, many=True)
            return Response({"message":"Successfull","status":200 ,"data":ticketsJson.data})
        else:
            return Response({"message":"Error","status":201 ,"data":['id invalid']})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})


@api_view(['POST'])
def updateHistory(request):
    try:
        historyId = request.data['id']
        if History.objects.filter(pk = historyId).exists():
            fetchObj = History.objects.get(pk = historyId)
            fetchJson = HistorySerializer(fetchObj, data = request.data)
            if fetchJson.is_valid():
                fetchJson.save()
                return Response({"status":"200","message":"successfully","data":[fetchJson.data]})
            return Response(fetchJson.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"Error","status":201 ,"data":['Ticket history invalid']})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})


def showHistory(objs):
    allData = []
    for obj in objs:
        historyDatetime = obj.Datetime
        # print(historyDatetime)
        historyobj = HistorySerializer(obj)
        finalHistory = json.loads(json.dumps(historyobj.data))

        # Converting to Asia/Kolkata time zone
        istTime = historyDatetime.astimezone(timezone('Asia/Kolkata'))
        istTime = istTime.strftime("%d/%m/%Y %I:%M:%S %p")
        finalHistory['Datetime'] = istTime
        allData.append(finalHistory)
    return allData

# Create createRescue API
@api_view(['POST'])
def createRescue(request):
    try:
        RescueHistory(
            TicketId_id = request.data['TicketId'],
            Status = request.data['Status'], # On the way, Reached, Work in Progress, Rescue
            Remarks = request.data['Remarks'], # work what have done
        ).save()
            
        historyObj = RescueHistory.objects.latest('id')

        return Response({"message":"Successfull","status":200 ,"data":[{'TicketHistoryId': historyObj.id}]})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

# filter rescue history by ticket
@api_view(['POST'])
def allRescue(request):
    try:
        TicketId = request.data['TicketId']
        ticketsObj = RescueHistory.objects.filter(TicketId = TicketId)
        ticketsJson = RescueHistorySerializer(ticketsObj, many=True)
        return Response({"message":"Successfull","status":200 ,"data":ticketsJson.data})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

