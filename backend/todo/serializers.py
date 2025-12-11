from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "created_at",
            "completed",
        ]


class TaskToggleCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id"]
        read_only_fields = ["title", "description", "created", "completed"]
