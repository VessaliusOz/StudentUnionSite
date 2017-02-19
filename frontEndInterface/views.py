# coding=utf-8生气生

from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from frontEndInterface.models import *
from django.utils import timezone
from frontEndInterface.tools import static_url_handle
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.


def index(request):
    if request.method == 'GET':
        ret_dict = {}

        # 轮播图模块
        ret_carousel_list = []
        for carousel in Carousel.objects.all():
            ele_dict = {}

            ele_dict['url'] = None
            ele_dict['image'] = static_url_handle(carousel.image.url)
            ret_carousel_list.append(ele_dict)
        ret_dict['carousel'] = ret_carousel_list

        # 校会新闻
        ret_xnews_list = []
        for xnew in X_news.objects.all().order_by('datetime')[0:8]:
            ele_dict = {}

            # 决定是不是有new这个小标签
            deltatime = datetime.now() - xnew.datetime.replace(tzinfo=None)
            if deltatime.days >= 7:
                new_flag = False
            else:
                new_flag = True
            ele_dict['newFlag'] = new_flag

            # 决定校会新闻的标题
            title = xnew.title
            ele_dict['title'] = title

            # 把东西放到list里面去
            ret_xnews_list.append(ele_dict)
        # 把list放到返回的大字典里面去
        ret_dict['xNews'] = ret_xnews_list

        # 院会新闻
        ret_snews_list = []
        for snew in S_news.objects.all().order_by('datetime')[0:8]:
            ele_dict = {}

            # 决定是不是有new这个小标签
            deltatime = datetime.now() - snew.datetime.replace(tzinfo=None)
            if deltatime.days >= 7:
                new_flag = False
            else:
                new_flag = True
            ele_dict['newFlag'] = new_flag

            title = snew.title
            ele_dict['title'] = title

            ret_xnews_list.append(ele_dict)
        ret_dict['sNews'] = ret_snews_list

        # 信息公告
        ret_info_list = []
        for info in Information.objects.all().order_by('datetime')[0:6]:
            ele_dict = {}
            deltatime = datetime.now() - info.datetime.replace(tzinfo=None)
            if deltatime.days >= 7:
                new_flag = False
            else:
                new_flag = True
            ele_dict['newFlag'] = new_flag

            title = info.title
            ele_dict['title'] = title

            ret_info_list.append(ele_dict)
        ret_dict['information'] = ret_info_list

        # 学联活动推荐
        ret_xact_list = []
        for xact in X_activity.objects.all().order_by('datetime')[0:4]:
            ele_dict = {}
            ele_dict['title'] = xact.name

            ret_xact_list.append(ele_dict)
        ret_dict['xActivity'] = ret_xact_list

        # 学术
        ret_academy_list = []
        for aca in Academy.objects.all():
            ele_dict = {}
            ele_dict['title'] = aca.title
            ele_dict['url'] = aca.url

            ret_academy_list.append(ele_dict)
        ret_dict['academy'] = ret_academy_list

        # 权益
        ret_rights_list = []
        for right in Rights.objects.all():
            ele_dict = {}
            ele_dict['title'] = right.title
            ele_dict['url'] = right.url

            ret_rights_list.append(ele_dict)

        ret_dict['rights'] = ret_rights_list

        # 思潮
        ret_thou_list = []
        for thou in Thoughts.objects.all():
            ele_dict = {}
            ele_dict['title'] = thou.title
            ele_dict['url'] = thou.url

            ret_thou_list.append(ele_dict)

        ret_dict['thoughts'] = ret_thou_list

        # xx月之星
        ret_star_list = []
        for star in Star.objects.all():
            ele_dict = {}
            ele_dict['title'] = star.content
            ele_dict['imageUrl'] = static_url_handle(star.image.url)

            ret_star_list.append(ele_dict)

        ret_dict['star'] = ret_star_list

        # 精彩视频
        ret_video_list = []
        ele_dict = {}
        ele_dict['imageUrl'] = static_url_handle(WondVideo.objects.all()[0].compress_image.url)
        ret_video_list.append(ele_dict)
        ret_dict['wonderfulVideo'] = ret_video_list

        # 精彩图片
        ret_image_list = []
        ele_dict = {}
        ele_dict['imageUrl'] = static_url_handle(WondPicture.objects.all()[0].image.url)
        ret_image_list.append(ele_dict)
        ret_dict['wonderfulImage'] = ret_image_list

        json_file = json.dumps(ret_dict, ensure_ascii=False, sort_keys=True, indent=4)
        # return JsonResponse(ret_dict)
        return HttpResponse(json_file, content_type="application/json")

    else:
        return HttpResponse('fail')


