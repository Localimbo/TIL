from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Post(models.Model):
    content = models.TextField()
    # image = models.ImageField(blank=True)
    image = ProcessedImageField(
        upload_to='posts/images',             # 올리는 위치 설정
        processors=[ResizeToFill(600, 600)],  # 인스타 사이즈 ^^
        format='JPEG',
        options={'quality': 90})




