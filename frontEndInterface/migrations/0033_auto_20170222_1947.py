# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('frontEndInterface', '0032_auto_20170222_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessCooperation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 47, 33, 50144), verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4')),
                ('view_num', models.IntegerField(default=0, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe6\x95\xb0')),
                ('title', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('image', models.ImageField(default=None, upload_to=b'Business', null=True, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87', blank=True)),
                ('body', models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('exc_editor', models.CharField(default=b'\xe6\x9c\xac\xe5\x85\xac\xe5\x91\x8a\xe6\x89\xa7\xe8\xa1\x8c\xe7\xbc\x96\xe8\xbe\x91', max_length=20, verbose_name=b'\xe6\x89\xa7\xe8\xa1\x8c\xe7\xbc\x96\xe8\xbe\x91')),
                ('duty_editor', models.CharField(default=b'\xe6\x9c\xac\xe5\x85\xac\xe5\x91\x8a\xe8\xb4\xa3\xe4\xbb\xbb\xe7\xbc\x96\xe8\xbe\x91', max_length=20, verbose_name=b'\xe8\xb4\xa3\xe4\xbb\xbb\xe7\xbc\x96\xe8\xbe\x91')),
                ('video_url', models.CharField(default=b'\xe8\xa7\x86\xe9\xa2\x91\xe9\x93\xbe\xe6\x8e\xa5', max_length=200, verbose_name=b'\xe8\xa7\x86\xe9\xa2\x91\xe9\x93\xbe\xe6\x8e\xa5', blank=True)),
                ('file', models.FileField(default=None, upload_to=b'information/files', null=True, verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6', blank=True)),
            ],
            options={
                'verbose_name': '\u5546\u4e1a\u5408\u4f5c',
                'verbose_name_plural': '\u5546\u4e1a\u5408\u4f5c',
            },
        ),
        migrations.CreateModel(
            name='ForeignContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 47, 33, 50814), verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4')),
                ('view_num', models.IntegerField(default=0, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe6\x95\xb0')),
                ('title', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('image', models.ImageField(default=None, upload_to=b'ForeignContact', null=True, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87', blank=True)),
                ('body', models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('exc_editor', models.CharField(default=b'\xe6\x9c\xac\xe5\x85\xac\xe5\x91\x8a\xe6\x89\xa7\xe8\xa1\x8c\xe7\xbc\x96\xe8\xbe\x91', max_length=20, verbose_name=b'\xe6\x89\xa7\xe8\xa1\x8c\xe7\xbc\x96\xe8\xbe\x91')),
                ('duty_editor', models.CharField(default=b'\xe6\x9c\xac\xe5\x85\xac\xe5\x91\x8a\xe8\xb4\xa3\xe4\xbb\xbb\xe7\xbc\x96\xe8\xbe\x91', max_length=20, verbose_name=b'\xe8\xb4\xa3\xe4\xbb\xbb\xe7\xbc\x96\xe8\xbe\x91')),
                ('video_url', models.CharField(default=b'\xe8\xa7\x86\xe9\xa2\x91\xe9\x93\xbe\xe6\x8e\xa5', max_length=200, verbose_name=b'\xe8\xa7\x86\xe9\xa2\x91\xe9\x93\xbe\xe6\x8e\xa5', blank=True)),
                ('file', models.FileField(default=None, upload_to=b'information/files', null=True, verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6', blank=True)),
            ],
            options={
                'verbose_name': '\u5916\u4e8b\u8054\u7edc',
                'verbose_name_plural': '\u5916\u4e8b\u8054\u7edc',
            },
        ),
        migrations.AlterField(
            model_name='academy',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 47, 33, 56638), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 47, 33, 52812), verbose_name=b'\xe7\x94\xb3\xe8\xaf\xb7\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='chef',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 47, 33, 46127), verbose_name=b'\xe4\xb8\x8a\xe4\xbb\xbb\xe6\x97\xb6\xe9\x97\xb4(\xe6\x8e\x92\xe5\xba\x8f\xe7\x94\xa8)'),
        ),
        migrations.AlterField(
            model_name='fixserver',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 47, 33, 53376), verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='information',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 47, 33, 49494), verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 47, 33, 51598), verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='rights',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 47, 33, 57107), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 47, 33, 48868), verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 47, 33, 53898), verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='thoughts',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 47, 33, 57569), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 47, 33, 56123), verbose_name=b'\xe4\xb8\x8a\xe4\xbc\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 47, 33, 55610), verbose_name=b'\xe4\xb8\x8a\xe4\xbc\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 47, 33, 47557), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 19, 47, 33, 46842), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
