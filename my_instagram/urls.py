from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    # API маршруты
    path('api/auth/', include('users.urls')),
    path('api/follows/', include('follows.urls')),
    path('api/likes/', include('likes.urls')),
    path('api/comments/', include('comments.urls')),
    path('api/posts/', include('posts.urls')),
    path('api/stories/', include('stories.urls')),

    # JWT токены
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger/OpenAPI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Страницы сайта (шаблоны)
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('register/', TemplateView.as_view(template_name='register.html'), name='register'),
    path('profile/<str:username>/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('search/', TemplateView.as_view(template_name='search.html'), name='search'),
    path('posts/', include('posts.urls')),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
