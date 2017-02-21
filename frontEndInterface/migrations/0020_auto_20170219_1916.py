# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('frontEndInterface', '0019_auto_20170219_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='someelse',
            name='school_system_brief_image',
            field=models.ImageField(default=None, null=True, upload_to=b'static/xxsh/school_system', blank=True),
        ),
        migrations.AddField(
            model_name='someelse',
            name='school_system_brief_text',
            field=DjangoUeditor.models.UEditorField(verbose_name='\u5185\u5bb9   ', blank=True),
        ),
        migrations.AlterField(
            model_name='academy',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 19, 16, 48, 195016)),
        ),
        migrations.AlterField(
            model_name='apply',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 19, 16, 48, 191907)),
        ),
        migrations.AlterField(
            model_name='information',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 19, 16, 48, 190580)),
        ),
        migrations.AlterField(
            model_name='rights',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 19, 16, 48, 195482)),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 19, 16, 48, 189976)),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 19, 16, 48, 192453)),
        ),
        migrations.AlterField(
            model_name='thoughts',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 19, 16, 48, 195965)),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 19, 16, 48, 194383)),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 19, 16, 48, 193874)),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 19, 16, 48, 188836)),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 19, 16, 48, 188001)),
        ),
    ]
