from rest_framework import serializers
from .models import *

class ServiceContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceContract
        fields = "__all__"

class MasterServiceContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterServiceContract
        fields = "__all__"
                