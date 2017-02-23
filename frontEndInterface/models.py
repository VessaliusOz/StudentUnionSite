# coding=utf-8
from django.db import models
from django.utils.datetime_safe import datetime


class SchoolUnion(models.Model):
    Text = models.TextField(default='学联简介，组织架构，历史', verbose_name='学生联合会')

    class Meta:
        verbose_name = '学生联合会'
        verbose_name_plural = '学生联合会'

    def __unicode__(self):
        return "学生联合会"


class suChef(models.Model):
    name = models.CharField(max_length=20, default='主席', verbose_name='主席')
    if_chef_now = models.BooleanField(default=False, verbose_name='是否在任')
    introduction = models.TextField(default='introduction', verbose_name='介绍')
    # image = models.ImageField(upload_to='chef', default=None, null=True, verbose_name='图片')
    grade = models.CharField(max_length=20, default='', verbose_name='年级')
    datetime = models.DateTimeField(default=datetime.now(), verbose_name='上任时间(排序用)')
    telephone = models.CharField(max_length=30, default='电话号码', verbose_name='电话号码', blank=True)
    e_mail = models.CharField(max_length=30, default='Email', verbose_name='Email', blank=True)
    school = models.ForeignKey(SchoolUnion, verbose_name="学生联合会")

    class Meta:
        verbose_name_plural = '主席'
        verbose_name = '主席'

    def __unicode__(self):
        return self.name


class suStaff(models.Model):
    name = models.CharField(max_length=20, default='骨干', verbose_name='姓名', unique=True)
    grade = models.CharField(max_length=20, default='', verbose_name='年级')  # 大几
    rank = models.CharField(max_length=20, default='', verbose_name='职务')
    introduction = models.TextField(verbose_name='介绍', default='introduction')
    telephone = models.CharField(max_length=30, default='电话号码', verbose_name='电话号码')
    e_mail = models.CharField(max_length=30, default='Email', verbose_name='Email')
    school = models.ForeignKey(SchoolUnion, verbose_name="学生联合会")

    class Meta:
        verbose_name = '骨干'
        verbose_name_plural = '骨干'

    def __unicode__(self):
        return self.name


# class suPhoto(models.Model):
#     shcool = models.ForeignKey(SchoolUnion, verbose_name="学生联合会历史图片")
#     photo = models.TextField(verbose_name="历史照片")
#
class suPhoto(models.Model):
    school = models.OneToOneField(SchoolUnion, verbose_name="学生联合会")
    photo = models.TextField(verbose_name="历史照片")

    class Meta:
        verbose_name = "历史照片"
        verbose_name_plural = "历史照片"

    def __unicode__(self):
        return "历史照片"


class Department(models.Model):
    name = models.CharField(max_length=20, default='部门的名字', verbose_name='名称',unique=True)
    introduction = models.TextField(default='这是简介', verbose_name='介绍')
    image = models.ImageField(upload_to='department', default=None, null=True, verbose_name='视频缩略图')
    video_url = models.CharField(max_length=200, default='视频链接', blank=True, verbose_name='视频链接')

    class Meta:
        verbose_name = u'部门'
        verbose_name_plural = u'部门'

    def __unicode__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=20, default='组员名字', verbose_name='姓名', unique=True)
    grade = models.CharField(max_length=20, default='', verbose_name='年级')  # 大几
    rank = models.CharField(max_length=20, default='', verbose_name='职务')
    introduction = models.TextField(verbose_name='介绍')
    #  image = models.ImageField(upload_to='staff', verbose_name='图片')
    department = models.ForeignKey(Department, verbose_name='部门')
    chef_flag = models.BooleanField(default=False, verbose_name='是否为骨干')  # 是否是骨干
    telephone = models.CharField(max_length=30, default='电话号码', verbose_name='电话号码')
    e_mail = models.CharField(max_length=30, default='Email', verbose_name='Email')

    class Meta:
        verbose_name = u'人员'
        verbose_name_plural = u'人员'

    def __unicode__(self):
        return self.name


