from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Follow
from .serializers import FollowSerializer

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]  # чтобы только залогиненные могли подписываться

    def perform_create(self, serializer):
        # сохраняем подписку, указывая, кто подписывается — текущий пользователь
        serializer.save(follower=self.request.user)
