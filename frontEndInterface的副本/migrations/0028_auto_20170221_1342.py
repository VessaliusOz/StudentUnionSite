# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('frontEndInterface', '0027_auto_20170220_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Image_x', models.ImageField(null=True, upload_to=b'image', blank=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': '\u8bfe\u7a0b', 'verbose_name_plural': '\u8bfe\u7a0b'},
        ),
        migrations.AlterModelOptions(
            name='coursefile',
            options={'verbose_name': '\u8bfe\u7a0b\u6587\u6863', 'verbose_name_plural': '\u8bfe\u7a0b\u6587\u6863'},
        ),
        migrations.AlterField(
            model_name='academy',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 13, 42, 25, 144731)),
        ),
        migrations.AlterField(
            model_name='apply',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 13, 42, 25, 140929)),
        ),
        migrations.AlterField(
            model_name='chef',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 13, 42, 25, 135575)),
        ),
        migrations.AlterField(
            model_name='coursefile',
            name='course',
            field=models.ForeignKey(verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b', to='frontEndInterface.Course'),
        ),
        migrations.AlterField(
            model_name='fixserver',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 13, 42, 25, 141491)),
        ),
        migrations.AlterField(
            model_name='information',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 13, 42, 25, 138979)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 13, 42, 25, 139729)),
        ),
        migrations.AlterField(
            model_name='rights',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 13, 42, 25, 145187)),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 13, 42, 25, 138370)),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 13, 42, 25, 142015)),
        ),
        migrations.AlterField(
            model_name='someelse',
            name='school_system_brief_text',
            field=models.TextField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='thoughts',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 13, 42, 25, 145666)),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 13, 42, 25, 144174)),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 13, 42, 25, 143670)),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 13, 42, 25, 137249)),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 13, 42, 25, 136537)),
        ),
    ]
