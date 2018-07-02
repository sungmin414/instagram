from django.shortcuts import render

from ..models import Comment

__all__ =(
    'comment',
)


def comment(request,pk):

    if request.method == 'POST':
        comment_post = Comment(
            post=request.post,
            post_user = request.user,
            text = request.text,
        )

        return (request, 'posts:commnet', comment_post)
    # context = {
    #     'comments':comments,
    # }
    return render(request, 'posts/post_detail.html')



