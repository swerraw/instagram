# posts/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post
from comments.models import Comment


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)

    return render(request, 'post_detail.html', {'post': post, 'comments': comments})
