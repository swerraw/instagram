from rest_framework import serializers
from .models import Like

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user', 'post', 'comment', 'created_at')

    def validate(self, data):
        # Проверка, чтобы не лайкать одновременно пост и комментарий
        if data.get('post') and data.get('comment'):
            raise serializers.ValidationError("Можно лайкать только пост или комментарий, но не оба одновременно.")
        return data