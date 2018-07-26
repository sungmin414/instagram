# /api/posts/
#1. posts.serializers -> PostSerializer
#2. apis.__init__
# class PostList(APIView)
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from members.serializers import UserSerializer
from ..models import Post
from ..serializers import PostSerializer

__all__ = (
    'PostList',
    'UserList',
)
#
# class PostList(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#/posts/        <- posts.views.post_list
#/api/posts/    <- posts.apis.PostList.as_view()
#
# 1. posts.serializers에 PostSerializer구현
# 2. apis에 PostList GenericCbv구현
# 3. posts.urls를 분할
#     -> posts.urls.views
#     -> posts.urls.apis
# 4. config.urls에서 적절히 include처리
# 5. /api/posts/로 Postman Collection작성
# 6. 잘되나 확인

