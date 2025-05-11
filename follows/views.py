from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .models import Follows

class UnfollowView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            to_unfollow = get_user_model().objects.get(id=user_id)
            follow_instance = Follows.objects.get(follower=request.user, following=to_unfollow)
            follow_instance.delete()
            return Response({"detail": f"Вы отписались от {to_unfollow.email}"}, status=200)
        except get_user_model().DoesNotExist:
            return Response({"detail": "Пользователь не найден."}, status=404)
        except Follows.DoesNotExist:
            return Response({"detail": "Вы не подписаны на этого пользователя."}, status=400)
