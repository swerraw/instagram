from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import render


def create_post(request):
    return render(request, 'posts/create_post.html')

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Возвращаем только посты текущего пользователя
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        # При создании поста автоматически привязываем его к текущему пользователю
        serializer.save(user=self.request.user)

    @extend_schema(
        tags=["Посты"],
        summary="Получить список постов пользователя"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        tags=["Посты"],
        summary="Создать новый пост"
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=["Посты"],
        summary="Получить пост по ID"
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=["Посты"],
        summary="Полностью обновить пост по ID"
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=["Посты"],
        summary="Частично обновить пост по ID"
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        request=None,
        responses={204: None},
        tags=["Посты"],
        summary="Удалить пост по ID"
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
