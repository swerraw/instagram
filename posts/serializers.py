from rest_framework import serializers
from posts.models import Post
from comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user_name', 'body']

class PostSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='author.username', read_only=True)
    user_avatar = serializers.ImageField(source='author.avatar', read_only=True)
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    image = serializers.ImageField()

    class Meta:
        model = Post
        fields = [
            'id', 'user_name', 'user_avatar',
            'image', 'caption', 'created_at',
            'likes_count', 'comments'
        ]
