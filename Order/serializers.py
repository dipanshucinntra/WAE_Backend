from rest_framework import serializers
from .models import *

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        #fields = ['ename',"econtact"]
        #exclude = ['id']
        fields = "__all__"

class AddressExtensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressExtension
        #fields = ['ename',"econtact"]
        #exclude = ['id']
        fields = "__all__"
        
class DocumentLinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentLines
        #fields = ['ename',"econtact"]
        #exclude = ['id']
        fields = "__all__"

class AddOnDocumentLinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddOnDocumentLines
        #fields = ['ename',"econtact"]
        #exclude = ['id']
        fields = "__all__"

class AddendumSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddendumRequest
        fields = "__all__"

class TapTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TapType
        fields = "__all__"

class MachineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineType
        fields = "__all__"


################################################# Order History #####################################

class OrderHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderHistory
        fields = "__all__"

class DocumentLinesHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentLinesHistory
        fields = "__all__"

class AddOnDocumentLinesHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddOnDocumentLinesHistory
        fields = "__all__"

class OrderStatusRemarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatusRemarks
        #fields = ['ename',"econtact"]
        #exclude = ['id']
        fields = "__all__"


class AMCSalesOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMCSalesOrder
        fields = "__all__"

class AMCOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMCOrderItem
        fields = "__all__"

# >>>>>>>>>>>>>>>>>> Service Contracts  >>>>>>>>>>>>>>>>>>>
class ServiceContractsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceContracts
        fields = "__all__"
        
class ServiceContractsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceContractsItem
        fields = "__all__"

class OrderStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStage
        fields = "__all__"

