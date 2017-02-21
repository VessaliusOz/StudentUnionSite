# coding=utf-8
from django.db import models
from django.utils.datetime_safe import datetime
from DjangoUeditor.models import UEditorField


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=20, default='部门的名字')
    introduction = models.TextField(default='这是简介')
    image = models.ImageField(upload_to='department', default=None, null=True)

    class Meta:
        verbose_name = u'部门'
        verbose_name_plural = u'部门'

    def __unicode__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=20, default='组员名字')
    grade = models.CharField(max_length=20, default='')  # 大几
    rank = models.CharField(max_length=20, default='')
    introduction = models.TextField()
    image = models.ImageField(upload_to='staff')
    department = models.ForeignKey(Department)
    chef_flag = models.BooleanField(default=False)  # 是否是骨干

    class Meta:
        verbose_name = u'人员'
        verbose_name_plural = u'人员'

    def __unicode__(self):
        return self.name


#  顺序没有写。。。。
class Chef(models.Model):
    name = models.CharField(max_length=20, default='部长的名字')
    if_chef_now = models.BooleanField(default=False)
    introduction = models.TextField(default='introduction')
    image = models.ImageField(upload_to='chef', default=None, null=True)
    grade = models.CharField(max_length=20, default='')
    department = models.ForeignKey(Department)
    datetime = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = u'部长'
        verbose_name_plural = u'部长'

    def __unicode__(self):
        return self.name


class X_news(models.Model):
    '''校学生会的新闻'''
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='xnews')
    video = models.CharField(max_length=200, blank=True)
    exc_editor = models.CharField(max_length=20, default='本新闻执行编辑')
    duty_editor = models.CharField(max_length=20, default='本新闻责任编辑')
    view_num = models.IntegerField(default=0)
    datetime = models.DateTimeField(default=datetime.now())
    department = models.ForeignKey(Department)

    class Meta:
        verbose_name = u'校学生会新闻'
        verbose_name_plural = u'校学生会新闻'

    def __unicode__(self):
        return self.title


class X_activity(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='activity')
    video = models.CharField(max_length=200, blank=True)
    sponsor = models.CharField(max_length=20)
    datetime = models.DateTimeField(default=datetime.now())
    department = models.ForeignKey(Department)

    class Meta:
        verbose_name = u'校学生会活动'
        verbose_name_plural = u'校学生会活动'

    def __unicode__(self):
        return self.department.name + "的" + self.name + "活动"


########################################################################
########################################################################

class School(models.Model):
    ''' 学院的学生会 '''
    name = models.CharField(max_length=100)
    introduction = models.TextField()
    chef = models.CharField(max_length=20)
    chef_introduction = models.TextField()

    class Meta:
        verbose_name = u'院学生会'
        verbose_name_plural = u'院学生会'

    def __unicode__(self):
        return self.name


class S_news(models.Model):  # 院会的新闻
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='snews')
    video = models.CharField(max_length=200, blank=True)
    exc_editor = models.CharField(max_length=20, default='本新闻执行编辑')
    duty_editor = models.CharField(max_length=20, default='本新闻责任编辑')
    view_num = models.IntegerField(default=0)
    datetime = models.DateTimeField(default=datetime.now())
    school = models.ForeignKey(School)

    class Meta:
        verbose_name = u'院会新闻'
        verbose_name_plural = u'院会新闻'

    def __unicode__(self):
        return self.title


########################################################################
########################################################################


class Information(models.Model):
    datetime = models.DateTimeField(default=datetime.now())
    view_num = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='information', default=None, blank=True, null=True)
    body = models.TextField()
    exc_editor = models.CharField(max_length=20, default='本公告执行编辑')
    duty_editor = models.CharField(max_length=20, default='本公告责任编辑')

    class Meta:
        verbose_name = u'公告'
        verbose_name_plural = u'公告'

    def __unicode__(self):
        return self.title


class Notice(models.Model):
    datetime = models.DateTimeField(default=datetime.now())
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='information', default=None)
    body = models.TextField()
    exc_editor = models.CharField(max_length=20, default='本公告执行编辑')
    duty_editor = models.CharField(max_length=20, default='本公告责任编辑')

    def __unicode__(self):
        return self.title


class Carousel(models.Model):  # Carousel是轮播器的意思
    image = models.ImageField(upload_to='carousel', default=None)
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)

    class Meta:
        verbose_name = u'轮播器'
        verbose_name_plural = u'轮播器'

    def __unicode__(self):
        return self.title


