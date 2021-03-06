from rest_framework import serializers
from .models import Task, Project

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('title', 'description')


class TaskSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(required=False)
    class Meta:
        model = Task
        fields = ('project','title', 'description', 'due_date')

    def create(self, validated_data):
        print('fuck')
        if 'project' in validated_data:
            project = validated_data.pop('project')
            projectObj = Project.objects.create(**project)
            
            task = Task.objects.create(project=projectObj,**validated_data)
        task.save() 
        return task