from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'image', 'caption', 'created_at']
        read_only_fields = ['id', 'author', 'created_at']