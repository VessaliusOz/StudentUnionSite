
# encoding:utf8
import xadmin
from xadmin.views import CommAdminView, ModelAdminView
from models import *


class GlobalSetting(object):
    site_title = '校学生会管理系统'
    site_footer = 'IEC'


class EditorXAdmin(object):

    def get_media(self):
        media = super(EditorXAdmin, self).get_media()
        media.add_js((
            'js/editor/kindeditor/kindeditor-all-min.js',
            'js/editor/kindeditor/lang/zh_CN.js',
            'js/editor/kindeditor/config.js',
        ))
        return media


class DepartmentModelAdmin(ModelAdminView):
    model = Staff
    pass

xadmin.site.register(CommAdminView, GlobalSetting)
xadmin.site.register(WpPosts, EditorXAdmin)
xadmin.site.register(Department)
xadmin.site.register(Staff)
xadmin.site.register(X_news)
xadmin.site.register(X_activity)
xadmin.site.register(Information)
xadmin.site.register(Carousel)
xadmin.site.register(School)
xadmin.site.register(S_news)
xadmin.site.register(SomeElse)
xadmin.site.register(Chef)
xadmin.site.register(Star)
xadmin.site.register(WondVideo)
xadmin.site.register(WondPicture)
xadmin.site.register(Academy)
xadmin.site.register(Rights)
xadmin.site.register(Thoughts)
xadmin.site.register(BusinessCooperation)
xadmin.site.register(ForeignContact)
xadmin.site.register(Course)
xadmin.site.register(CourseFile)
xadmin.site.register(CourseInformation)
xadmin.site.register(Apply)
xadmin.site.register(Safeguard)
xadmin.site.register(FixServer)
