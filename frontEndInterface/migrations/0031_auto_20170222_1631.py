# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('frontEndInterface', '0030_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='video_url',
            field=models.CharField(default=b'\xe8\xa7\x86\xe9\xa2\x91\xe9\x93\xbe\xe6\x8e\xa5', max_length=200, verbose_name=b'\xe8\xa7\x86\xe9\xa2\x91\xe9\x93\xbe\xe6\x8e\xa5', blank=True),
        ),
        migrations.AddField(
            model_name='information',
            name='video_url',
            field=models.CharField(default=b'\xe8\xa7\x86\xe9\xa2\x91\xe9\x93\xbe\xe6\x8e\xa5', max_length=200, verbose_name=b'\xe8\xa7\x86\xe9\xa2\x91\xe9\x93\xbe\xe6\x8e\xa5', blank=True),
        ),
        migrations.AddField(
            model_name='school',
            name='video_url',
            field=models.CharField(default=b'\xe8\xa7\x86\xe9\xa2\x91\xe9\x93\xbe\xe6\x8e\xa5', max_length=200, verbose_name=b'\xe8\xa7\x86\xe9\xa2\x91\xe9\x93\xbe\xe6\x8e\xa5', blank=True),
        ),
        migrations.AddField(
            model_name='someelse',
            name='organization_framework_video',
            field=models.CharField(default=b'\xe8\xa7\x86\xe9\xa2\x91\xe8\xbf\x9e\xe6\x8e\xa5', max_length=200, verbose_name=b'\xe7\xbb\x84\xe7\xbb\x87\xe6\x9e\xb6\xe6\x9e\x84\xe8\xa7\x86\xe9\xa2\x91', blank=True),
        ),
        migrations.AddField(
            model_name='someelse',
            name='school_system_brief_video',
            field=models.CharField(default=b'\xe8\xa7\x86\xe9\xa2\x91\xe8\xbf\x9e\xe6\x8e\xa5', max_length=200, verbose_name=b'\xe9\x99\xa2\xe4\xbc\x9a\xe4\xbd\x93\xe7\xb3\xbb\xe8\xa7\x86\xe9\xa2\x91', blank=True),
        ),
        migrations.AddField(
            model_name='x_news',
            name='file',
            field=models.FileField(default=None, upload_to=b'xnews/files', null=True, verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6', blank=True),
        ),
        migrations.AlterField(
            model_name='academy',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 16, 31, 57, 755290), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='academy',
            name='text',
            field=models.TextField(default=b'\xe5\xad\xa6\xe6\x9c\xaf\xe9\x82\xa3\xe4\xb8\x80\xe6\xa0\x8f\xe8\xa6\x81\xe5\xa1\xab\xe5\x85\x85\xe7\x9a\x84\xe5\xad\x97\xe7\xac\xa6', verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='academy',
            name='title',
            field=models.CharField(default=b'\xe5\xad\xa6\xe6\x9c\xaf\xe9\x82\xa3\xe4\xb8\x80\xe6\xa0\x8f\xe8\xa6\x81\xe5\xa1\xab\xe5\x85\x85\xe7\x9a\x84\xe5\xad\x97\xe7\xac\xa6', max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='academy',
            name='url',
            field=models.CharField(default=b'\xe8\xbf\x99\xe4\xb8\xaa\xe5\xad\xa6\xe6\x9c\xaf\xe6\x89\x80\xe6\x8c\x87\xe5\x90\x91\xe7\x9a\x84url', max_length=200, verbose_name=b'\xe9\x93\xbe\xe6\x8e\xa5'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 16, 31, 57, 751353), verbose_name=b'\xe7\x94\xb3\xe8\xaf\xb7\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='department',
            field=models.CharField(max_length=100, verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='image',
            field=models.ImageField(upload_to=b'apply', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87', blank=True),
        ),
        migrations.AlterField(
            model_name='apply',
            name='introduction',
            field=models.TextField(verbose_name=b'\xe8\x87\xaa\xe6\x88\x91\xe4\xbb\x8b\xe7\xbb\x8d'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='school',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name=b'\xe5\xad\xa6\xe6\xa0\xa1', blank=True),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='content',
            field=models.CharField(max_length=200, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='image',
            field=models.ImageField(default=None, upload_to=b'carousel', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='title',
            field=models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='url',
            field=models.CharField(max_length=100, verbose_name=b'\xe9\x93\xbe\xe6\x8e\xa5'),
        ),
        migrations.AlterField(
            model_name='chef',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 16, 31, 57, 746278), verbose_name=b'\xe4\xb8\x8a\xe4\xbb\xbb\xe6\x97\xb6\xe9\x97\xb4(\xe6\x8e\x92\xe5\xba\x8f\xe7\x94\xa8)'),
        ),
        migrations.AlterField(
            model_name='chef',
            name='department',
            field=models.ForeignKey(verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8', to='frontEndInterface.Department'),
        ),
        migrations.AlterField(
            model_name='chef',
            name='grade',
            field=models.CharField(default=b'', max_length=20, verbose_name=b'\xe5\xb9\xb4\xe7\xba\xa7'),
        ),
        migrations.AlterField(
            model_name='chef',
            name='if_chef_now',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x9c\xa8\xe4\xbb\xbb'),
        ),
        migrations.AlterField(
            model_name='chef',
            name='image',
            field=models.ImageField(default=None, upload_to=b'chef', null=True, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='chef',
            name='introduction',
            field=models.TextField(default=b'introduction', verbose_name=b'\xe4\xbb\x8b\xe7\xbb\x8d'),
        ),
        migrations.AlterField(
            model_name='chef',
            name='name',
            field=models.CharField(default=b'\xe9\x83\xa8\xe9\x95\xbf\xe7\x9a\x84\xe5\x90\x8d\xe5\xad\x97', max_length=20, verbose_name=b'\xe9\x83\xa8\xe9\x95\xbf'),
        ),
        migrations.AlterField(
            model_name='department',
            name='image',
            field=models.ImageField(default=None, upload_to=b'department', null=True, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='department',
            name='introduction',
            field=models.TextField(default=b'\xe8\xbf\x99\xe6\x98\xaf\xe7\xae\x80\xe4\xbb\x8b', verbose_name=b'\xe4\xbb\x8b\xe7\xbb\x8d'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(default=b'\xe9\x83\xa8\xe9\x97\xa8\xe7\x9a\x84\xe5\x90\x8d\xe5\xad\x97', max_length=20, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='fixserver',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 16, 31, 57, 752037), verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='fixserver',
            name='image',
            field=models.ImageField(default=None, upload_to=b'fixServer', null=True, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87', blank=True),
        ),
        migrations.AlterField(
            model_name='fixserver',
            name='name',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97', blank=True),
        ),
        migrations.AlterField(
            model_name='fixserver',
            name='text',
            field=models.TextField(default=None, null=True, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='fixserver',
            name='title',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98', blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='body',
            field=models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='information',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 16, 31, 57, 749562), verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='information',
            name='duty_editor',
            field=models.CharField(default=b'\xe6\x9c\xac\xe5\x85\xac\xe5\x91\x8a\xe8\xb4\xa3\xe4\xbb\xbb\xe7\xbc\x96\xe8\xbe\x91', max_length=20, verbose_name=b'\xe8\xb4\xa3\xe4\xbb\xbb\xe7\xbc\x96\xe8\xbe\x91'),
        ),
        migrations.AlterField(
            model_name='information',
            name='exc_editor',
            field=models.CharField(default=b'\xe6\x9c\xac\xe5\x85\xac\xe5\x91\x8a\xe6\x89\xa7\xe8\xa1\x8c\xe7\xbc\x96\xe8\xbe\x91', max_length=20, verbose_name=b'\xe6\x89\xa7\xe8\xa1\x8c\xe7\xbc\x96\xe8\xbe\x91'),
        ),
        migrations.AlterField(
            model_name='information',
            name='image',
            field=models.ImageField(default=None, upload_to=b'information', null=True, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87', blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='title',
            field=models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='information',
            name='view_num',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe6\x95\xb0'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='body',
            field=models.TextField(verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='notice',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 16, 31, 57, 750212), verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='notice',
            name='duty_editor',
            field=models.CharField(default=b'\xe6\x9c\xac\xe5\x85\xac\xe5\x91\x8a\xe8\xb4\xa3\xe4\xbb\xbb\xe7\xbc\x96\xe8\xbe\x91', max_length=20, verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='notice',
            name='exc_editor',
            field=models.CharField(default=b'\xe6\x9c\xac\xe5\x85\xac\xe5\x91\x8a\xe6\x89\xa7\xe8\xa1\x8c\xe7\xbc\x96\xe8\xbe\x91', max_length=20, verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='notice',
            name='image',
            field=models.ImageField(default=None, upload_to=b'information', verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='notice',
            name='title',
            field=models.CharField(max_length=100, verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='rights',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 16, 31, 57, 755744), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='rights',
            name='text',
            field=models.TextField(default=b'\xe6\x9d\x83\xe7\x9b\x8a\xe9\x82\xa3\xe4\xb8\x80\xe6\xa0\x8f\xe8\xa6\x81\xe5\xa1\xab\xe5\x85\x85\xe7\x9a\x84\xe5\xad\x97\xe7\xac\xa6', verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='rights',
            name='title',
            field=models.CharField(default=b'\xe6\x9d\x83\xe7\x9b\x8a\xe9\x82\xa3\xe4\xb8\x80\xe6\xa0\x8f\xe8\xa6\x81\xe5\xa1\xab\xe5\x85\x85\xe7\x9a\x84\xe5\xad\x97\xe7\xac\xa6', max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='rights',
            name='url',
            field=models.CharField(default=b'\xe8\xbf\x99\xe4\xb8\xaa\xe6\x9d\x83\xe7\x9b\x8a\xe5\xad\x97\xe6\xae\xb5\xe6\x89\x80\xe6\x8c\x87\xe5\x90\x91\xe7\x9a\x84url', max_length=200, verbose_name=b'\xe9\x93\xbe\xe6\x8e\xa5'),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='body',
            field=models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 16, 31, 57, 748969), verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='duty_editor',
            field=models.CharField(default=b'\xe6\x9c\xac\xe6\x96\xb0\xe9\x97\xbb\xe8\xb4\xa3\xe4\xbb\xbb\xe7\xbc\x96\xe8\xbe\x91', max_length=20, verbose_name=b'\xe8\xb4\xa3\xe4\xbb\xbb\xe7\xbc\x96\xe8\xbe\x91'),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='exc_editor',
            field=models.CharField(default=b'\xe6\x9c\xac\xe6\x96\xb0\xe9\x97\xbb\xe6\x89\xa7\xe8\xa1\x8c\xe7\xbc\x96\xe8\xbe\x91', max_length=20, verbose_name=b'\xe6\x89\xa7\xe8\xa1\x8c\xe7\xbc\x96\xe8\xbe\x91'),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='image',
            field=models.ImageField(upload_to=b'snews', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='school',
            field=models.ForeignKey(verbose_name=b'\xe9\x99\xa2\xe4\xbc\x9a', to='frontEndInterface.School'),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='title',
            field=models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='video',
            field=models.CharField(max_length=200, verbose_name=b'\xe8\xa7\x86\xe9\xa2\x91\xe9\x93\xbe\xe6\x8e\xa5', blank=True),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='view_num',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe6\xac\xa1\xe6\x95\xb0'),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='content',
            field=models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 16, 31, 57, 752558), verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='name',
            field=models.CharField(default=b'\xe7\xbb\xb4\xe6\x9d\x83\xe8\x80\x85\xe5\x90\x8d\xe5\xad\x97', max_length=20, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97'),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='title',
            field=models.CharField(default=b'\xe7\xbb\xb4\xe6\x9d\x83\xe4\xb8\xbb\xe9\xa2\x98', max_length=200, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='school',
            name='chef',
            field=models.CharField(max_length=20, verbose_name=b'\xe4\xb8\xbb\xe5\xb8\xad'),
        ),
        migrations.AlterField(
            model_name='school',
            name='chef_introduction',
            field=models.TextField(verbose_name=b'\xe4\xb8\xbb\xe5\xb8\xad\xe4\xbb\x8b\xe7\xbb\x8d'),
        ),
        migrations.AlterField(
            model_name='school',
            name='introduction',
            field=models.TextField(verbose_name=b'\xe4\xbb\x8b\xe7\xbb\x8d'),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'\xe9\x99\xa2\xe4\xbc\x9a\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='someelse',
            name='organization_framework_image',
            field=models.ImageField(default=None, upload_to=b'organizatin_framework', null=True, verbose_name=b'\xe7\xbb\x84\xe7\xbb\x87\xe6\x9e\xb6\xe6\x9e\x84\xe5\x9b\xbe\xe7\x89\x87', blank=True),
        ),
        migrations.AlterField(
            model_name='someelse',
            name='organization_framework_text',
            field=models.TextField(default=None, null=True, verbose_name=b'\xe7\xbb\x84\xe7\xbb\x87\xe6\x9e\xb6\xe6\x9e\x84\xe5\x86\x85\xe5\xae\xb9', blank=True),
        ),
        migrations.AlterField(
            model_name='someelse',
            name='school_system_brief_image',
            field=models.ImageField(default=None, upload_to=b'school_system', null=True, verbose_name=b'\xe9\x99\xa2\xe4\xbc\x9a\xe4\xbd\x93\xe7\xb3\xbb\xe5\x9b\xbe\xe7\x89\x87', blank=True),
        ),
        migrations.AlterField(
            model_name='someelse',
            name='school_system_brief_text',
            field=models.TextField(default=None, null=True, verbose_name=b'\xe9\x99\xa2\xe4\xbc\x9a\xe4\xbd\x93\xe7\xb3\xbb\xe5\x86\x85\xe5\xae\xb9', blank=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='chef_flag',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\xba\xe9\xaa\xa8\xe5\xb9\xb2'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='department',
            field=models.ForeignKey(verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8', to='frontEndInterface.Department'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='grade',
            field=models.CharField(default=b'', max_length=20, verbose_name=b'\xe5\xb9\xb4\xe7\xba\xa7'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='image',
            field=models.ImageField(upload_to=b'staff', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='introduction',
            field=models.TextField(verbose_name=b'\xe4\xbb\x8b\xe7\xbb\x8d'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='name',
            field=models.CharField(default=b'\xe7\xbb\x84\xe5\x91\x98\xe5\x90\x8d\xe5\xad\x97', max_length=20, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='rank',
            field=models.CharField(default=b'', max_length=20, verbose_name=b'\xe8\x81\x8c\xe5\x8a\xa1'),
        ),
        migrations.AlterField(
            model_name='star',
            name='content',
            field=models.CharField(max_length=200, verbose_name=b'\xe4\xb8\xbb\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='star',
            name='image',
            field=models.ImageField(default=None, upload_to=b'star', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='star',
            name='text',
            field=models.TextField(default=b'', verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='testimage',
            name='Image_x',
            field=models.ImageField(null=True, upload_to=b'image', blank=True),
        ),
        migrations.AlterField(
            model_name='thoughts',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 16, 31, 57, 756193), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='thoughts',
            name='text',
            field=models.TextField(default=b'\xe6\x80\x9d\xe6\xbd\xae\xe9\x82\xa3\xe4\xb8\x80\xe6\xa0\x8f\xe8\xa6\x81\xe5\xa1\xab\xe5\x85\x85\xe7\x9a\x84\xe5\xad\x97\xe7\xac\xa6', verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='thoughts',
            name='title',
            field=models.CharField(default=b'\xe6\x80\x9d\xe6\xbd\xae\xe9\x82\xa3\xe4\xb8\x80\xe6\xa0\x8f\xe8\xa6\x81\xe5\xa1\xab\xe5\x85\x85\xe7\x9a\x84\xe5\xad\x97\xe7\xac\xa6', max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='thoughts',
            name='url',
            field=models.CharField(default=b'\xe8\xbf\x99\xe4\xb8\xaa\xe6\x80\x9d\xe6\xbd\xae\xe5\xad\x97\xe6\xae\xb5\xe6\x89\x80\xe6\x8c\x87\xe5\x90\x91\xe7\x9a\x84url', max_length=200, verbose_name=b'\xe9\x93\xbe\xe6\x8e\xa5'),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='image',
            field=models.ImageField(upload_to=b'wonderful_picture', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='title',
            field=models.CharField(default=b'\xe5\x9b\xbe\xe7\x89\x87\xe7\x9a\x84\xe6\xa0\x87\xe9\xa2\x98\xef\xbc\x8c\xe4\xb8\x8d\xe8\xa6\x81\xe8\xb6\x85\xe8\xbf\x87100\xe4\xb8\xaa\xe5\xad\x97', max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 16, 31, 57, 754673), verbose_name=b'\xe4\xb8\x8a\xe4\xbc\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='compress_image',
            field=models.ImageField(default=None, upload_to=b'wonderful_video', verbose_name=b'\xe7\xbc\xa9\xe7\x95\xa5\xe5\x9b\xbe'),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='title',
            field=models.CharField(default=b'\xe8\xa7\x86\xe9\xa2\x91\xe7\x9a\x84\xe6\xa0\x87\xe9\xa2\x98', max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 16, 31, 57, 754180), verbose_name=b'\xe4\xb8\x8a\xe4\xbc\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='video_url',
            field=models.CharField(max_length=200, verbose_name=b'\xe8\xa7\x86\xe9\xa2\x91\xe9\x93\xbe\xe6\x8e\xa5'),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='body',
            field=models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 16, 31, 57, 747627), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='department',
            field=models.ForeignKey(verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8', to='frontEndInterface.Department'),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='image',
            field=models.ImageField(upload_to=b'activity', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8'),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='sponsor',
            field=models.CharField(max_length=20, verbose_name=b'\xe8\xb5\x9e\xe5\x8a\xa9\xe5\x95\x86'),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='video',
            field=models.CharField(max_length=200, verbose_name=b'\xe8\xa7\x86\xe9\xa2\x91\xe9\x93\xbe\xe6\x8e\xa5', blank=True),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='body',
            field=models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 16, 31, 57, 746924), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='department',
            field=models.ForeignKey(verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8', to='frontEndInterface.Department'),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='duty_editor',
            field=models.CharField(default=b'\xe6\x9c\xac\xe6\x96\xb0\xe9\x97\xbb\xe8\xb4\xa3\xe4\xbb\xbb\xe7\xbc\x96\xe8\xbe\x91', max_length=20, verbose_name=b'\xe8\xb4\xa3\xe4\xbb\xbb\xe7\xbc\x96\xe8\xbe\x91'),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='exc_editor',
            field=models.CharField(default=b'\xe6\x9c\xac\xe6\x96\xb0\xe9\x97\xbb\xe6\x89\xa7\xe8\xa1\x8c\xe7\xbc\x96\xe8\xbe\x91', max_length=20, verbose_name=b'\xe6\x89\xa7\xe8\xa1\x8c\xe7\xbc\x96\xe8\xbe\x91'),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='image',
            field=models.ImageField(upload_to=b'xnews', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='title',
            field=models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='video',
            field=models.CharField(max_length=200, verbose_name=b'\xe8\xa7\x86\xe9\xa2\x91\xe9\x93\xbe\xe6\x8e\xa5', blank=True),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='view_num',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe6\xac\xa1\xe6\x95\xb0'),
        ),
    ]
