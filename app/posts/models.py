import re

from django.conf import settings
from django.db import models

from members.forms import User


class Post(models.Model):
    PATTERN_HASHTAG = re.compile(r'#(\w+)')

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='post', blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('HashTag', blank=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,

        related_name='like_posts',
    )

    class Meta:
        ordering = ['-pk']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for tag_name in re.findall(self.PATTERN_HASHTAG, self.content):
            tag, tag_created = HashTag.objects.get_or_create(name=tag_name)
            self.tags.add(tag)


    @property
    def content_html(self):
        return re.sub(
            r'#(?P<tag>#\w+)',
            '<a href="/posts/tags/\g<tag>">#\g<tag></a>',
            self.content,
        )


class HashTag(models.Model):
    name = models.CharField(max_length=20)


    def __str__(self):
        return f'HashTag (self.name)'


# admin에 등록
# superuser생성
# 로그인 해서 Post하나 추가해보기

#
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text
