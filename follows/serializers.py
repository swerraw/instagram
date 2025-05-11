from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Follow

# Сериализатор для пользователя
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'avatar', 'bio']

# Сериализатор для Follow (Подписка)
class FollowSerializer(serializers.ModelSerializer):
    # Заменяем вложенные сериализаторы на представление только ID пользователя для улучшения производительности
    follower = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    following = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())

    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following', 'created_at']

    # Дополнительный метод, если вы хотите вернуть информацию о пользователе (например, в виде словаря)
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['follower'] = UserSerializer(instance.follower).data
        representation['following'] = UserSerializer(instance.following).data
        return representation
