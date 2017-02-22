"""xxsh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, handler404, handler500
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from frontEndInterface.views import *
import xadmin
xadmin.autodiscover()

urlpatterns = [
    url(r'xadmin/', include(xadmin.site.urls)),
    url(r'admin/', include(admin.site.urls)),
    url(r'index/$', index, name='index'),
    url(r'xnews/(.*)', xnews, name='xnews'),
    url(r'snews/(.*)', snews, name='snews'),
    url(r'information/(.*)', show_information, name='show_information'),
    url(r'safegaurd/', safegaurd, name='safegaurd'),
    url(r'apply/', apply, name='apply'),
    url(r'fixserver/', fix_server, name='fix_server'),
    url(r'pic/', wonder_image, name='wonder_image'),
    url(r'^department/(.*)', show_department, name='department'),
    url(r'departmentframework/', show_framework, name='show_framework'),
    url(r'images/', wonder_image),
    url(r'videos/', wonder_image),
    url(r'academy/(.*)', show_academy),
    url(r'rights/(.*)', show_rights),
    url(r'thoughts/(.*)', show_thoughts),
    url(r'stars/(.*)', show_stars),
    url(r'schools/(.*)', show_schools),
    url(r'course/', show_course),
    url(r'upload_media/$', upload_media),
    url(r'get_test_data/$', get_test_data),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
