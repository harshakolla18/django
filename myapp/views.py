from django.shortcuts import render, get_object_or_404
from .models import Post

def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'all_posts.html', {'posts': posts})

def single_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'single_post.html', {'post': post})
