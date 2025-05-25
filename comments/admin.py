from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'body', 'date']
    list_filter = ['date']
    search_fields = ['body', 'user__username']
