from rest_framework import serializers
from .models import Like

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user', 'post', 'comment', 'created_at')

    def validate(self, data):
        post = data.get('post')
        comment = data.get('comment')

        if post and comment:
            raise serializers.ValidationError("Можно лайкать только пост или комментарий, но не оба одновременно.")
        if not post and not comment:
            raise serializers.ValidationError("Необходимо указать либо пост, либо комментарий для лайка.")
        return data
