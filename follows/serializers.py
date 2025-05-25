from rest_framework import serializers
from .models import Follow

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following']
        read_only_fields = ['follower']

    def validate(self, data):
        follower = self.context['request'].user
        following = data['following']
        if Follow.objects.filter(follower=follower, following=following).exists():
            raise serializers.ValidationError(
                f"Вы уже подписаны на пользователя {following.username}."
            )
        if follower == following:
            raise serializers.ValidationError("Вы не можете подписаться на самого себя.")
        return data
