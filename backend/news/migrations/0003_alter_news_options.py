# Generated by Django 3.2 on 2022-05-07 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20220424_1840'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-id']},
        ),
    ]
