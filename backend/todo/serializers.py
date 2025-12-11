from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()

    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "created_at",
            "completed",
        ]
