from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Используем строковые ссылки вместо прямого импорта моделей
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='likes', blank=True, null=True)
    comment = models.ForeignKey('comments.Comment', on_delete=models.CASCADE, related_name='likes', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post', 'comment')
        constraints = [
            models.CheckConstraint(
                check=models.Q(post__isnull=False) | models.Q(comment__isnull=False),
                name="like_post_or_comment"
            )
        ]

    def __str__(self):
        user_name = getattr(self.user, 'name', str(self.user))
        if self.post:
            return f"{user_name} лайкнул пост {self.post.id}"
        elif self.comment:
            return f"{user_name} лайкнул комментарий {self.comment.id}"
        else:
            return f"{user_name} поставил лайк"
