from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model
from .models import Follow
from .serializers import FollowSerializer

class FollowView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        to_follow = get_user_model().objects.get(id=user_id)
        Follow.objects.get_or_create(follower=request.user, following=to_follow)
        return Response({"detail": f"Вы подписались на {to_follow.email}"}, status=201)

class UnfollowView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, user_id):
        Follow.objects.filter(follower=request.user, following__id=user_id).delete()
        return Response({"detail": "Вы отписались"}, status=204)

class FollowersListView(generics.ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = get_user_model().objects.get(id=self.kwargs['user_id'])
        return Follow.objects.filter(following=user)

class FollowingListView(generics.ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = get_user_model().objects.get(id=self.kwargs['user_id'])
        return Follow.objects.filter(follower=user)
