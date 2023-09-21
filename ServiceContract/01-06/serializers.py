from rest_framework import serializers
from .models import ServiceContract

class ServiceContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceContract
        fields = "__all__"
        