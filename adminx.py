from rte.widgets import Ueditor
from django.core.files.storage import FileSystemStorage
import os
from xxsh import settings

class SomeElseAdmin(object):
    style_fields = {"school_system_brief_text": 'ueditor'}
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'upload'))
    def get_field_style(self, db_field, style, **kwargs):

        if style in ('ueditor',):
            attrs = {'widget': Ueditor}
            return attrs