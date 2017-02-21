# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('frontEndInterface', '0021_auto_20170219_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2017, 2, 19, 20, 44, 54, 236909))),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(default=None, upload_to=b'static/xxsh/information')),
                ('body', models.TextField()),
                ('exc_editor', models.CharField(default=b'\xe6\x9c\xac\xe5\x85\xac\xe5\x91\x8a\xe6\x89\xa7\xe8\xa1\x8c\xe7\xbc\x96\xe8\xbe\x91', max_length=20)),
                ('duty_editor', models.CharField(default=b'\xe6\x9c\xac\xe5\x85\xac\xe5\x91\x8a\xe8\xb4\xa3\xe4\xbb\xbb\xe7\xbc\x96\xe8\xbe\x91', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='academy',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 20, 44, 54, 241442)),
        ),
        migrations.AlterField(
            model_name='apply',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 20, 44, 54, 238200)),
        ),
        migrations.AlterField(
            model_name='information',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 20, 44, 54, 236314)),
        ),
        migrations.AlterField(
            model_name='rights',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 20, 44, 54, 241908)),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 20, 44, 54, 235707)),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 20, 44, 54, 238741)),
        ),
        migrations.AlterField(
            model_name='someelse',
            name='organization_framework_text',
            field=DjangoUeditor.models.UEditorField(verbose_name='\u6821\u5b66\u751f\u4f1a\u7ec4\u7ec7\u67b6\u6784 ', blank=True),
        ),
        migrations.AlterField(
            model_name='someelse',
            name='school_system_brief_text',
            field=DjangoUeditor.models.UEditorField(verbose_name='\u9662\u4f1a\u4f53\u7cfb\u7b80\u4ecb', blank=True),
        ),
        migrations.AlterField(
            model_name='thoughts',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 20, 44, 54, 242365)),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 20, 44, 54, 240918)),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 20, 44, 54, 240288)),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 20, 44, 54, 234585)),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 20, 44, 54, 233753)),
        ),
    ]
