from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import timedelta


class Story(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='stories'
    )
    image = models.ImageField(upload_to='stories/images/', blank=True, null=True)
    video = models.FileField(upload_to='stories/videos/', blank=True, null=True)
    caption = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(hours=24)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Story by {self.user.name} at {self.created_at}"
