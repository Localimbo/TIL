# Generated by Django 2.1.8 on 2019-06-17 05:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0006_auto_20190617_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_users',
            field=models.ManyToManyField(related_name='like_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
