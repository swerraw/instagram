from rest_framework.routers import DefaultRouter
from .views import PostViewSet
from django.urls import path
from . import views

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
path('create/', views.create_post, name='create_post'),

urlpatterns = router.urls