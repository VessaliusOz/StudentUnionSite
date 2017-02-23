# coding=utf-8
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from .models import *
import json


def index(request):
    if request.method == 'GET':
        ret_dict = {}

        # 轮播图模块
        ret_carousel_list = []
        for carousel in Carousel.objects.all():
            ele_dict = {}

            ele_dict['url'] = None
            ele_dict['image'] = carousel.image.url
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
            if len(ret_xnews_list) == 8:
                break
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

            ret_snews_list.append(ele_dict)
            if len(ret_snews_list) == 8:
                break

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
            if len(ret_info_list) == 8:
                break
        ret_dict['information'] = ret_info_list

        # 学联活动推荐
        ret_xact_list = []
        for xact in X_activity.objects.all().order_by('datetime')[0:4]:
            ele_dict = {}
            ele_dict['title'] = xact.name
            ele_dict['url'] = xact.image.url

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
            ele_dict['imageUrl'] = star.image.url

            ret_star_list.append(ele_dict)

        ret_dict['star'] = ret_star_list

        # 精彩视频
        ret_video_list = []
        ele_dict = {}
        ele_dict['imageUrl'] = WondVideo.objects.all()[0].compress_image.url
        ret_video_list.append(ele_dict)
        ret_dict['wonderfulVideo'] = ret_video_list

        # 精彩图片
        ret_image_list = []
        ele_dict = {}
        ele_dict['imageUrl'] = WondPicture.objects.all()[0].image.url
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
            json_data = json.dumps({'news': ret_list}, ensure_ascii=False, sort_keys=True, indent=4)
            # return JsonResponse({'news': ret_list})
            return HttpResponse(json_data, content_type="application/json")

        else:
            new = S_news.objects.get(title=dynamic_news_url)
            new.view_num += 1
            new.save()
            ret_dict = {}
            ret_dict['title'] = new.title
            ret_dict['body'] = new.body

            if new.image.url:
                ret_dict['image'] = new.image.url

            if not new.video:
                ret_dict['video'] = new.video

            ret_dict['excEditor'] = new.exc_editor
            ret_dict['dutyEditor'] = new.duty_editor
            ret_dict['viewNum'] = new.view_num
            ret_dict['datetime'] = new.datetime.strftime(("%Y-%m-%d %H:%M"))
            if new.file:
                ret_dict['attachmentUrl'] = new.file.url
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
            json_data = json.dumps({'news': ret_list}, ensure_ascii=False, sort_keys=True, indent=4)
            # return JsonResponse({'news': ret_list})
            return HttpResponse(json_data, content_type="application/json")

        else:
            new = X_news.objects.get(title=dynamic_news_url)
            new.view_num += 1
            new.save()
            ret_dict = {}
            ret_dict['title'] = new.title
            ret_dict['body'] = new.body

            if new.image.url:
                ret_dict['image'] = new.image.url

            if not new.video:
                ret_dict['video'] = new.video

            ret_dict['excEditor'] = new.exc_editor
            ret_dict['dutyEditor'] = new.duty_editor
            ret_dict['viewNum'] = new.view_num
            ret_dict['datetime'] = new.datetime.strftime(("%Y-%m-%d %H:%M"))
            if new.file:
                ret_dict['attachmentUrl'] = new.file.url
            json_data = json.dumps(ret_dict, ensure_ascii=False, sort_keys=True, indent=4)
            # return JsonResponse(ret_dict)
            return HttpResponse(json_data, content_type="application/json")
    else:
        return HttpResponse('fail, wrong request method')