class Apply(models.Model):
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    introduction = models.TextField()
    image = models.ImageField(upload_to='apply', blank=True)
    datetime = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = u'申请'
        verbose_name_plural = u'申请'

    def __unicode__(self):
        return self.name


class FixServer(models.Model):
    name = models.CharField(max_length=100, default=None, null=True, blank=True)
    title = models.CharField(max_length=100, default=None,null=True, blank=True)
    text = models.TextField(default=None, null=True)
    image = models.ImageField(upload_to='fixServer', default=None, blank=True, null=True)
    datetime = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = u'后勤报修'
        verbose_name_plural = u'后勤报修'


class Safeguard(models.Model):
    name = models.CharField(max_length=20, default='维权者名字')
    title = models.CharField(max_length=200, default='维权主题')
    content = models.TextField()
    datetime = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = u'维权'
        verbose_name_plural = u'维权'

    def __unicode__(self):
        return self.title


###################################################################
#               其他一些元素                                        #
###################################################################
# 一些乱起八糟


class SomeElse(models.Model):
    group_frame = models.ImageField()
    school_system_brief_image = models.ImageField(upload_to='school_system',
                                                  default=None, null=True, blank=True)
    school_system_brief_text = models.TextField(default=None, null=True, blank=True)
    organization_framework_text = UEditorField(u'校学生会组织架构 ', width=600, height=300, toolbars="full", imagePath="",
                                            filePath="", upload_settings={"imageMaxSize":1204000},
                                            settings={}, command=None, blank=True)
    organization_framework_image = models.ImageField(upload_to='organizatin_framework',
                                                  default=None, null=True, blank=True)

    class Meta:
        verbose_name = u'院会体系/校学生会组织架构'
        verbose_name_plural = u'院会体系/校学生会组织架构'

    def __unicode__(self):
        return '院会体系/校学生会组织架构'


class Star(models.Model):  # 某月之星
    content = models.CharField(max_length=200)
    image = models.ImageField(upload_to='star', default=None)
    text = models.TextField(default='')

    class Meta:
        verbose_name = u'某月之星'
        verbose_name_plural = u'某月之星'


    def __unicode__(self):
        return self.content


class WondVideo(models.Model):
    title = models.CharField(max_length=100, default="视频的标题")
    compress_image = models.ImageField(upload_to='wonderful_video', default=None)
    upload_time = models.DateTimeField(default=datetime.now())
    video_url = models.CharField(max_length=200)

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = u'视频'

    def __unicode__(self):
        return self.title


class WondPicture(models.Model):
    title = models.CharField(max_length=100, default="图片的标题，不要超过100个字")
    upload_time = models.DateTimeField(default=datetime.now())
    image = models.ImageField(upload_to='wonderful_picture')

    class Meta:
        verbose_name = u'图片'
        verbose_name_plural = u'图片'

    def __unicode__(self):
        return self.title


class Academy(models.Model):
    title = models.CharField(max_length=100, default="学术那一栏要填充的字符")
    url = models.CharField(max_length=200, default="这个学术所指向的url")
    text = models.TextField(default="学术那一栏要填充的字符")
    datetime = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = u'学术'
        verbose_name_plural = u'学术'

    def __unicode__(self):
        return self.title


class Rights(models.Model):
    title = models.CharField(max_length=100, default="权益那一栏要填充的字符")
    url = models.CharField(max_length=200, default="这个权益字段所指向的url")
    text = models.TextField(default="权益那一栏要填充的字符")
    datetime = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = u'权益'
        verbose_name_plural = u'权益'

    def __unicode__(self):
        return self.title


class Thoughts(models.Model):
    title = models.CharField(max_length=100, default="思潮那一栏要填充的字符")
    url = models.CharField(max_length=200, default="这个思潮字段所指向的url")
    text = models.TextField(default="思潮那一栏要填充的字符")
    datetime = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = u'思潮'
        verbose_name_plural = u'思潮'

    def __unicode__(self):
        return self.title


class Course(models.Model):
    course_name = models.CharField(max_length=20, verbose_name="课程")

    class Meta:
        verbose_name_plural = '课程'
        verbose_name = '课程'

    def __unicode__(self):
        return self.course_name


class CourseFile(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    file = models.FileField(upload_to='course_file', verbose_name='文档')
    file_name = models.CharField(max_length=20, verbose_name='文档名称', default='文档名称')

    class Meta:
        verbose_name = '课程文档'
        verbose_name_plural = '课程文档'

    def __unicode__(self):
        return self.file_name


class TestImage(models.Model):
    Image_x = models.ImageField(upload_to='image', blank=True, null=True)
