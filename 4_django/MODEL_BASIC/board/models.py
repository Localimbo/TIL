from django.db import models
# class 정의

# Model Template View
class Article(models.Model):
    # id = Primary Key
    title = models.CharField(max_length=200)        # 최대로 들어 갈 수 있는 길이 지정 필수!
    content = models.TextField()

    def __str__(self):
        return f'{self.id}: {self.title} - {self.content}'


