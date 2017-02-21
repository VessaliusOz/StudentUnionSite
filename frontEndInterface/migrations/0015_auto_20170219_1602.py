# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('frontEndInterface', '0014_auto_20170219_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='image',
            field=models.ImageField(default=None, upload_to=b'static/xxsh/department'),
        ),
        migrations.AlterField(
            model_name='academy',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 16, 2, 0, 44542)),
        ),
        migrations.AlterField(
            model_name='apply',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 16, 2, 0, 40876)),
        ),
        migrations.AlterField(
            model_name='information',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 16, 2, 0, 39522)),
        ),
        migrations.AlterField(
            model_name='rights',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 16, 2, 0, 45016)),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 16, 2, 0, 38913)),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 16, 2, 0, 41706)),
        ),
        migrations.AlterField(
            model_name='thoughts',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 16, 2, 0, 45477)),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 16, 2, 0, 44020)),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 16, 2, 0, 43461)),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 16, 2, 0, 37660)),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 16, 2, 0, 36943)),
        ),
    ]
