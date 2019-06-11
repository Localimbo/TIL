from django.db import models
from django.conf import settings
# settings.AUTH_USER_MODEL  :  장고에서 만들어놓은 user model이다.

# Create your models here.
# 모델 정의
class Article(models.Model):
    title = models.CharField(max_length=100)   # 제한두고 작성, title 100자 이하로 제한
    content = models.TextField()
    # user에 대한 정보 추가
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)