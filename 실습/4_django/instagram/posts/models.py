from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings


class HashTag(models.Model):
    content = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.content


class Post(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts")    # user model과 연결, 중간모델을 거침
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    # image = models.ImageField(blank=True)    # blank여도 괜츈
    image = ProcessedImageField(
        upload_to='posts/images',             # 올리는 위치 tjfwjd설정
        processors=[ResizeToFill(600, 600)],  # 인스타 사이즈 ^^
        format='JPEG',
        options={'quality': 90})
    hashtags = models.ManyToManyField(HashTag, blank=True)


class Comment(models.Model):
    content = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


