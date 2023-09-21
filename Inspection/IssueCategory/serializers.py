from rest_framework import serializers
from .models import *
class IssueCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueCategory
        fields = "__all__"
