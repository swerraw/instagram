from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from .models import Follow
from .serializers import FollowSerializer

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Показываем подписки, где текущий пользователь — подписчик
        return self.queryset.filter(follower=self.request.user)

    def perform_create(self, serializer):
        # При создании подписки указываем текущего пользователя как подписчика
        serializer.save(follower=self.request.user)

    @extend_schema(
        tags=["Подписки"],
        summary="Получить список подписок текущего пользователя"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        tags=["Подписки"],
        summary="Создать новую подписку"
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=["Подписки"],
        summary="Получить подписку по ID"
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=["Подписки"],
        summary="Полностью обновить подписку по ID"
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=["Подписки"],
        summary="Частично обновить подписку по ID"
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        request=None,
        responses={204: None},
        tags=["Подписки"],
        summary="Удалить подписку по ID"
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
