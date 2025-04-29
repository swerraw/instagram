# comments/views.py
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Comment
from posts.models import Post

@csrf_exempt
def create_comment(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, id=post_id)  # Получаем пост по ID
        user = request.user  # Получаем текущего пользователя

        # Получаем текст комментария из POST-запроса
        body = request.POST.get('body')

        if body:
            # Создаем новый комментарий
            comment = Comment.objects.create(post=post, user=user, body=body)

            # Возвращаем успешный ответ
            return JsonResponse({"message": "Comment created successfully", "comment_id": comment.id}, status=201)

        return JsonResponse({"error": "Comment body is required"}, status=400)
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)
