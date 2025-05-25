from django.contrib import admin
from .models import Post  # Импорт модели

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'created_at')
    search_fields = ('author__username',)
    list_filter = ('created_at',)