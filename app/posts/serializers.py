from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post
User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'pk',
            'author',
            'photo',
            'content',
            'created_at',
            'tags',
            'like_users',
        )
