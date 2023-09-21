from rest_framework import serializers
from .models import *

# ################################################## 
# ################ Tickets ######################### 
# ################################################## 
class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = "__all__"
        read_only_fields = ('CreatedBy', 'CreateDate')
        # depth=1

# ################################################## 
# ################ History ######################### 
# ################################################## 
class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"
        # depth=1

# ################################################## 
# ################ Rescue History ######################### 
# ################################################## 
class RescueHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RescueHistory
        fields = "__all__"
        # depth=1

# ################################################## 
# ################ Conversation ####################
# ################################################## 
class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = "__all__"
        # depth=1

# ################################################## 
# ############## Parts Requests ####################
# ################################################## 
# class PartsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Parts
#         fields = "__all__"
#         # depth=1

class PartRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartRequest
        fields = "__all__"
        # depth=1

class PRItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PRItems
        fields = "__all__"
        # depth=1

class PRAttachmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PRAttachments
        fields = "__all__"
        # depth=1

class PRStatusRemarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = PRStatusRemarks
        fields = "__all__"
        # depth=1


# ################################################## 
# ############# Service Checklist ##################
# ################################################## 
class ServiceCheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCheckList
        fields = "__all__"
        # depth=1


# ################################################## 
# ################# Dropdown #######################
# ################################################## 
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"
        # depth=1

class SubTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubType
        fields = "__all__"
        # depth=1

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"
        # depth=1

class TicketStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketStatus
        fields = "__all__"
        # depth=1

class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = "__all__"
        # depth=1

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = "__all__"
        # depth=1
class TicketChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketChecklist
        fields = "__all__"
        # depth=1        
        