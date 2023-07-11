from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format=None, read_only=True)
    updated_at = serializers.DateTimeField(format=None, read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'completed', 'image', 'created_at', 'updated_at')

    def to_representation(self, instance):
        format = self.context.get('format')
        if format:
            self.fields['created_at'].format = format
            self.fields['updated_at'].format = format
        return super().to_representation(instance)

