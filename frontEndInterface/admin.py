import xadmin
from models import *


class EditorXAdmin(object):

    def get_media(self):
        media = super(EditorXAdmin, self).get_media()
        media.add_js((
            'js/editor/kindeditor/kindeditor-all-min.js',
            'js/editor/kindeditor/lang/zh_CN.js',
            'js/editor/kindeditor/config.js',
        ))
        return media


xadmin.site.register(WpPosts, EditorXAdmin)
xadmin.site.register(Department)
xadmin.site.register(Staff)
xadmin.site.register(X_news)
xadmin.site.register(X_activity)
xadmin.site.register(Information)
xadmin.site.register(Carousel)
xadmin.site.register(Apply)
xadmin.site.register(Safeguard)
xadmin.site.register(FixServer)
xadmin.site.register(School)
xadmin.site.register(S_news)
xadmin.site.register(SomeElse)
xadmin.site.register(Star)
xadmin.site.register(WondVideo)
xadmin.site.register(WondPicture)
xadmin.site.register(Academy)
xadmin.site.register(Rights)
xadmin.site.register(Thoughts)
xadmin.site.register(Chef)
xadmin.site.register(Course)
xadmin.site.register(CourseFile)
xadmin.site.register(TestImage)
