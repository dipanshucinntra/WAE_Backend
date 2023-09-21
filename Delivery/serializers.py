from rest_framework import serializers
from .models import *

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
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
                
        
class DeliveryAttachmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAttachments
        #fields = ['ename',"econtact"]
        #exclude = ['id']
        fields = "__all__"
                