#  顺序没有写。。。。
class Chef(models.Model):
    name = models.CharField(max_length=20, default='部长的名字', verbose_name='部长')
    if_chef_now = models.BooleanField(default=False, verbose_name='是否在任')
    introduction = models.TextField(default='introduction', verbose_name='介绍')
    # image = models.ImageField(upload_to='chef', default=None, null=True, verbose_name='图片')
    grade = models.CharField(max_length=20, default='', verbose_name='年级')
    department = models.ForeignKey(Department, verbose_name='部门')
    datetime = models.DateTimeField(default=datetime.now(), verbose_name='上任时间(排序用)')
    telephone = models.CharField(max_length=30, default='电话号码', verbose_name='电话号码', blank=True)
    e_mail = models.CharField(max_length=30, default='Email', verbose_name='Email', blank=True)

    class Meta:
        verbose_name = u'部长'
        verbose_name_plural = u'部长'

    def __unicode__(self):
        return self.name


class X_news(models.Model):
    '''校学生会的新闻'''
    title = models.CharField(max_length=100, verbose_name='标题', default='标题', unique=True)
    body = models.TextField(verbose_name='内容')
    image = models.ImageField(upload_to='xnews', verbose_name='视频缩略图')
    video = models.CharField(max_length=200, blank=True, verbose_name='视频链接')
    exc_editor = models.CharField(max_length=20, default='本新闻执行编辑', verbose_name='执行编辑')
    duty_editor = models.CharField(max_length=20, default='本新闻责任编辑', verbose_name='责任编辑')
    view_num = models.IntegerField(default=0, verbose_name='浏览次数')
    datetime = models.DateTimeField(default=datetime.now(),verbose_name='创建时间')
    department = models.ForeignKey(Department, verbose_name='部门')
    file = models.FileField(upload_to='xnews/files', default=None, null=True, blank=True, verbose_name='附件')

    class Meta:
        verbose_name = u'校学生会新闻'
        verbose_name_plural = u'校学生会新闻'

    def __unicode__(self):
        return self.title


class X_activity(models.Model):
    name = models.CharField(max_length=100, verbose_name='活动', unique=True)
    body = models.TextField(verbose_name='内容')
    image = models.ImageField(upload_to='activity', verbose_name='视频缩略图')
    video = models.CharField(max_length=200, blank=True, verbose_name='视频链接',default='视频链接')
    sponsor = models.CharField(max_length=20, verbose_name='赞助商')
    datetime = models.DateTimeField(default=datetime.now(),verbose_name='创建时间')
    department = models.ForeignKey(Department, verbose_name='部门')
    file = models.FileField(upload_to='xnews/files', default=None, null=True, blank=True, verbose_name='附件')

    class Meta:
        verbose_name = u'校学生会活动'
        verbose_name_plural = u'校学生会活动'

    def __unicode__(self):
        return self.department.name + "的" + self.name + "活动"


########################################################################
########################################################################

class School(models.Model):
    ''' 学院的学生会 '''
    name = models.CharField(max_length=100, verbose_name='院会名称')
    introduction = models.TextField(verbose_name='介绍')
    chef = models.CharField(max_length=20, verbose_name='主席')
    chef_introduction = models.TextField(verbose_name='主席介绍')
    video_url = models.CharField(max_length=200, default='视频链接', blank=True, verbose_name='视频链接')

    class Meta:
        verbose_name = u'院学生会'
        verbose_name_plural = u'院学生会'

    def __unicode__(self):
        return self.name


