# Generated by Django 3.2 on 2022-04-24 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='title_video',
            field=models.FileField(blank=True, null=True, upload_to='news/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title_image',
            field=models.ImageField(blank=True, null=True, upload_to='news/'),
        ),
    ]
