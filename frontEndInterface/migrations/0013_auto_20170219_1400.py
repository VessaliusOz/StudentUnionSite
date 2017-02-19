# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('frontEndInterface', '0012_auto_20170219_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='academy',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 14, 0, 59, 627514)),
        ),
        migrations.AddField(
            model_name='rights',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 14, 0, 59, 627987)),
        ),
        migrations.AddField(
            model_name='thoughts',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 14, 0, 59, 628450)),
        ),
        migrations.AlterField(
            model_name='apply',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 14, 0, 59, 624553)),
        ),
        migrations.AlterField(
            model_name='information',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 14, 0, 59, 623283)),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 14, 0, 59, 622552)),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 14, 0, 59, 625094)),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 14, 0, 59, 626993)),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 14, 0, 59, 626486)),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 14, 0, 59, 621444)),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 14, 0, 59, 620745)),
        ),
    ]
