# Generated by Django 3.2 on 2022-05-11 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
