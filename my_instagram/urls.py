from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Схема документации Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="My Instagram API",
      default_version='v1',
      description="API для работы с подписками и пользователями",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@myinstagram.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('api/follows/', include('follows.urls')),
    path('api/likes/', include('likes.urls')),
    path('api/comments/', include('comments.urls')),


    # Добавление URL для Swagger
    path('swagger/', schema_view.as_view()),  # Документация Swagger
]
