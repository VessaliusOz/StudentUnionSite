# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('frontEndInterface', '0016_auto_20170219_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academy',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 16, 51, 34, 928879)),
        ),
        migrations.AlterField(
            model_name='apply',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 16, 51, 34, 925842)),
        ),
        migrations.AlterField(
            model_name='department',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=b'static/xxsh/department'),
        ),
        migrations.AlterField(
            model_name='information',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 16, 51, 34, 924647)),
        ),
        migrations.AlterField(
            model_name='rights',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 16, 51, 34, 929354)),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 16, 51, 34, 924030)),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 16, 51, 34, 926387)),
        ),
        migrations.AlterField(
            model_name='thoughts',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 16, 51, 34, 929824)),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 16, 51, 34, 928356)),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 16, 51, 34, 927829)),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 16, 51, 34, 922773)),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 16, 51, 34, 922072)),
        ),
    ]
