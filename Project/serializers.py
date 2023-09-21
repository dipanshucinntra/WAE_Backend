from rest_framework import serializers
from .models import Project, ProjectStaticstage, ProjectItem, MasterProject, ProjectStage

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        #fields = ['ename',"econtact"]
        #exclude = ['id']
        fields = "__all__"

class MasterProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterProject
        #fields = ['ename',"econtact"]
        #exclude = ['id']
        fields = "__all__"        

class ProjectStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStage
        #fields = ['ename',"econtact"]
        #exclude = ['id']
        fields = "__all__"
        read_only_fields = ('Name', 'ProjectId','Stageno','CreateDate','CreateTime')

class ProjectStaticstageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStaticstage
        #fields = ['ename',"econtact"]
        #exclude = ['id']
        fields = "__all__"

class ProjectItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectItem
        #fields = ['ename',"econtact"]
        #exclude = ['id']
        fields = "__all__"