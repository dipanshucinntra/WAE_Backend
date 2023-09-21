from rest_framework import serializers
from .models import *

class TenderQuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenderQuotation
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

