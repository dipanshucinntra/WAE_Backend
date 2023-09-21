from rest_framework import serializers
from .models import *
class InspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspection
        fields = "__all__"

