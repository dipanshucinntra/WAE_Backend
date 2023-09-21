from rest_framework import serializers
from .models import *

class QuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotation
        #fields = ['ename',"econtact"]
        #exclude = ['id']
        fields = "__all__"
        #depth = 1

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


########## CODE ADDED BY DIPANSHU FROM STANDALONE SUPPORT ################
class QuotStatusRemarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotStatusRemarks
        fields = "__all__"

class QuotAttachmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotAttachments
        fields = "__all__"

                