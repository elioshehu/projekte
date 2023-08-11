# Generated by Django 4.0.3 on 2022-05-03 09:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('theblog', '0004_category_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lieks',
            field=models.ManyToManyField(related_name='blog_post', to=settings.AUTH_USER_MODEL),
        ),
    ]