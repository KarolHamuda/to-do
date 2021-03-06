from .models import Task
from rest_framework import serializers


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Task
        fields = ['task_id', 'title', 'description', 'priority', 'inserted_at']