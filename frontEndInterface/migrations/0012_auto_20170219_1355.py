# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('frontEndInterface', '0011_auto_20170218_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='academy',
            name='text',
            field=models.TextField(default=b'\xe5\xad\xa6\xe6\x9c\xaf\xe9\x82\xa3\xe4\xb8\x80\xe6\xa0\x8f\xe8\xa6\x81\xe5\xa1\xab\xe5\x85\x85\xe7\x9a\x84\xe5\xad\x97\xe7\xac\xa6'),
        ),
        migrations.AddField(
            model_name='rights',
            name='text',
            field=models.TextField(default=b'\xe6\x9d\x83\xe7\x9b\x8a\xe9\x82\xa3\xe4\xb8\x80\xe6\xa0\x8f\xe8\xa6\x81\xe5\xa1\xab\xe5\x85\x85\xe7\x9a\x84\xe5\xad\x97\xe7\xac\xa6'),
        ),
        migrations.AddField(
            model_name='thoughts',
            name='text',
            field=models.TextField(default=b'\xe6\x80\x9d\xe6\xbd\xae\xe9\x82\xa3\xe4\xb8\x80\xe6\xa0\x8f\xe8\xa6\x81\xe5\xa1\xab\xe5\x85\x85\xe7\x9a\x84\xe5\xad\x97\xe7\xac\xa6'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 13, 55, 14, 529334)),
        ),
        migrations.AlterField(
            model_name='information',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 13, 55, 14, 528140)),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 13, 55, 14, 527459)),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 13, 55, 14, 529866)),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 13, 55, 14, 531763)),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 13, 55, 14, 531257)),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 13, 55, 14, 526199)),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 13, 55, 14, 525502)),
        ),
    ]
