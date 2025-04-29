from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Like, Post, Comment
from .serializers import LikeSerializer


class LikePostAPIView(APIView):
    def post(self, request, *args, **kwargs):
        post_id = request.data.get('post')
        comment_id = request.data.get('comment')

        # Лайк к посту
        if post_id:
            post = Post.objects.get(id=post_id)
            like, created = Like.objects.get_or_create(user=request.user, post=post)

        # Лайк к комментарию
        elif comment_id:
            comment = Comment.objects.get(id=comment_id)
            like, created = Like.objects.get_or_create(user=request.user, comment=comment)

        else:
            return Response({"error": "Необходимо указать post или comment"}, status=status.HTTP_400_BAD_REQUEST)

        # Если лайк уже существует
        if not created:
            return Response({"message": "Вы уже лайкнули этот пост/комментарий."}, status=status.HTTP_400_BAD_REQUEST)

        return Response(LikeSerializer(like).data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        post_id = request.data.get('post')
        comment_id = request.data.get('comment')

        if post_id:
            like = Like.objects.filter(user=request.user, post_id=post_id).first()
        elif comment_id:
            like = Like.objects.filter(user=request.user, comment_id=comment_id).first()
        else:
            return Response({"error": "Необходимо указать post или comment"}, status=status.HTTP_400_BAD_REQUEST)

        if like:
            like.delete()
            return Response({"message": "Лайк удалён."}, status=status.HTTP_204_NO_CONTENT)

        return Response({"error": "Лайк не найден."}, status=status.HTTP_404_NOT_FOUND)