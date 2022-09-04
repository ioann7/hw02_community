from django.shortcuts import render, get_object_or_404

from .models import Post, Group
from yatube.settings import POSTS_PER_PAGE


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.select_related(
        'author'
    ).select_related(
        'group'
    )[:POSTS_PER_PAGE]
    context = {
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POSTS_PER_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
