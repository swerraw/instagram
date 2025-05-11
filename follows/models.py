from django.conf import settings
from django.db import models

class Follow(models.Model):
    follower = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='following',
        on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='followers',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Используем UniqueConstraint для явного указания уникальности
        constraints = [
            models.UniqueConstraint(fields=['follower', 'following'], name='unique_follow')
        ]

    def __str__(self):
        return f"{self.follower} → {self.following}"

    # Проверка, подписан ли пользователь на другого
    @classmethod
    def is_following(cls, follower, following):
        return cls.objects.filter(follower=follower, following=following).exists()

