# Generated by Django 2.0.6 on 2018-06-29 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_post_user_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
    ]
