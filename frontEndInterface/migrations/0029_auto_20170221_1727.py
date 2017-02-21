# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('frontEndInterface', '0028_auto_20170221_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academy',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 17, 27, 37, 847663)),
        ),
        migrations.AlterField(
            model_name='apply',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 17, 27, 37, 843912)),
        ),
        migrations.AlterField(
            model_name='apply',
            name='image',
            field=models.ImageField(upload_to=b'apply', blank=True),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='image',
            field=models.ImageField(default=None, upload_to=b'carousel'),
        ),
        migrations.AlterField(
            model_name='chef',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 17, 27, 37, 838691)),
        ),
        migrations.AlterField(
            model_name='chef',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=b'chef'),
        ),
        migrations.AlterField(
            model_name='coursefile',
            name='file',
            field=models.FileField(upload_to=b'course_file', verbose_name=b'\xe6\x96\x87\xe6\xa1\xa3'),
        ),
        migrations.AlterField(
            model_name='department',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=b'department'),
        ),
        migrations.AlterField(
            model_name='fixserver',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 17, 27, 37, 844484)),
        ),
        migrations.AlterField(
            model_name='fixserver',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=b'fixServer', blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 17, 27, 37, 842008)),
        ),
        migrations.AlterField(
            model_name='information',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=b'information', blank=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 17, 27, 37, 842737)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='image',
            field=models.ImageField(default=None, upload_to=b'information'),
        ),
        migrations.AlterField(
            model_name='rights',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 17, 27, 37, 848124)),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 17, 27, 37, 841388)),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='image',
            field=models.ImageField(upload_to=b'snews'),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 17, 27, 37, 845004)),
        ),
        migrations.AlterField(
            model_name='someelse',
            name='organization_framework_image',
            field=models.ImageField(default=None, null=True, upload_to=b'organizatin_framework', blank=True),
        ),
        migrations.AlterField(
            model_name='someelse',
            name='school_system_brief_image',
            field=models.ImageField(default=None, null=True, upload_to=b'school_system', blank=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='image',
            field=models.ImageField(upload_to=b'staff'),
        ),
        migrations.AlterField(
            model_name='star',
            name='image',
            field=models.ImageField(default=None, upload_to=b'star'),
        ),
        migrations.AlterField(
            model_name='thoughts',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 17, 27, 37, 848584)),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='image',
            field=models.ImageField(upload_to=b'wonderful_picture'),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 17, 27, 37, 847131)),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='compress_image',
            field=models.ImageField(default=None, upload_to=b'wonderful_video'),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 17, 27, 37, 846634)),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 17, 27, 37, 840268)),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='image',
            field=models.ImageField(upload_to=b'activity'),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 17, 27, 37, 839574)),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='image',
            field=models.ImageField(upload_to=b'xnews'),
        ),
    ]
