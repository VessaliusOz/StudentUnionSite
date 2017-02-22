# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('frontEndInterface', '0033_auto_20170222_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2017, 2, 22, 20, 20, 0, 551139), verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4')),
                ('view_num', models.IntegerField(default=0, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe6\x95\xb0')),
                ('title', models.CharField(default=b'\xe6\xa0\x87\xe9\xa2\x98', unique=True, max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('image', models.ImageField(default=None, upload_to=b'CourseInformation', null=True, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87', blank=True)),
                ('body', models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('exc_editor', models.CharField(default=b'\xe6\x9c\xac\xe5\x85\xac\xe5\x91\x8a\xe6\x89\xa7\xe8\xa1\x8c\xe7\xbc\x96\xe8\xbe\x91', max_length=20, verbose_name=b'\xe6\x89\xa7\xe8\xa1\x8c\xe7\xbc\x96\xe8\xbe\x91')),
                ('duty_editor', models.CharField(default=b'\xe6\x9c\xac\xe5\x85\xac\xe5\x91\x8a\xe8\xb4\xa3\xe4\xbb\xbb\xe7\xbc\x96\xe8\xbe\x91', max_length=20, verbose_name=b'\xe8\xb4\xa3\xe4\xbb\xbb\xe7\xbc\x96\xe8\xbe\x91')),
                ('file', models.FileField(default=None, upload_to=b'information/files', null=True, verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6', blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='academy',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 20, 20, 0, 549332), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='academy',
            name='title',
            field=models.CharField(default=b'\xe5\xad\xa6\xe6\x9c\xaf\xe9\x82\xa3\xe4\xb8\x80\xe6\xa0\x8f\xe8\xa6\x81\xe5\xa1\xab\xe5\x85\x85\xe7\x9a\x84\xe5\xad\x97\xe7\xac\xa6', unique=True, max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 20, 20, 0, 545455), verbose_name=b'\xe7\x94\xb3\xe8\xaf\xb7\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='businesscooperation',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 20, 20, 0, 542786), verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='businesscooperation',
            name='file',
            field=models.FileField(default=None, upload_to=b'Business/files', null=True, verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6', blank=True),
        ),
        migrations.AlterField(
            model_name='businesscooperation',
            name='title',
            field=models.CharField(default=b'\xe6\xa0\x87\xe9\xa2\x98', unique=True, max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='chef',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 20, 20, 0, 538466), verbose_name=b'\xe4\xb8\x8a\xe4\xbb\xbb\xe6\x97\xb6\xe9\x97\xb4(\xe6\x8e\x92\xe5\xba\x8f\xe7\x94\xa8)'),
        ),
        migrations.AlterField(
            model_name='coursefile',
            name='file_name',
            field=models.CharField(default=b'\xe6\x96\x87\xe6\xa1\xa3\xe5\x90\x8d\xe7\xa7\xb0', unique=True, max_length=20, verbose_name=b'\xe6\x96\x87\xe6\xa1\xa3\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(default=b'\xe9\x83\xa8\xe9\x97\xa8\xe7\x9a\x84\xe5\x90\x8d\xe5\xad\x97', unique=True, max_length=20, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='fixserver',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 20, 20, 0, 546018), verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='foreigncontact',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 20, 20, 0, 543464), verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='foreigncontact',
            name='file',
            field=models.FileField(default=None, upload_to=b'ForeignContact/files', null=True, verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6', blank=True),
        ),
        migrations.AlterField(
            model_name='foreigncontact',
            name='title',
            field=models.CharField(default=b'\xe6\xa0\x87\xe9\xa2\x98', unique=True, max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='information',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 20, 20, 0, 542063), verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='information',
            name='title',
            field=models.CharField(default=b'\xe6\xa0\x87\xe9\xa2\x98', unique=True, max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 20, 20, 0, 544271), verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='rights',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 20, 20, 0, 549783), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='rights',
            name='title',
            field=models.CharField(default=b'\xe6\x9d\x83\xe7\x9b\x8a\xe9\x82\xa3\xe4\xb8\x80\xe6\xa0\x8f\xe8\xa6\x81\xe5\xa1\xab\xe5\x85\x85\xe7\x9a\x84\xe5\xad\x97\xe7\xac\xa6', unique=True, max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 20, 20, 0, 541416), verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='title',
            field=models.CharField(default=b'\xe6\xa0\x87\xe9\xa2\x98', unique=True, max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 20, 20, 0, 546546), verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='name',
            field=models.CharField(default=b'\xe7\xbb\x84\xe5\x91\x98\xe5\x90\x8d\xe5\xad\x97', unique=True, max_length=20, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='thoughts',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 20, 20, 0, 550358), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='thoughts',
            name='title',
            field=models.CharField(default=b'\xe6\x80\x9d\xe6\xbd\xae\xe9\x82\xa3\xe4\xb8\x80\xe6\xa0\x8f\xe8\xa6\x81\xe5\xa1\xab\xe5\x85\x85\xe7\x9a\x84\xe5\xad\x97\xe7\xac\xa6', unique=True, max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 20, 20, 0, 548813), verbose_name=b'\xe4\xb8\x8a\xe4\xbc\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 20, 20, 0, 548220), verbose_name=b'\xe4\xb8\x8a\xe4\xbc\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 20, 20, 0, 540174), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='name',
            field=models.CharField(unique=True, max_length=100, verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8'),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 20, 20, 0, 539227), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='title',
            field=models.CharField(default=b'\xe6\xa0\x87\xe9\xa2\x98', unique=True, max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
    ]
