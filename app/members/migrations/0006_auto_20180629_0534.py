# Generated by Django 2.0.6 on 2018-06-29 05:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20180629_0226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='relations',
        ),
        migrations.AddField(
            model_name='user',
            name='to_relations_users',
            field=models.ManyToManyField(blank=True, related_name='from_relation_users', related_query_name='from_relation_user', through='members.Relation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='relation',
            name='relation_type',
            field=models.CharField(choices=[('f', 'Follow'), ('b', 'BLOCK')], max_length=1),
        ),
    ]
