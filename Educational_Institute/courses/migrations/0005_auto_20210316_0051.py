# Generated by Django 3.1.6 on 2021-03-15 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(max_length=100),
        ),
    ]