def show_information(request, dynamic_news_url=None):
    if request.method == 'GET':
        if not dynamic_news_url:
            # 动态url为空的情况，赋予列表
            ret_list = []
            for notice in Information.objects.all().order_by('datetime'):
                ele_dict = {}
                ele_dict['title'] = notice.title
                ele_dict['datetime'] = notice.datetime.strftime(("%Y-%m-%d %H:%M"))
                ret_list.append(ele_dict)
            json_data = json.dumps({'information': ret_list}, ensure_ascii=False, sort_keys=True, indent=4)
            # return JsonResponse({'information': ret_list})
            return HttpResponse(json_data, content_type="application/json")

        else:
            notice = Information.objects.get(title=dynamic_news_url)
            notice.view_num += 1
            notice.save()
            ret_dict = {}
            ret_dict['title'] = notice.title
            ret_dict['body'] = notice.body
            if notice.image.url:
                ret_dict['image'] = notice.image.url

            ret_dict['excEditor'] = notice.exc_editor
            ret_dict['dutyEditor'] = notice.duty_editor
            ret_dict['viewNum'] = notice.view_num
            if notice.file:
                ret_dict['attachmentUrl'] = notice.file.url
            ret_dict['datetime'] = notice.datetime.strftime(("%Y-%m-%d %H:%M"))
            json_file = json.dumps(ret_dict, ensure_ascii=False, sort_keys=True, indent=4)
            # return JsonResponse(ret_dict)
            return HttpResponse(json_file, content_type="application/json")
    else:
        return HttpResponse('fail, wrong request method')


def show_business(request, dynamic_news_url=None):
    if request.method == 'GET':
        if not dynamic_news_url:
            # 动态url为空的情况，赋予列表
            ret_list = []
            for new in BusinessCooperation.objects.all().order_by('datetime'):
                ele_dict = {}
                ele_dict['title'] = new.title
                ele_dict['viewNum'] = new.view_num
                ele_dict['datetime'] = new.datetime.strftime(("%Y-%m-%d %H:%M"))
                ret_list.append(ele_dict)
            # json_data = json.dumps({'news': ret_list}, ensure_ascii=False, sort_keys=True, indent=4)
            return JsonResponse({'business': ret_list})
            # return HttpResponse(json_data, content_type="application/json")

        else:
            new = BusinessCooperation.objects.get(title=dynamic_news_url)
            new.view_num += 1
            new.save()
            ret_dict = {}
            ret_dict['title'] = new.title
            ret_dict['body'] = new.body
            if new.image.url:
                ret_dict['image'] = new.image.url
            ret_dict['excEditor'] = new.exc_editor
            ret_dict['dutyEditor'] = new.duty_editor
            ret_dict['viewNum'] = new.view_num
            ret_dict['datetime'] = new.datetime.strftime(("%Y-%m-%d %H:%M"))
            if new.file:
                ret_dict['attachmentUrl'] = new.file.url
            json_file = json.dumps(ret_dict, ensure_ascii=False, sort_keys=True, indent=4)
            # return JsonResponse(ret_dict)
            return HttpResponse(json_file, content_type="application/json")
    else:
        return HttpResponse('fail, wrong request method')


def show_contact(request, dynamic_news_url=None):
    if request.method == 'GET':
        if not dynamic_news_url:
            # 动态url为空的情况，赋予列表
            ret_list = []
            for new in ForeignContact.objects.all().order_by('datetime'):
                ele_dict = {}
                ele_dict['title'] = new.title
                ele_dict['viewNum'] = new.view_num
                ele_dict['datetime'] = new.datetime.strftime(("%Y-%m-%d %H:%M"))
                ret_list.append(ele_dict)
            # json_data = json.dumps({'news': ret_list}, ensure_ascii=False, sort_keys=True, indent=4)
            return JsonResponse({'contact': ret_list})
            # return HttpResponse(json_data, content_type="application/json")

        else:
            new = ForeignContact.objects.get(title=dynamic_news_url)
            new.view_num += 1
            new.save()
            ret_dict = {}
            ret_dict['title'] = new.title
            ret_dict['body'] = new.body
            ret_dict['image'] = new.image.url
            ret_dict['excEditor'] = new.exc_editor
            ret_dict['dutyEditor'] = new.duty_editor
            ret_dict['viewNum'] = new.view_num
            ret_dict['datetime'] = new.datetime.strftime(("%Y-%m-%d %H:%M"))
            if new.file:
                ret_dict['attachmentUrl'] = new.file.url
            json_file = json.dumps(ret_dict, ensure_ascii=False, sort_keys=True, indent=4)
            # return JsonResponse(ret_dict)
            return HttpResponse(json_file, content_type="application/json")
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


