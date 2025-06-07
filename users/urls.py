from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, UserProfileView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #  Новый путь для получения данных профиля по имени
    path('users/<str:name>/', UserProfileView.as_view(), name='user-profile'),
]
