from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    # 내가 팔로하고 있는 사람 = follow, 나를 팔로하고 있는 사람 보기 위해 related name 설정
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="follower")   # 아까 settings에 선언했었던 accounts의 모델 연결
