# encoding:utf8
"""
    BaseCustomAdmin为自定义基类,其复写了get_media方法以在xadmin后台页面的Textarea中插入必须的js文件,
    其他Admin类若有将普通Textarea组件改变为kindeditor编辑器的需求,则继承该BaseCustomAdmin类:

    class AuthorAdmin(BaseCustomAdmin):
        pass

    若没有将普通Textarea组件改变为kindeditor编辑器的需求,则继承默认的object类:

    class AuthorAdmin(object):
        pass
"""
import xadmin
from xadmin.views import CommAdminView, ModelAdminView
from .models import *


class BaseCustomAdmin(object):

    def get_media(self):
        """
        :return: media
        :description: 为弥补xadmin中不支持class Media指定js文件插入的缺陷,
                      此处复写父类get_media方法,将xadmin默认引入文件与自定义
                      js文件(通过media.add_js添加)一起引入管理后台页面.
        """
        media = super(BaseCustomAdmin, self).get_media()
        media.add_js((
            'js/editor/kindeditor-4.1.12/kindeditor-all.js',
            'js/editor/kindeditor-4.1.12/lang/zh-CN.js',
            'js/editor/kindeditor-4.1.12/config.js',
        ))
        return media


class GlobalSetting(object):
    site_title = '校学生会管理系统'
    site_footer = 'IEC'


class WpPostsAdmin(BaseCustomAdmin):
    pass


class DepartmentAdmin(BaseCustomAdmin):
    pass


class StaffAdmin(BaseCustomAdmin):
    pass


class X_newsAdmin(BaseCustomAdmin):
    pass


class X_activityAdmin(BaseCustomAdmin):
    pass


class InformationAdmin(BaseCustomAdmin):
    pass


class CarouselAdmin(BaseCustomAdmin):
    pass


class ApplyAdmin(BaseCustomAdmin):
    pass


class SafeguardAdmin(BaseCustomAdmin):
    pass


class FixServerAdmin(BaseCustomAdmin):
    pass


class SchoolAdmin(BaseCustomAdmin):
    pass


class S_newsAdmin(BaseCustomAdmin):
    pass


class SomeElseAdmin(BaseCustomAdmin):
    pass


class StarAdmin(BaseCustomAdmin):
    pass


class WondVideoAdmin(BaseCustomAdmin):
    pass


class WondPictureAdmin(BaseCustomAdmin):
    pass


class AcademyAdmin(BaseCustomAdmin):
    pass


class RightsAdmin(BaseCustomAdmin):
    pass


class ThoughtsAdmin(BaseCustomAdmin):
    pass


class ChefAdmin(BaseCustomAdmin):
    pass


class CourseAdmin(BaseCustomAdmin):
    pass


class CourseFileAdmin(BaseCustomAdmin):
    pass


class BusinessCooperationAdmin(BaseCustomAdmin):
    pass


class ForeignContactAdmin(BaseCustomAdmin):
    pass


class CourseInformationAdmin(BaseCustomAdmin):
    pass


class suChefAdmin(BaseCustomAdmin):
    pass

class suStaffAdmin(BaseCustomAdmin):
    pass

class suPhotoAdmin(BaseCustomAdmin):
    pass

class SchoolUnionAdmin(BaseCustomAdmin):
    pass

xadmin.site.register(WpPosts, WpPostsAdmin)
xadmin.site.register(Carousel, CarouselAdmin)
xadmin.site.register(SchoolUnion, SchoolUnionAdmin)
xadmin.site.register(suChef, suChefAdmin)
xadmin.site.register(suStaff, suStaffAdmin)
xadmin.site.register(suPhoto, suPhotoAdmin)
xadmin.site.register(Department, DepartmentAdmin)
xadmin.site.register(Chef, ChefAdmin)
xadmin.site.register(Staff, StaffAdmin)
xadmin.site.register(X_news, X_newsAdmin)
xadmin.site.register(X_activity, X_activityAdmin)
xadmin.site.register(Information, InformationAdmin)
xadmin.site.register(School, SchoolAdmin)
xadmin.site.register(S_news, S_newsAdmin)
xadmin.site.register(SomeElse, SomeElseAdmin)
xadmin.site.register(Apply, ApplyAdmin)
xadmin.site.register(Safeguard, SafeguardAdmin)
xadmin.site.register(FixServer, FixServerAdmin)
xadmin.site.register(Star, StarAdmin)
xadmin.site.register(WondVideo, WondVideoAdmin)
xadmin.site.register(WondPicture, WondPictureAdmin)
xadmin.site.register(Academy, AcademyAdmin)
xadmin.site.register(Rights, RightsAdmin)
xadmin.site.register(Thoughts, ThoughtsAdmin)
xadmin.site.register(CourseInformation, CourseInformationAdmin)
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(CourseFile, CourseFileAdmin)
xadmin.site.register(BusinessCooperation, BusinessCooperationAdmin)
xadmin.site.register(ForeignContact, ForeignContactAdmin)
xadmin.site.register(CommAdminView, GlobalSetting)