def snews(request, dynamic_news_url=None):
    if request.method == 'GET':
        if not dynamic_news_url:
            # 动态url为空的情况，赋予列表
            ret_list = []
            for new in S_news.objects.all().order_by('datetime'):
                ele_dict = {}
                ele_dict['title'] = new.title
                ele_dict['viewNum'] = new.view_num
                ele_dict['datetime'] = new.datetime.strftime(("%Y-%m-%d %H:%M"))
                ret_list.append(ele_dict)
            # json_data = json.dumps({'news': ret_list}, ensure_ascii=False, sort_keys=True, indent=4)
            return JsonResponse({'news': ret_list})
            # return HttpResponse(json_data, content_type="application/json")

        else:
            new = S_news.objects.get(title=dynamic_news_url)
            new.view_num += 1
            new.save()
            ret_dict = {}
            ret_dict['title'] = new.title
            ret_dict['body'] = new.body
            ret_dict['image'] = static_url_handle(new.image.url)
            if not new.video:
                ret_dict['video'] = new.video

            ret_dict['excEditor'] = new.exc_editor
            ret_dict['dutyEditor'] = new.duty_editor
            ret_dict['viewNum'] = new.view_num
            ret_dict['datetime'] = new.datetime
            json_file = json.dumps(ret_dict, ensure_ascii=False, sort_keys=True, indent=4)
            # return JsonResponse(ret_dict)
            return HttpResponse(json_file, content_type="application/json")
    else:
        return HttpResponse('fail, wrong request method')


def xnews(request, dynamic_news_url=None):
    if request.method == 'GET':
        if not dynamic_news_url:
            # 动态url为空的情况，赋予列表
            ret_list = []
            for new in X_news.objects.all().order_by('datetime'):
                ele_dict = {}
                ele_dict['title'] = new.title
                ele_dict['viewNum'] = new.view_num
                ele_dict['datetime'] = new.datetime.strftime(("%Y-%m-%d %H:%M"))
                ret_list.append(ele_dict)

            return JsonResponse({'news': ret_list})

        else:
            new = X_news.objects.get(title=dynamic_news_url)
            new.view_num += 1
            new.save()
            ret_dict = {}
            ret_dict['title'] = new.title
            ret_dict['body'] = new.body
            ret_dict['image'] = static_url_handle(new.image.url)
            if not new.video:
                ret_dict['video'] = new.video

            ret_dict['excEditor'] = new.exc_editor
            ret_dict['dutyEditor'] = new.duty_editor
            ret_dict['viewNum'] = new.view_num
            ret_dict['datetime'] = new.datetime

            return JsonResponse(ret_dict)
            # return HttpResponse(json_file, content_type="application/json")
    else:
        return HttpResponse('fail, wrong request method')


