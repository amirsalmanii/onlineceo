# Generated by Django 3.2 on 2022-04-10 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_operator',
            field=models.BooleanField(default=False),
        ),
    ]
