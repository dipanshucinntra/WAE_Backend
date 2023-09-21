from rest_framework import serializers
from .models import *

class CheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckList
        #fields = ['ename',"econtact"]
        #exclude = ['id']
        fields = "__all__"
        depth = 1
