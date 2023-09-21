from rest_framework import serializers
from .models import *

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
        # depth = 2

############### New Serializer by [DK]################
class ItemPendingSerializer(serializers.ModelSerializer):    
    ItemGroupName= serializers.SerializerMethodField('get_group_name')
    class Meta:
        model = Item
        fields = "__all__"
        extra_fields = ['ItemGroupName']
    def get_group_name(self, obj):
        return obj.ItemsGroupCode.GroupName     

class ItemOrderStatusRemarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemOrderStatusRemarks
        fields = "__all__"       
############### New Serializer by [DK]################

class ItSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["ItemCode","ItemName"]

class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = "__all__"

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

#########################  added   for item master########################

class ItemGroupMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemGroupMaster
        fields = "__all__"

