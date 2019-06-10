from django.db import models

# Create your models here.
# 모델 정의
class Article(models.Model):
    title = models.CharField(max_length=100)   # 제한두고 작성, title 100자 이하로 제한
    content = models.TextField()