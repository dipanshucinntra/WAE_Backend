from rest_framework import serializers
from .models import *

class DraftOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DraftOrder
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
