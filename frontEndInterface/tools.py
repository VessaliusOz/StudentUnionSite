from xxsh.settings import BASE_DIR
from datetime import datetime
import os
import random


class UploadMediaManager:

    def __init__(self):
        self.BASE_DIR = os.path.join(BASE_DIR, 'files', 'upload_media')

    def save(self, media, type):
        media_suffix = str(media).split('.')[-1]
        filename = '{0}{1}.{2}'.format(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"),
                                       str(random.randint(0, 10000)), media_suffix)
        storepath = os.path.join(BASE_DIR, 'files', 'upload_media', type, filename)
        with open(storepath, 'wb') as fp:
            fp.write(media.read())
        media_url = '/files/upload_media/%s/%s' % (type, filename)
        return media_url
