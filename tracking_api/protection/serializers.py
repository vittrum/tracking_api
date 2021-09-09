from rest_framework import serializers

from protection.models import Task
from users.models import Worker


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = []


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = 'status'


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'