class S_news(models.Model):  # 院会的新闻
    title = models.CharField(max_length=100, verbose_name='标题', default='标题', unique=True)
    body = models.TextField(verbose_name='内容')
    image = models.ImageField(upload_to='snews', verbose_name='视频缩略图')
    video = models.CharField(max_length=200, blank=True, verbose_name='视频链接')
    exc_editor = models.CharField(max_length=20, default='本新闻执行编辑', verbose_name='执行编辑')
    duty_editor = models.CharField(max_length=20, default='本新闻责任编辑', verbose_name='责任编辑')
    view_num = models.IntegerField(default=0, verbose_name='浏览次数')
    datetime = models.DateTimeField(default=datetime.now(), verbose_name='时间')
    school = models.ForeignKey(School, verbose_name='院会')
    file = models.FileField(upload_to='snews/files', default=None, null=True, blank=True, verbose_name='附件')

    class Meta:
        verbose_name = u'院会新闻'
        verbose_name_plural = u'院会新闻'

    def __unicode__(self):
        return self.title


########################################################################
########################################################################


class Information(models.Model):
    datetime = models.DateTimeField(default=datetime.now(), verbose_name='时间')
    view_num = models.IntegerField(default=0, verbose_name='浏览数')
    title = models.CharField(max_length=100, verbose_name='标题', default='标题', unique=True)
    image = models.ImageField(upload_to='information', default=None, blank=True, null=True, verbose_name='视频缩略图')
    body = models.TextField(verbose_name='内容')
    exc_editor = models.CharField(max_length=20, default='本公告执行编辑', verbose_name='执行编辑')
    duty_editor = models.CharField(max_length=20, default='本公告责任编辑', verbose_name='责任编辑')
    video_url = models.CharField(max_length=200, default='视频链接', blank=True, verbose_name='视频链接')
    file = models.FileField(upload_to='information/files', default=None, null=True, blank=True, verbose_name='附件')

    class Meta:
        verbose_name = u'公告'
        verbose_name_plural = u'公告'

    def __unicode__(self):
        return self.title


class BusinessCooperation(models.Model):
    datetime = models.DateTimeField(default=datetime.now(), verbose_name='时间')
    view_num = models.IntegerField(default=0, verbose_name='浏览数')
    title = models.CharField(max_length=100, verbose_name='标题', default='标题', unique=True)
    image = models.ImageField(upload_to='Business', default=None, blank=True, null=True, verbose_name='视频缩略图')
    body = models.TextField(verbose_name='内容')
    exc_editor = models.CharField(max_length=20, default='本公告执行编辑', verbose_name='执行编辑')
    duty_editor = models.CharField(max_length=20, default='本公告责任编辑', verbose_name='责任编辑')
    video_url = models.CharField(max_length=200, default='视频链接', blank=True, verbose_name='视频链接')
    file = models.FileField(upload_to='Business/files', default=None, null=True, blank=True, verbose_name='附件')

    class Meta:
        verbose_name = u'商业合作'
        verbose_name_plural = u'商业合作'

    def __unicode__(self):
        return self.title


class ForeignContact(models.Model):
    datetime = models.DateTimeField(default=datetime.now(), verbose_name='时间')
    view_num = models.IntegerField(default=0, verbose_name='浏览数')
    title = models.CharField(max_length=100, verbose_name='标题', default='标题', unique=True)
    image = models.ImageField(upload_to='ForeignContact', default=None, blank=True, null=True, verbose_name='视频缩略图')
    body = models.TextField(verbose_name='内容')
    exc_editor = models.CharField(max_length=20, default='本公告执行编辑', verbose_name='执行编辑')
    duty_editor = models.CharField(max_length=20, default='本公告责任编辑', verbose_name='责任编辑')
    video_url = models.CharField(max_length=200, default='视频链接', blank=True, verbose_name='视频链接')
    file = models.FileField(upload_to='ForeignContact/files', default=None, null=True, blank=True, verbose_name='附件')

    class Meta:
        verbose_name = u'外事联络'
        verbose_name_plural = u'外事联络'

    def __unicode__(self):
        return self.title


