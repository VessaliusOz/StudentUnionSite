# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('frontEndInterface', '0031_auto_20170222_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='chef',
            name='e_mail',
            field=models.CharField(default=b'Email', max_length=30, verbose_name=b'Email', blank=True),
        ),
        migrations.AddField(
            model_name='chef',
            name='telephone',
            field=models.CharField(default=b'\xe7\x94\xb5\xe8\xaf\x9d\xe5\x8f\xb7\xe7\xa0\x81', max_length=30, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d\xe5\x8f\xb7\xe7\xa0\x81', blank=True),
        ),
        migrations.AddField(
            model_name='information',
            name='file',
            field=models.FileField(default=None, upload_to=b'information/files', null=True, verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6', blank=True),
        ),
        migrations.AddField(
            model_name='s_news',
            name='file',
            field=models.FileField(default=None, upload_to=b'snews/files', null=True, verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6', blank=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='e_mail',
            field=models.CharField(default=b'Email', max_length=30, verbose_name=b'Email', blank=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='telephone',
            field=models.CharField(default=b'\xe7\x94\xb5\xe8\xaf\x9d\xe5\x8f\xb7\xe7\xa0\x81', max_length=30, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d\xe5\x8f\xb7\xe7\xa0\x81', blank=True),
        ),
        migrations.AddField(
            model_name='x_activity',
            name='file',
            field=models.FileField(default=None, upload_to=b'xnews/files', null=True, verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6', blank=True),
        ),
        migrations.AlterField(
            model_name='academy',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 33, 28, 838042), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 33, 28, 834239), verbose_name=b'\xe7\x94\xb3\xe8\xaf\xb7\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='school',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name=b'\xe5\xad\xa6\xe9\x99\xa2', blank=True),
        ),
        migrations.AlterField(
            model_name='chef',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 33, 28, 828860), verbose_name=b'\xe4\xb8\x8a\xe4\xbb\xbb\xe6\x97\xb6\xe9\x97\xb4(\xe6\x8e\x92\xe5\xba\x8f\xe7\x94\xa8)'),
        ),
        migrations.AlterField(
            model_name='fixserver',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 33, 28, 834792), verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='information',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 33, 28, 832223), verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 33, 28, 832893), verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='rights',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 33, 28, 838504), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 33, 28, 831598), verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 33, 28, 835305), verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='thoughts',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 33, 28, 838956), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 33, 28, 837527), verbose_name=b'\xe4\xb8\x8a\xe4\xbc\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 33, 28, 836909), verbose_name=b'\xe4\xb8\x8a\xe4\xbc\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 33, 28, 830284), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='video',
            field=models.CharField(default=b'\xe8\xa7\x86\xe9\xa2\x91\xe9\x93\xbe\xe6\x8e\xa5', max_length=200, verbose_name=b'\xe8\xa7\x86\xe9\xa2\x91\xe9\x93\xbe\xe6\x8e\xa5', blank=True),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 33, 28, 829577), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
