from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect

from ..models import Post





@require_POST
@login_required
def post_delete(request, pk):
    # if request.method != 'POST':
    #     return HttpResponseNotAllowed()
    # if not request.user.is_authenticated:
    #     return redirect('members:login')
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        raise PermissionDenied('지울 권한이 없습니다')
    post.delete()
    return redirect('posts:post-list')
