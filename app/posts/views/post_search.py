from django.shortcuts import render

from ..models import Post


def search_post_list(request, tag):
    posts = Post.objects.filter(tags__name__contains=tag).distinct()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/search_post_list.html', context)

