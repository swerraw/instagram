from django.urls import path
from .views import LikePostAPIView

urlpatterns = [
    path('like/', LikePostAPIView.as_view(), name='like_post'),
]