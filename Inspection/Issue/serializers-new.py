from rest_framework import serializers
from .models import *
from Inspection.IssueCategory.models import IssueCategory


class IssueCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueCategory
        fields = ["id","Title"]

class IssueSerializer(serializers.ModelSerializer):
    IssueCategory = IssueCategorySerializer()
    class Meta:
        model = Issue
        fields = "__all__"
