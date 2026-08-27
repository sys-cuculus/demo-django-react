from .models import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'task_name',
            'description',
            'due_date',
            'assigned_to',
            'status',
            'started_at',
            'closed_at',
            'priority',
            'created_at',
            'updated_at',
        ]