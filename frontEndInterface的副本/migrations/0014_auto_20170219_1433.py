# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('frontEndInterface', '0013_auto_20170219_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='star',
            name='text',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='academy',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 14, 33, 58, 499490)),
        ),
        migrations.AlterField(
            model_name='apply',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 14, 33, 58, 496467)),
        ),
        migrations.AlterField(
            model_name='information',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 14, 33, 58, 495256)),
        ),
        migrations.AlterField(
            model_name='rights',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 14, 33, 58, 499988)),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 14, 33, 58, 494513)),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 14, 33, 58, 497017)),
        ),
        migrations.AlterField(
            model_name='thoughts',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 14, 33, 58, 500455)),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 14, 33, 58, 498972)),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 14, 33, 58, 498458)),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 14, 33, 58, 493382)),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 14, 33, 58, 492683)),
        ),
    ]
