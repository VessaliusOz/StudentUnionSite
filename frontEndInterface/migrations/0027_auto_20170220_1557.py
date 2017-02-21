# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('frontEndInterface', '0026_auto_20170220_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=20, verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b')),
            ],
        ),
        migrations.CreateModel(
            name='CourseFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'static/xxsh/files', verbose_name=b'\xe6\x96\x87\xe6\xa1\xa3')),
                ('file_name', models.CharField(default=b'\xe6\x96\x87\xe6\xa1\xa3\xe5\x90\x8d\xe7\xa7\xb0', max_length=20, verbose_name=b'\xe6\x96\x87\xe6\xa1\xa3\xe5\x90\x8d\xe7\xa7\xb0')),
                ('course', models.ForeignKey(verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe6\x96\x87\xe6\xa1\xa3', to='frontEndInterface.Course')),
            ],
        ),
        migrations.AlterField(
            model_name='academy',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 15, 57, 49, 319649)),
        ),
        migrations.AlterField(
            model_name='apply',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 15, 57, 49, 315671)),
        ),
        migrations.AlterField(
            model_name='chef',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 15, 57, 49, 307463)),
        ),
        migrations.AlterField(
            model_name='fixserver',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 15, 57, 49, 316298)),
        ),
        migrations.AlterField(
            model_name='information',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 15, 57, 49, 310733)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 15, 57, 49, 312213)),
        ),
        migrations.AlterField(
            model_name='rights',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 15, 57, 49, 320121)),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 15, 57, 49, 310103)),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 15, 57, 49, 316867)),
        ),
        migrations.AlterField(
            model_name='thoughts',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 15, 57, 49, 320596)),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 15, 57, 49, 319121)),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 15, 57, 49, 318602)),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 15, 57, 49, 308888)),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 15, 57, 49, 308170)),
        ),
    ]