def fix_server(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name', '')
            title = request.POST.get('title', '')
            text = request.POST.get('text', '')
            try:
                image = request.FILES['image']
            except:
                image = None
            FixServer.objects.create(name=name, title=title, text=text, image=image)
            return JsonResponse({'status':'success'})
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
            ele_dict['imageUrl'] = img.image.url
            ret_list.append(ele_dict)
        for video in WondVideo.objects.all().order_by('upload_time'):
            video_dict = {}
            video_dict['title'] = video.title
            video_dict['compress_image'] = video.compress_image.url
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
            organization_framework_image = SomeElse.objects.all()[0].organization_framework_image.url
            organization_framework_text = SomeElse.objects.all()[0].organization_framework_text
            json_data = json.dumps({'department': ret_list, "framework_image": organization_framework_image,
                                    "framework_text": organization_framework_text
                                    }, ensure_ascii=False, sort_keys=True, indent=4)
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
                    sta_dict['imageUrl'] = staff.image.url
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
                chef = Chef.objects.get(if_chef_now=True)
                json_data = json.dumps({'chef': chef.name, 'staffs': staff_list, 'news': news_list, 'activity': activity_list},
                                       ensure_ascii=False, sort_keys=True, indent=4)
                return HttpResponse(json_data, content_type="application/json")

            elif department_name[1] == 'staff':
                department = Department.objects.get(name=department_name[0])
                staff = department.staff_set.get(name=department_name[2])
                staff_dict = {}
                staff_dict['name'] = staff.name
                staff_dict['grade'] = staff.grade
                staff_dict['rank'] = staff.rank
                staff_dict['introduction'] = staff.introduction
                staff_dict['department'] = staff.department.name
                staff_dict['chef_flag'] = staff.chef_flag
                staff_dict['imageUrl'] = staff.image.url

                staff_dict['phone'] = staff.telephone
                staff_dict['email'] = staff.e_mail

                json_data = json.dumps(staff_dict,
                                       ensure_ascii=False, sort_keys=True, indent=4)
                return HttpResponse(json_data, content_type="application/json")

            elif department_name[1] == 'chef':
                department = Department.objects.get(name=department_name[0])
                chef = department.chef_set.get(name=department_name[2])
                chef_dict={}
                chef_dict['name'] = chef.name
                chef_dict['grade'] = chef.grade

                chef_dict['introduction'] = chef.introduction
                chef_dict['department'] = chef.department.name
                chef_dict['chef_now'] = chef.chef_now
                chef_dict['imageUrl'] = chef.image.url
                json_data = json.dumps(chef_dict,
                                       ensure_ascii=False, sort_keys=True, indent=4)
                return HttpResponse(json_data, content_type="application/json")

            elif department_name[1] == 'chefs':
                department = Department.objects.get(name=department_name[0])
                chefs = department.chef_set.all().order_by('datetime')
                chefs_dict = {}
                chefs_list = []
                for chef in chefs:
                    chefs_dict['name'] = chef.name
                    chefs_dict['if_chef_now'] = chef.if_chef_now
                    chefs_dict['introduction'] = chef.introduction
                    chefs_dict['grade'] = chef.grade
                    chefs_dict['departmrnt'] = chef.department.name
                    chefs_dict['phone'] = chef.telephone
                    chefs_dict['email'] = chef.e_mail
                    chefs_list.append(chefs_dict)
                json_data = json.dumps({'chefs': chefs_dict},
                                       ensure_ascii=False, sort_keys=True, indent=4)
                return HttpResponse(json_data, content_type="application/json")


            else:
                return HttpResponse('wwwwwwwwwwrong url')
    else:
        return HttpResponse('fail, wrong request method')


def show_framework(request):
    organization_framework_image = SomeElse.objects.all()[0].organization_framework_image.url
    organization_framework_text = SomeElse.objects.all()[0].organization_framework_text
    json_data = json.dumps({"framework_image": organization_framework_image,
                            "framework_text": organization_framework_text
                            }, ensure_ascii=False, sort_keys=True, indent=4)
    return HttpResponse(json_data, content_type="application/json")


# 合作交流
def show_academy(request, dynamic_news_url=None):
    if request.method == 'GET':
        if not dynamic_news_url:
            # 动态url为空的情况，赋予列表
            ret_list = []
            for new in Academy.objects.all().order_by('datetime'):
                ele_dict = {}
                # deltatime = datetime.now() - new.datetime.replace(tzinfo=None)
                # if deltatime.days >= 7:
                #     new_flag = False
                # else:
                #     new_flag = True
                # ele_dict['newFlag'] = new_flag
                ele_dict['title'] = new.title
                ele_dict['url'] = new.url
                ele_dict['datetime'] = new.datetime.strftime(("%Y-%m-%d %H:%M"))
                ele_dict['text'] = new.text
                ret_list.append(ele_dict)
            json_data = json.dumps({'academy': ret_list}, ensure_ascii=False, sort_keys=True, indent=4)
            # return JsonResponse({'news': ret_list})
            return HttpResponse(json_data, content_type="application/json")

        else:
            academy = Academy.objects.get(title=dynamic_news_url)
            ret_dict = {}
            ret_dict['url'] = academy.url
            ret_dict['text'] = academy.text
            ret_dict['title'] = academy.title
            ret_dict['datetime'] = academy.datetime.strftime(("%Y-%m-%d %H:%M"))
            json_file = json.dumps(ret_dict, ensure_ascii=False, sort_keys=True, indent=4)
            # return JsonResponse(ret_dict)
            return HttpResponse(json_file, content_type="application/json")

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
            json_data = json.dumps({'rights': ret_list}, ensure_ascii=False, sort_keys=True, indent=4)
            # return JsonResponse({'news': ret_list})
            return HttpResponse(json_data, content_type="application/json")

        else:
            right = Rights.objects.get(title=dynamic_news_url)
            ret_dict = {}
            ret_dict['url'] = right.url
            ret_dict['text'] = right.text
            ret_dict['title'] = right.title
            ret_dict['datetime'] = right.datetime.strftime(("%Y-%m-%d %H:%M"))
            json_file = json.dumps(ret_dict, ensure_ascii=False, sort_keys=True, indent=4)
            # return JsonResponse(ret_dict)
            return HttpResponse(json_file, content_type="application/json")
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
            json_data = json.dumps({'thoughts': ret_list}, ensure_ascii=False, sort_keys=True, indent=4)
            # return JsonResponse({'news': ret_list})
            return HttpResponse(json_data, content_type="application/json")

        else:
            thought = Thoughts.objects.get(title=dynamic_news_url)
            ret_dict = {}
            ret_dict['url'] = thought.url
            ret_dict['text'] = thought.text
            ret_dict['title'] = thought.title
            ret_dict['datetime'] = thought.datetime.strftime(("%Y-%m-%d %H:%M"))
            json_file = json.dumps(ret_dict, ensure_ascii=False, sort_keys=True, indent=4)
            # return JsonResponse(ret_dict)
            return HttpResponse(json_file, content_type="application/json")
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
                ele_dict['url'] = new.image.url
                ele_dict['text'] = new.text
                ret_list.append(ele_dict)
            json_data = json.dumps({'star': ret_list}, ensure_ascii=False, sort_keys=True, indent=4)
            # return JsonResponse({'news': ret_list})
            return HttpResponse(json_data, content_type="application/json")

        else:
            ret_dict = {}
            star = Star.objects.get(content=dynamic_url)
            ret_dict['content'] = star.content
            ret_dict['image'] = star.image.url
            ret_dict['text'] = star.text
            json_file = json.dumps(ret_dict, ensure_ascii=False, sort_keys=True, indent=4)
            # return JsonResponse(ret_dict)
            return HttpResponse(json_file, content_type="application/json")
    else:
        return HttpResponse('fail, wrong request method')


def show_schools(request, dynamic_url=None):
    if request.method == 'GET':
        if not dynamic_url:
            ret_list = []
            for school in School.objects.all():
                ele_dict = {}
                ele_dict['name'] = school.name
                ele_dict['introduction'] = school.introduction
                ele_dict['chef'] = school.chef
                ele_dict['chef_introduction'] = school.chef_introduction
                ret_list.append(ele_dict)
            system_brief_image = SomeElse.objects.all()[0].school_system_brief_image.url
            system_brief_text = SomeElse.objects.all()[0].school_system_brief_text
            json_data = json.dumps({'schools': ret_list, 'system_brief_image': system_brief_image,
                                    'system_brief_text':system_brief_text}, ensure_ascii=False, sort_keys=True, indent=4)
            return HttpResponse(json_data, content_type="application/json")

        else:
            school_name = dynamic_url.split('/')
            if len(list(school_name)) == 1 and school_name[0] != 'brief':
                school = School.objects.get(name=school_name[0])
                ret_dict = {}
                ret_dict['name'] = school.name
                ret_dict['introcduction'] = school.introduction
                ret_dict['chef'] = school.chef
                ret_dict['chef_introduction'] = school.chef_introduction
                json_file = json.dumps(ret_dict, ensure_ascii=False, sort_keys=True, indent=4)
                return HttpResponse(json_file, content_type="application/json")
            else:
                system_brief_image = SomeElse.objects.all()[0].school_system_brief_image.url
                system_brief_text = SomeElse.objects.all()[0].school_system_brief_text
                json_data = json.dumps({'system_brief_image': system_brief_image, 'system_brief_text':system_brief_text}
                                       , ensure_ascii=False, sort_keys=True, indent=4)
                return HttpResponse(json_data, content_type="application/json")
    else:
        return HttpResponse('fail, wrong request method')


def show_course(request, dynamic_url=None):
    if request.method == 'GET':
        if not dynamic_url:
            all_course = Course.objects.all()
            course_list = []
            for course in all_course:
                course_dict={}
                course_dict['name'] = course.course_name
                course_dict['fileUrl'] = [{'filename': file.file_name, 'url': file.file.url}
                                          for file in course.coursefile_set.all()]
                course_list.append(course_dict)
            json_data = json.dumps({'course': course_list}, ensure_ascii=False, sort_keys=True, indent=4)
            return HttpResponse(json_data, content_type="application/json")
        else:
            course = Course.objects.get(course_name=dynamic_url)
            re_dict = {}
            re_dict['name'] = course.course_name
            file_list = []
            for file in course.coursefile_set.all():
                ele_dict = {}
                ele_dict['filename'] = file.file_name
                ele_dict['url'] = file.file.url
                file_list.append(ele_dict)
            re_dict['file'] = file_list
            json_data = json.dumps(re_dict, ensure_ascii=False, sort_keys=True, indent=4)
            return HttpResponse(json_data, content_type="application/json")
    else:
        return HttpResponse('fail , method wrong')


def show_course_information(request, dynamic_news_url=None):
    if request.method == 'GET':
        if not dynamic_news_url:
            # 动态url为空的情况，赋予列表
            ret_list = []
            for new in CourseInformation.objects.all().order_by('datetime'):
                ele_dict = {}
                ele_dict['title'] = new.title
                ele_dict['viewNum'] = new.view_num
                ele_dict['datetime'] = new.datetime.strftime(("%Y-%m-%d %H:%M"))
                ret_list.append(ele_dict)
            json_data = json.dumps({'courseinformation': ret_list}, ensure_ascii=False, sort_keys=True, indent=4)
            # return JsonResponse({'contact': ret_list})
            return HttpResponse(json_data, content_type="application/json")

        else:
            new = CourseInformation.objects.get(title=dynamic_news_url)
            new.view_num += 1
            new.save()
            ret_dict = {}
            ret_dict['title'] = new.title
            ret_dict['body'] = new.body
            if new.image.url:
                ret_dict['image'] = new.image.url
            ret_dict['excEditor'] = new.exc_editor
            ret_dict['dutyEditor'] = new.duty_editor
            ret_dict['viewNum'] = new.view_num
            ret_dict['datetime'] = new.datetime.strftime(("%Y-%m-%d %H:%M"))
            if new.file:
                ret_dict['attachmentUrl'] = new.file.url
            json_file = json.dumps(ret_dict, ensure_ascii=False, sort_keys=True, indent=4)
            # return JsonResponse(ret_dict)
            return HttpResponse(json_file, content_type="application/json")
    else:
        return HttpResponse('fail, wrong request method')


def show_schoolUnion(request):
    if request.method == "GET":
        try:
            school = models.ForeignKey(SchoolUnion, verbose_name="学生联合会")
            schoolUnion = SchoolUnion.objects.all()[0]
            ret_dict = {}
            ret_dict['text'] = schoolUnion.Text
            ret_dict['chef'] = "suchef/"
            ret_dict['staff'] = "sustaff/"
            ret_dict['photos'] = 'suphoto/'
        except:
            ret_dict = {}
            ret_dict['text'] = ''
            ret_dict['chef'] = ""
            ret_dict['staff'] = ""
            ret_dict['photos'] = ''
        return JsonResponse(ret_dict)
    else:
        return HttpResponse("fail wrong method")


def show_suChef(request):
    if request.method == "GET":
        # suChef_list = SchoolUnion.suchef_set.all()
        chef_list = []
        for suChef in SchoolUnion.suchef_set.all().order_by("datetime"):
            ret_dict = {}
            ret_dict['name'] = suChef.name
            ret_dict['if_chef_now'] = suChef.if_chef_now
            ret_dict["introduction"] = suChef.introduction
            ret_dict["grade"] = suChef.grade
            ret_dict["datetime"] = suChef.datetime.strftime(("%Y-%m-%d %H:%M"))
            ret_dict["telephone"] = suChef.telephone
            ret_dict["email"] = suChef.e_mail
            chef_list.append(ret_dict)
        return JsonResponse(chef_list)
    else:
        return HttpResponse("fail wrong method")


def show_suStaff(request):
    if request.method == "GET":
        # suChef_list = SchoolUnion.suchef_set.all()
        chef_list = []
        for sustaff in SchoolUnion.sustaff_set.all():
            ret_dict = {}
            ret_dict['name'] = sustaff.name
            ret_dict["introduction"] = sustaff.introduction
            ret_dict["grade"] = sustaff.grade
            ret_dict["rank"] = sustaff.rank
            ret_dict["telephone"] = sustaff.telephone
            ret_dict["email"] = sustaff.e_mail
            chef_list.append(ret_dict)
        return JsonResponse(chef_list)
    else:
        return HttpResponse("fail wrong method")


def show_oldPicture(request):
    if request.method == "GET":
         photo = SchoolUnion.suphoto.photo
         return JsonResponse({"photo": photo.photo})
    else:
        return HttpResponse("wrong method")


# class suPhoto(models.Model):
#     shcool = models.ForeignKey(SchoolUnion, verbose_name="学生联合会历史图片")
#     photo = models.TextField(verbose_name="历史照片")


def upload_media(request):
    """
    :param request:
    :return: {'error': 0, 'url': 'file_url'} or {'error': 1}
    :description: 接收后台富文本Textarea上传的媒体文件,正常接收&存储返回{'error': 0, 'url': '/file/path/to/upload_media.png'}.
    :var: media_type: 接收媒体文件类型, image / media / file
          media_data: 接收媒体文件数据, 可直接写入文件
    """
    media_type = request.GET.get('dir')
    media_data = request.FILES.get('media_file').read()
    return JsonResponse({'error': 0, 'url': '/files/information/d.jpg'})


def get_test_data(request):
    """
    :param request:
    :return:
    :description: 测试富文本返回页面
    """
    return HttpResponse(WpPosts.objects.get(post_title='asd').post_content)

