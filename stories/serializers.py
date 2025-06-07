from rest_framework import serializers
from .models import Story

class StorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name', read_only=True)
    avatar = serializers.CharField(source='user.avatar', read_only=True)  # если в user есть avatar

    class Meta:
        model = Story
        fields = [
            'id', 'user', 'name', 'avatar',
            'image', 'created_at', 'expires_at', 'is_active'
        ]
        read_only_fields = ['user', 'created_at', 'expires_at', 'is_active']
