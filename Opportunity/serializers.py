from rest_framework import serializers
from .models import *

class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = "__all__"
        #exclude = ['id']
        #depth = 1
        
class OppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = ['id', 'OpportunityName', 'U_LEADID']
        
class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = "__all__"
        #exclude = ['id']
        #depth = 1
class StaticStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaticStage
        fields = "__all__"
        #exclude = ['id']
        #depth = 1

class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        fields = "__all__"
        #exclude = ['id']
        #depth = 1

class OppItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OppItem
        fields = "__all__"


################## CODE ADDED BY DIPANSHU FROM STANDALONE SUPPORT ###################
class PreSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreSite
        fields = "__all__"

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = "__all__"

class RFQSerializer(serializers.ModelSerializer):
    class Meta:
        model = RFQ
        fields = "__all__"

class InitiationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Initiation
        fields = "__all__"        