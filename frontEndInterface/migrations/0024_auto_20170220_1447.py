# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('frontEndInterface', '0023_auto_20170219_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='FixServer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('title', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('text', models.TextField(default=None, null=True)),
                ('image', models.ImageField(default=None, null=True, upload_to=b'static/xxsh/Fixserver', blank=True)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2017, 2, 20, 14, 47, 30, 613280))),
            ],
            options={
                'verbose_name': '\u540e\u52e4\u62a5\u4fee',
                'verbose_name_plural': '\u540e\u52e4\u62a5\u4fee',
            },
        ),
        migrations.AlterModelOptions(
            name='academy',
            options={'verbose_name': '\u5b66\u672f', 'verbose_name_plural': '\u5b66\u672f'},
        ),
        migrations.AlterModelOptions(
            name='apply',
            options={'verbose_name': '\u7533\u8bf7', 'verbose_name_plural': '\u7533\u8bf7'},
        ),
        migrations.AlterModelOptions(
            name='carousel',
            options={'verbose_name': '\u8f6e\u64ad\u5668', 'verbose_name_plural': '\u8f6e\u64ad\u5668'},
        ),
        migrations.AlterModelOptions(
            name='chef',
            options={'verbose_name': '\u90e8\u957f', 'verbose_name_plural': '\u90e8\u957f'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': '\u90e8\u95e8', 'verbose_name_plural': '\u90e8\u95e8'},
        ),
        migrations.AlterModelOptions(
            name='information',
            options={'verbose_name': '\u516c\u544a', 'verbose_name_plural': '\u516c\u544a'},
        ),
        migrations.AlterModelOptions(
            name='rights',
            options={'verbose_name': '\u6743\u76ca', 'verbose_name_plural': '\u6743\u76ca'},
        ),
        migrations.AlterModelOptions(
            name='s_news',
            options={'verbose_name': '\u9662\u4f1a\u65b0\u95fb', 'verbose_name_plural': '\u9662\u4f1a\u65b0\u95fb'},
        ),
        migrations.AlterModelOptions(
            name='safeguard',
            options={'verbose_name': '\u7ef4\u6743', 'verbose_name_plural': '\u7ef4\u6743'},
        ),
        migrations.AlterModelOptions(
            name='school',
            options={'verbose_name': '\u9662\u5b66\u751f\u4f1a', 'verbose_name_plural': '\u9662\u5b66\u751f\u4f1a'},
        ),
        migrations.AlterModelOptions(
            name='someelse',
            options={'verbose_name': '\u9662\u4f1a\u4f53\u7cfb/\u6821\u5b66\u751f\u4f1a\u7ec4\u7ec7\u67b6\u6784', 'verbose_name_plural': '\u9662\u4f1a\u4f53\u7cfb/\u6821\u5b66\u751f\u4f1a\u7ec4\u7ec7\u67b6\u6784'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': '\u4eba\u5458', 'verbose_name_plural': '\u4eba\u5458'},
        ),
        migrations.AlterModelOptions(
            name='star',
            options={'verbose_name': '\u67d0\u6708\u4e4b\u661f', 'verbose_name_plural': '\u67d0\u6708\u4e4b\u661f'},
        ),
        migrations.AlterModelOptions(
            name='thoughts',
            options={'verbose_name': '\u601d\u6f6e', 'verbose_name_plural': '\u601d\u6f6e'},
        ),
        migrations.AlterModelOptions(
            name='wondpicture',
            options={'verbose_name': '\u56fe\u7247', 'verbose_name_plural': '\u56fe\u7247'},
        ),
        migrations.AlterModelOptions(
            name='wondvideo',
            options={'verbose_name': '\u89c6\u9891', 'verbose_name_plural': '\u89c6\u9891'},
        ),
        migrations.AlterModelOptions(
            name='x_activity',
            options={'verbose_name': '\u6821\u5b66\u751f\u4f1a\u6d3b\u52a8', 'verbose_name_plural': '\u6821\u5b66\u751f\u4f1a\u6d3b\u52a8'},
        ),
        migrations.AlterModelOptions(
            name='x_news',
            options={'verbose_name': '\u6821\u5b66\u751f\u4f1a\u65b0\u95fb', 'verbose_name_plural': '\u6821\u5b66\u751f\u4f1a\u65b0\u95fb'},
        ),
        migrations.AlterField(
            model_name='academy',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 14, 47, 30, 616433)),
        ),
        migrations.AlterField(
            model_name='apply',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 14, 47, 30, 612708)),
        ),
        migrations.AlterField(
            model_name='information',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 14, 47, 30, 610803)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 14, 47, 30, 611408)),
        ),
        migrations.AlterField(
            model_name='rights',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 14, 47, 30, 616897)),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 14, 47, 30, 610201)),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 14, 47, 30, 613799)),
        ),
        migrations.AlterField(
            model_name='thoughts',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 14, 47, 30, 617368)),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 14, 47, 30, 615907)),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 14, 47, 30, 615416)),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 14, 47, 30, 609079)),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 14, 47, 30, 608384)),
        ),
    ]