@csrf_exempt  # 维权
def safegaurd(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name', '')
            title = request.POST.get('title', '')
            content = request.POST.get('content', '')
            Safeguard.objects.create(name=name, title=title, content=content)
            return JsonResponse({'status': 'success'})
        except:
            return HttpResponse('参数不全')
    else:
        return HttpResponse('fail, method wrong')


# 申请表格
def apply(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name', '')
            school = request.POST.get('school', '')
            department = request.POST.get('department', '')
            introduction = request.POST.get('introduction', '')
            try:
                image = request.FILES['image']
            except:
                image = None
            Apply.objects.create(name=name, school=school, department=department, introduction=introduction,
                                 image=image)
            return JsonResponse({'status': 'success'})
        except:
            return HttpResponse('参数不全')
    else:
        return HttpResponse('fail, method wrong')


def wonder_image(request):
    if request.method == 'GET':
        ret_list = []
        video_list = []
        for img in WondPicture.objects.all().order_by('upload_time'):
            ele_dict = {}
            ele_dict['title'] = img.title
            ele_dict['imageUrl'] = static_url_handle(img.image.url)
            ret_list.append(ele_dict)
        for video in WondVideo.objects.all().order_by('upload_time'):
            video_dict = {}
            video_dict['title'] = video.title
            video_dict['compress_image'] = static_url_handle(video.compress_image.url)
            video_dict['videoUrl'] = video.video_url
            video_list.append(video_dict)
        json_data = json.dumps({'image': ret_list, 'video': video_list}, ensure_ascii=False, sort_keys=True, indent=4)
        return HttpResponse(json_data, content_type="application/json")
    else:
        return HttpResponse('fail, wrong request method')


# 外联部要站时的东西很多
def show_department(request, dynamic_dap_url=None):
    if request.method == 'GET':
        if not dynamic_dap_url:
            ret_list = []
            for department in Department.objects.all():
                dep_dict = {}
                dep_dict['name'] = department.name
                dep_dict['introduction'] = department.introduction
                ret_list.append(dep_dict)
            json_data = json.dumps({'department': ret_list}, ensure_ascii=False, sort_keys=True, indent=4)
            return HttpResponse(json_data, content_type="application/json")
        else:
            department_name = dynamic_dap_url.split('/')
            #  判断是否在查询staff url=xxx/department/xxx/
            if len(list(department_name)) == 1:
                department = Department.objects.get(name=department_name[0])
                staff_list = []
                staffs = department.staff_set.all()
                for staff in staffs:
                    sta_dict = {}
                    sta_dict['name'] = staff.name
                    sta_dict['grade'] = staff.grade
                    sta_dict['rank'] = staff.rank
                    sta_dict['introduction'] = staff.introduction
                    sta_dict['department'] = staff.department.name
                    sta_dict['chef_flag'] = staff.chef_flag
                    sta_dict['imageUrl'] = static_url_handle(staff.image.url)
                    staff_list.append(sta_dict)
                news = department.x_news_set.all()
                news_list = []
                for new in news:
                    new_dict = {}
                    new_dict['title'] = new.title
                    new_dict['viewNum'] = new.view_num
                    new_dict['datatime'] = new.datetime.strftime(("%Y-%m-%d-%H:%M"))
                    news_list.append(new_dict)
                activity_list = []
                activitys = department.x_activity_set.all()
                for activity in activitys:
                    act_dict = {}
                    act_dict['title'] = activity.name
                    activity_list.append(act_dict)
                json_data = json.dumps({'staffs': staff_list, 'news': news_list, 'activity': activity_list},
                                       ensure_ascii=False, sort_keys=True, indent=4)
                return HttpResponse(json_data, content_type="application/json")
            else:
                department = Department.objects.get(name=department_name[0])
                staff = department.staff_set.get(name=department_name[2])
                staff_dict = {}
                staff_dict['name'] = staff.name
                staff_dict['grade'] = staff.grade
                staff_dict['rank'] = staff.rank
                staff_dict['introduction'] = staff.introduction
                staff_dict['department'] = staff.department.name
                staff_dict['chef_flag'] = staff.chef_flag
                staff_dict['imageUrl'] = static_url_handle(staff.image.url)
                json_data = json.dumps(staff_dict,
                                       ensure_ascii=False, sort_keys=True, indent=4)
                return HttpResponse(json_data, content_type="application/json")
    else:
        return HttpResponse('fail, wrong request method')


# 合作交流
def show_academy(request, dynamic_news_url=None):
    academy_list = Academy.objects.all()
    if request.method == 'GET':
        if not dynamic_news_url:
            # 动态url为空的情况，赋予列表
            ret_list = []
            for new in Academy.objects.all().order_by('datetime')[0:3]:
                ele_dict = {}
                # deltatime = datetime.now() - new.datetime.replace(tzinfo=None)
                # if deltatime.days >= 7:
                #     new_flag = False
                # else:
                #     new_flag = True
                # ele_dict['newFlag'] = new_flag
                ele_dict['title'] = new.title
                ele_dict['url'] = new.url
                ele_dict['datetime'] = new.datetime.strftime(("%Y-%m-%d-%H:%M"))
                ele_dict['text'] = new.text
                ret_list.append(ele_dict)
            json_data = json.dumps({'news': ret_list}, ensure_ascii=False, sort_keys=True, indent=4)
            # return JsonResponse({'news': ret_list})
            return HttpResponse(json_data, content_type="application/json")

        else:
            return HttpResponse('wrong url')
    else:
        return HttpResponse('fail, wrong request method')


def show_rights(request, dynamic_news_url=None):
    if request.method == 'GET':
        if not dynamic_news_url:
            # 动态url为空的情况，赋予列表
            ret_list = []
            for new in Rights.objects.all().order_by('datetime')[0:3]:
                ele_dict = {}
                # deltatime = datetime.now() - new.datetime.replace(tzinfo=None)
                # if deltatime.days >= 7:
                #     new_flag = False
                # else:
                #     new_flag = True
                # ele_dict['newFlag'] = new_flag
                ele_dict['title'] = new.title
                ele_dict['url'] = new.url
                ele_dict['datetime'] = new.datetime.strftime(("%Y-%m-%d-%H:%M"))
                ele_dict['text'] = new.text
                ret_list.append(ele_dict)
            json_data = json.dumps({'news': ret_list}, ensure_ascii=False, sort_keys=True, indent=4)
            # return JsonResponse({'news': ret_list})
            return HttpResponse(json_data, content_type="application/json")

        else:
            return HttpResponse('wrong url')
    else:
        return HttpResponse('fail, wrong request method')


def show_thoughts(request, dynamic_news_url=None):
    if request.method == 'GET':
        if not dynamic_news_url:
            # 动态url为空的情况，赋予列表
            ret_list = []
            for new in Thoughts.objects.all().order_by('datetime')[0:3]:
                ele_dict = {}
                # deltatime = datetime.now() - new.datetime.replace(tzinfo=None)
                # if deltatime.days >= 7:
                #     new_flag = False
                # else:
                #     new_flag = True
                # ele_dict['newFlag'] = new_flag
                ele_dict['title'] = new.title
                ele_dict['url'] = new.url
                ele_dict['datetime'] = new.datetime.strftime(("%Y-%m-%d-%H:%M"))
                ele_dict['text'] = new.text
                ret_list.append(ele_dict)
            json_data = json.dumps({'news': ret_list}, ensure_ascii=False, sort_keys=True, indent=4)
            # return JsonResponse({'news': ret_list})
            return HttpResponse(json_data, content_type="application/json")

        else:
            return HttpResponse('wrong url')
    else:
        return HttpResponse('fail, wrong request method')


def show_stars(request, dynamic_url=None):
    if request.method == 'GET':
        if not dynamic_url:
            # 动态url为空的情况，赋予列表
            ret_list = []
            for new in Star.objects.all()[0:3]:
                ele_dict = {}
                # deltatime = datetime.now() - new.datetime.replace(tzinfo=None)
                # if deltatime.days >= 7:
                #     new_flag = False
                # else:
                #     new_flag = True
                # ele_dict['newFlag'] = new_flag
                ele_dict['content'] = new.content
                ele_dict['url'] = static_url_handle(new.image.url)
                ele_dict['text'] = new.text
                ret_list.append(ele_dict)
            json_data = json.dumps({'star': ret_list}, ensure_ascii=False, sort_keys=True, indent=4)
            # return JsonResponse({'news': ret_list})
            return HttpResponse(json_data, content_type="application/json")

        else:
            ret_dict = {}
            star = Star.objects.get(content=dynamic_url)
            ret_dict['content'] = star.content
            ret_dict['image'] = static_url_handle(star.image.url)
            ret_dict['text'] = star.text
            json_file = json.dumps(ret_dict, ensure_ascii=False, sort_keys=True, indent=4)
            # return JsonResponse(ret_dict)
            return HttpResponse(json_file, content_type="application/json")
    else:
        return HttpResponse('fail, wrong request method')


        # class Star(models.Model):  # 某月之星
        #     content = models.CharField(max_length=200)
        #     image = models.ImageField(upload_to='static/xxsh/star', default=None)
        #
        #     def __unicode__(self):
        #         return self.content


def show_structure(request):
    pass