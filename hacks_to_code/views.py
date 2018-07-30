import json, collections
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
from django.http import \
    (JsonResponse, HttpResponse,
     Http404, HttpResponseRedirect,
     QueryDict)
from hacks_to_code.job_util import JobUtil
from hacks_to_code.models import TOPIC_CHOICES
from hacks_to_code.forms import BlogDescriptionForms

# Create your views here.


def view_homepage(request):
    """Opens the homepage/resume"""
    return view_homepage_blog_list(request,'sl001')

def view_my_blog(request):
    """Opens the blog homepage page"""
    success, user_detail = JobUtil.get_user_details()

    if not success:
        user_msg = {'error': 'Not Found',
                    'message': user_detail}
        return render(request,'error_page.html',user_msg)
    user_msg = {'success': True,
                           'message': user_detail}
    return render(request, 'my_blog.html', user_msg)

def get_form_data(request):
    """get data from the form"""

def view_write_blog_details(request):
    """ write the blog"""
    form = BlogDescriptionForms(request.POST or None)

    if form.is_valid():
        data = dict(name=form.get_cleaned_name(),
                    topic_id=form.get_cleaned_topic_id(),
                    topic_image=form.get_cleaned_topic_image(),
                    user_Id=form.get_cleaned_user_id(),
                    description=form.get_cleaned_description(),
                    is_published=form.get_cleaned_published())
        success, blog_desc = JobUtil.add_blog_description(**data)
        if not success:
            return JsonResponse({'success': False})

        return render(request,'write_blog_description.html', {'data': blog_desc})

    return render(request, 'write_blog.html', {'form': form})


def view_homepage_blog_list(request, topic_id):
    """ get the list of the blog"""

    if topic_id:
        print('topic _ id ---------', topic_id)
        topic_id = topic_id

    success_user, user_detail = JobUtil.get_user_details()
    success_topic_list, topic_list = JobUtil.get_topics_details()
    success_topic, topic = JobUtil.get_blog_list_by_id(topic_id)

    # print("url ",user_detail.profile_pic.url)
    if not success_topic_list:
        user_msg = {
                    'success_list': False,
                    'error': 'Not Found',
                    'message': user_detail}
        return render(request, 'error_page.html', user_msg)

    if not success_user:
        user_msg = {'success_topic': True,
                    'success_user': False,
                    'success_list': True,
                    'error': 'Not Found',
                    'topics_list': topic_list,
                    'topics': topic
                    }
        return render(request, 'home.html', user_msg)

    if not success_topic:
        user_msg = {'success_user': True,
                    'success_list': True,
                    'success_topic': False,
                    'error': 'Topics Not Found',
                    'user_detail': user_detail,
                    'topics_list': topic_list}

        return render(request, 'home.html', user_msg)

    user_msg = {
                'success_user': True,
                'success_list': True,
                'success_topic': True,
                'user_detail': user_detail,
                'topics_list': topic_list,
                'topics': topic
                }
    print("topic list ",topic)
    return render(request, 'home.html', user_msg)