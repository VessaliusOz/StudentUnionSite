# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('frontEndInterface', '0020_auto_20170219_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='someelse',
            name='organization_framework_image',
            field=models.ImageField(default=None, null=True, upload_to=b'static/xxsh/organizatin_framework', blank=True),
        ),
        migrations.AddField(
            model_name='someelse',
            name='organization_framework_text',
            field=DjangoUeditor.models.UEditorField(verbose_name='\u5185\u5bb9   ', blank=True),
        ),
        migrations.AlterField(
            model_name='academy',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 20, 25, 31, 245738)),
        ),
        migrations.AlterField(
            model_name='apply',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 20, 25, 31, 242470)),
        ),
        migrations.AlterField(
            model_name='information',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 20, 25, 31, 241128)),
        ),
        migrations.AlterField(
            model_name='rights',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 20, 25, 31, 246210)),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 20, 25, 31, 240501)),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 20, 25, 31, 243022)),
        ),
        migrations.AlterField(
            model_name='thoughts',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 20, 25, 31, 246684)),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 20, 25, 31, 245098)),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 20, 25, 31, 244591)),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 20, 25, 31, 239332)),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 20, 25, 31, 238442)),
        ),
    ]
