
from api.models import Task
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class TaskSerializer(ModelSerializer):
    class Meta:
        model= Task
        fields ="__all__"
