# Generated by Django 3.1.1 on 2020-09-13 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_post_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_excerpt',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
