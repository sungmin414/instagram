# Generated by Django 2.0.6 on 2018-06-28 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20180628_0734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user_photo',
        ),
    ]
