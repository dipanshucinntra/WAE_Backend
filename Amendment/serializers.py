from rest_framework import serializers
from .models import *

class AmendmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amendment
        #fields = ['ename',"econtact"]
        #exclude = ['id']
        fields = "__all__"


class AmendmentOrderStatusRemarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmendmentOrderStatusRemarks
        fields = "__all__"