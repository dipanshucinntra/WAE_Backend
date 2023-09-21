from rest_framework.decorators import api_view  
from rest_framework.response import Response
from rest_framework import status

from Employee.models import Employee
from Tickets.models import Conversation
from Tickets.serializers import ConversationSerializer

# Create your views here.
@api_view(['POST'])
def createConversation(request):
    try:
        Conversation(
            TicketId_id = request.data['TicketId'],
            OwnerId = request.data['OwnerId'],
            OwnerType = request.data['OwnerType'],
            Message = request.data['Message'],
            Type = request.data['Type'],
        ).save()
            
        ConversationObj = Conversation.objects.latest('id')

        return Response({"message":"Successfull","status":200 ,"data":[{'TicketConversationId': ConversationObj.id}]})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})


@api_view(['POST'])
def allConversation(request):
    try:
        PageNo = request.data['PageNo']
        MaxItem = 50
        endWith = (PageNo * MaxItem)
        startWith = (endWith - MaxItem)
        # [startWith:endWith]

        ConversationObj = Conversation.objects.all().order_by('-id')[startWith:endWith]
        ConversationJson = ConversationSerializer(ConversationObj, many=True)
        return Response({"message":"Successfull","status":200 ,"data":ConversationJson.data})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

#{"TicketId":1, "PageNo":1}
@api_view(['POST'])
def filter_all_Conversation(request):
    try:
        TicketId = request.data['TicketId']
        PageNo = request.data['PageNo']
        MaxItem = 50
        endWith = (PageNo * MaxItem)
        startWith = (endWith - MaxItem)

        ticketsObj = Conversation.objects.filter(TicketId = TicketId)[startWith:endWith]
        ticketsJson = ConversationSerializer(ticketsObj, many=True)
        
        for Obj in ticketsJson.data:
            if Employee.objects.filter(SalesEmployeeCode=Obj['OwnerId']).exists():
                fname = Employee.objects.get(SalesEmployeeCode=Obj['OwnerId']).SalesEmployeeName
                Obj['OwnerName'] = fname
            else:
                Obj['OwnerName'] = ""
                
        return Response({"message":"Successfull","status":200 ,"data":ticketsJson.data})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})

@api_view(['POST'])
def oneConversation(request):
    try:
        TicketId = request.data['TicketId']
        if Conversation.objects.filter(TicketId_id = TicketId).exists():
            ticketsObj = Conversation.objects.filter(TicketId_id = TicketId)
            ticketsJson = ConversationSerializer(ticketsObj, many=True)
            return Response({"message":"Successfull","status":200 ,"data":ticketsJson.data})
        else:
            return Response({"message":"Error","status":201 ,"data":['id invalid']})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})


@api_view(['POST'])
def updateConversation(request):
    try:
        ConversationId = request.data['id']
        if Conversation.objects.filter(pk = ConversationId).exists():
            fetchObj = Conversation.objects.get(pk = ConversationId)
            fetchJson = ConversationSerializer(fetchObj, data = request.data)
            if fetchJson.is_valid():
                fetchJson.save()
                return Response({"status":"200","message":"successfully","data":[fetchJson.data]})
            return Response(fetchJson.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"Error","status":201 ,"data":['Ticket Conversation invalid']})
    except Exception as e:
        return Response({"message":str(e),"status":201 ,"data":[]})
