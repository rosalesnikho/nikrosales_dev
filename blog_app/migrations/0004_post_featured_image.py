# Generated by Django 3.1.1 on 2020-09-12 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
