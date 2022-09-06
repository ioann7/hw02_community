from django.shortcuts import render, get_object_or_404
from django.conf import settings

from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.select_related(
        'author', 'group')[:settings.POSTS_PER_PAGE]
    context = {
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:settings.POSTS_PER_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
