from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Like
from posts.models import Post
from comments.models import Comment
from .serializers import LikeSerializer

class LikePostAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post_id = request.data.get('post')
        comment_id = request.data.get('comment')

        if post_id and comment_id:
            return Response({"error": "Можно лайкать либо пост, либо комментарий, но не оба одновременно."},
                            status=status.HTTP_400_BAD_REQUEST)

        if not post_id and not comment_id:
            return Response({"error": "Необходимо указать post или comment"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            if post_id:
                post = Post.objects.get(id=post_id)
                like, created = Like.objects.get_or_create(user=request.user, post=post)
            else:
                comment = Comment.objects.get(id=comment_id)
                like, created = Like.objects.get_or_create(user=request.user, comment=comment)
        except Post.DoesNotExist:
            return Response({"error": "Пост не найден"}, status=status.HTTP_404_NOT_FOUND)
        except Comment.DoesNotExist:
            return Response({"error": "Комментарий не найден"}, status=status.HTTP_404_NOT_FOUND)

        if not created:
            return Response({"message": "Вы уже лайкнули этот пост/комментарий."}, status=status.HTTP_400_BAD_REQUEST)

        return Response(LikeSerializer(like).data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        post_id = request.data.get('post')
        comment_id = request.data.get('comment')

        if post_id and comment_id:
            return Response({"error": "Можно удалять лайк либо с поста, либо с комментария, но не оба одновременно."},
                            status=status.HTTP_400_BAD_REQUEST)

        if not post_id and not comment_id:
            return Response({"error": "Необходимо указать post или comment"}, status=status.HTTP_400_BAD_REQUEST)

        if post_id:
            like = Like.objects.filter(user=request.user, post_id=post_id).first()
        else:
            like = Like.objects.filter(user=request.user, comment_id=comment_id).first()

        if like:
            like.delete()
            return Response({"message": "Лайк удалён."}, status=status.HTTP_204_NO_CONTENT)

        return Response({"error": "Лайк не найден."}, status=status.HTTP_404_NOT_FOUND)
