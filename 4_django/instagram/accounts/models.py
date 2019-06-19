from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class User(AbstractUser):
    # 내가 팔로하고 있는 사람 = follow, 나를 팔로하고 있는 사람 보기 위해 related name 설정
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="follower")   # 아까 settings에 선언했었던 accounts의 모델 연결
    introduce = models.TextField(blank=True)
    image = ProcessedImageField(
        upload_to='accounts/images',             # feed에 올리는 사진, 프로필에 올리는 사진 구분
        processors=[ResizeToFill(150, 150)],  # 인스타 사이즈 ^^
        format='JPEG',
        options={'quality': 90},
        blank=True
    )