class Notice(models.Model):
    datetime = models.DateTimeField(default=datetime.now(), verbose_name='')
    title = models.CharField(max_length=100, verbose_name='')
    image = models.ImageField(upload_to='information', default=None, verbose_name='')
    body = models.TextField(verbose_name='')
    exc_editor = models.CharField(max_length=20, default='本公告执行编辑', verbose_name='')
    duty_editor = models.CharField(max_length=20, default='本公告责任编辑', verbose_name='')

    def __unicode__(self):
        return self.title


class Carousel(models.Model):  # Carousel是轮播器的意思
    image = models.ImageField(upload_to='carousel', default=None, verbose_name='图片')
    url = models.CharField(max_length=100, verbose_name='链接')
    title = models.CharField(max_length=100, verbose_name='标题')
    content = models.CharField(max_length=200, verbose_name='内容')

    class Meta:
        verbose_name = u'轮播器'
        verbose_name_plural = u'轮播器'

    def __unicode__(self):
        return self.title


class Apply(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    school = models.CharField(max_length=100, verbose_name='学院', blank=True, null=True, default=None)
    department = models.CharField(max_length=100, verbose_name='部门')
    introduction = models.TextField(verbose_name='自我介绍')
    image = models.ImageField(upload_to='apply', blank=True, verbose_name='图片')
    datetime = models.DateTimeField(default=datetime.now(), verbose_name='申请时间')

    class Meta:
        verbose_name = u'申请'
        verbose_name_plural = u'申请'

    def __unicode__(self):
        return self.name


class FixServer(models.Model):
    name = models.CharField(max_length=100, default=None, null=True, blank=True, verbose_name='名字')
    title = models.CharField(max_length=100, default=None,null=True, blank=True, verbose_name='标题')
    text = models.TextField(default=None, null=True, verbose_name='内容')
    image = models.ImageField(upload_to='fixServer', default=None, blank=True, null=True, verbose_name='图片')
    datetime = models.DateTimeField(default=datetime.now(), verbose_name='时间')

    class Meta:
        verbose_name = u'后勤报修'
        verbose_name_plural = u'后勤报修'

    def __unicode__(self):
        return self.name


class Safeguard(models.Model):
    name = models.CharField(max_length=20, default='维权者名字', verbose_name='名字')
    title = models.CharField(max_length=200, default='维权主题', verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    datetime = models.DateTimeField(default=datetime.now(), verbose_name='时间')

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
                                                  default=None, null=True, blank=True, verbose_name='院会体系视频缩略图')
    school_system_brief_text = models.TextField(default=None, null=True, blank=True, verbose_name='院会体系内容')
    school_system_brief_video = models.CharField(max_length=200, default='视频连接', blank=True, verbose_name='院会体系视频')
    organization_framework_text = models.TextField(default=None, null=True, blank=True, verbose_name='组织架构内容')
    organization_framework_image = models.ImageField(upload_to='organizatin_framework',
                                                  default=None, null=True, blank=True, verbose_name='组织架构视频缩略图')
    organization_framework_video = models.CharField(max_length=200, default='视频连接', blank=True, verbose_name='组织架构视频')

    class Meta:
        verbose_name = u'院会体系/校学生会组织架构'
        verbose_name_plural = u'院会体系/校学生会组织架构'

    def __unicode__(self):
        return '院会体系/校学生会组织架构'


class Star(models.Model):  # 某月之星
    content = models.CharField(max_length=200, verbose_name='主题')
    image = models.ImageField(upload_to='star', default=None, verbose_name='图片')
    text = models.TextField(default='', verbose_name='内容')

    class Meta:
        verbose_name = u'某月之星'
        verbose_name_plural = u'某月之星'


    def __unicode__(self):
        return self.content


class WondVideo(models.Model):
    title = models.CharField(max_length=100, default="视频的标题", verbose_name='标题')
    compress_image = models.ImageField(upload_to='wonderful_video', default=None, verbose_name='缩略图')
    upload_time = models.DateTimeField(default=datetime.now(), verbose_name='上传时间')
    video_url = models.CharField(max_length=200, verbose_name='视频链接')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = u'视频'

    def __unicode__(self):
        return self.title


class WondPicture(models.Model):
    title = models.CharField(max_length=100, default="图片的标题，不要超过100个字", verbose_name='标题')
    upload_time = models.DateTimeField(default=datetime.now(), verbose_name='上传时间')
    image = models.ImageField(upload_to='wonderful_picture', verbose_name='图片')

    class Meta:
        verbose_name = u'图片'
        verbose_name_plural = u'图片'

    class Meta:
        verbose_name = u'图片'
        verbose_name_plural = u'图片'

    def __unicode__(self):
        return self.title


class Academy(models.Model):
    title = models.CharField(max_length=100, default="学术那一栏要填充的字符", verbose_name='标题', unique=True)
    url = models.CharField(max_length=200, default="这个学术所指向的url", verbose_name='链接')
    text = models.TextField(default="学术那一栏要填充的字符", verbose_name='内容')
    datetime = models.DateTimeField(default=datetime.now(), verbose_name='创建时间')

    class Meta:
        verbose_name = u'学术'
        verbose_name_plural = u'学术'

    def __unicode__(self):
        return self.title


class Rights(models.Model):
    title = models.CharField(max_length=100, default="权益那一栏要填充的字符", verbose_name='标题', unique=True)
    url = models.CharField(max_length=200, default="这个权益字段所指向的url", verbose_name='链接')
    text = models.TextField(default="权益那一栏要填充的字符", verbose_name='内容')
    datetime = models.DateTimeField(default=datetime.now(), verbose_name='创建时间')

    class Meta:
        verbose_name = u'权益'
        verbose_name_plural = u'权益'

    def __unicode__(self):
        return self.title


class Thoughts(models.Model):
    title = models.CharField(max_length=100, default="思潮那一栏要填充的字符", verbose_name='标题', unique=True)
    url = models.CharField(max_length=200, default="这个思潮字段所指向的url", verbose_name='链接')
    text = models.TextField(default="思潮那一栏要填充的字符", verbose_name='内容')
    datetime = models.DateTimeField(default=datetime.now(), verbose_name='创建时间')

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


class CourseInformation(models.Model):
    datetime = models.DateTimeField(default=datetime.now(), verbose_name='时间')
    view_num = models.IntegerField(default=0, verbose_name='浏览数')
    title = models.CharField(max_length=100, verbose_name='标题', default='标题', unique=True)
    image = models.ImageField(upload_to='CourseInformation', blank=True, default=None, null=True, verbose_name='视频缩略图')
    body = models.TextField(verbose_name='内容')
    exc_editor = models.CharField(max_length=20, default='本公告执行编辑', verbose_name='执行编辑')
    duty_editor = models.CharField(max_length=20, default='本公告责任编辑', verbose_name='责任编辑')
    file = models.FileField(upload_to='information/files', blank=True, default=None, null=True, verbose_name='附件')

    class Meta:
        verbose_name_plural = '学习信息'
        verbose_name = '学习信息'

    def __unicode__(self):
        return self.title


class CourseFile(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    file = models.FileField(upload_to='course_file', verbose_name='文档')
    file_name = models.CharField(max_length=20, verbose_name='文档名称', default='文档名称', unique=True)

    class Meta:
        verbose_name = '课程文档'
        verbose_name_plural = '课程文档'

    def __unicode__(self):
        return self.file_name


class WpPosts(models.Model):
    post_title = models.CharField(max_length=100, default='')
    post_content = models.TextField(blank=True)

    class Meta:
        verbose_name = u'富文本(测试)'
        verbose_name_plural = u'富文本(测试)'

    def __str__(self):
        return u'富文本测试: ' + self.post_title
