from django.contrib import admin
from .models import Article, Comment

# Register your models here.

admin.site.register(Article)       # 모델 등록 하는 방법
admin.site.register(Comment)

