from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from .models import CustomUser, UserSettings

@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ['name', 'email', 'is_staff', 'is_superuser', 'avatar_preview']
    search_fields = ['name', 'email']
    ordering = ['name']

    fieldsets = (
        (None, {'fields': ('name', 'email', 'password')}),
        ('Personal info', {'fields': ('phone', 'avatar', 'bio', 'links')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

    def get_fieldsets(self, request, obj=None):
        return self.add_fieldsets if not obj else self.fieldsets

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" width="40" height="40" style="border-radius: 50%;" />', obj.avatar.url)
        return "—"
    avatar_preview.short_description = 'Avatar'


@admin.register(UserSettings)
class UserSettingsAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_private', 'allow_comments']
    search_fields = ['user__name']
