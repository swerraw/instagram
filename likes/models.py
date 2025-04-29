from django.db import models
from django.contrib.auth import get_user_model
from posts.models import Post
from comments.models import Comment

User = get_user_model()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes', blank=True, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes', blank=True, null=True)

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
        if self.post:
            return f"{self.user.username} лайкнул пост {self.post.id}"
        elif self.comment:
            return f"{self.user.username} лайкнул комментарий {self.comment.id}"
        else:
            return f"{self.user.username} поставил лайк"
