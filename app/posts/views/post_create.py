from django.shortcuts import redirect, render

from ..models import Post
from ..forms import PostModelForm, PostForm


__all__ =(
    'post_create',
    'post_create_with_form',

)


def post_create(request):
    # PostModelForm을 사용
    #  form = PostModelForm(request.POST, request.FILES)
    #  post = form.save(commit=False)
    #  post.author = request.user
    #  post.save()
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:post-detail', pk=post.pk)
    else:
        form = PostModelForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/post_create.html', context)


@login_required
def post_create_with_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(author=request.user)
            return redirect('posts:post-detail', pk=post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/post_create.html', context)


def post_create_without_form(request):
    if request.method == 'POST':
        post = Post(
            author=request.user,
            photo=request.FILES['photo'],
            content=request.POST['content'],
        )
        post.save()
        return redirect('posts:post-detail', pk=post.pk)
    return render(request, 'posts/post_create.html')


