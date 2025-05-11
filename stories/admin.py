from django.contrib import admin
from .models import Story

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'expires_at', 'is_active']
    search_fields = ['user__name']
