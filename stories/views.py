from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Story
from .serializers import StorySerializer

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Возвращаем только истории текущего пользователя
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        # При создании истории автоматически привязываем её к текущему пользователю
        serializer.save(user=self.request.user)
