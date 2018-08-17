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


def view_write_blog_details(request):
    """ write the blog"""

    if request.method == 'POST':
        # this form contains field for both the models BlogDescriptionModel, Blog
        form = BlogDescriptionForms(request.POST, request.FILES)

        if form.is_valid():

            # we get values for the BlogDescriptionModel

            blog_desc_data = dict(name=form.get_cleaned_name(),
                                  topic_id=form.get_cleaned_topic_id(),
                                  topic_image=form.get_cleaned_topic_image(),
                                  user_Id=form.get_cleaned_user_id(),
                                  description=form.get_cleaned_description(),
                                  is_published=False    # It is False and will be made
                                                        # published by the admin till the auth
                                  )

            # save to BlogDescriptionModel
            succ, blog_des = JobUtil.add_blog_description(**blog_desc_data)
            if not succ:
                return JsonResponse({'success': False, 'message': blog_des})

            # blog_id = blog_des['blog_id']   # this must be a "BlogDescriptionModel" instance.
            my_id = blog_des['id']
            # we get values for the Blog

            blog_data = dict(user_Id=form.get_cleaned_user_id(),
                        blog_image=form.get_cleaned_blog_image(),
                        tags=form.get_cleaned_tags(),
                        tinymce=form.get_cleaned_tinymce()
                             )

            # save to Blog
            print('data_first', blog_desc_data.get('name'))
            print('data_second', blog_data.get('tinymce'))
            succ, blog = JobUtil.add_blog(my_id, **blog_data)
            if not succ:
                return JsonResponse({'success': False, 'message': blog})
            # print('data sent to blog', blog_des)
            # return view_write_blog(request, blog_des)
            user_obj = dict(success=True,
                            blog_data=blog.as_dict(),
                            blog_desc_data=blog_des)
            # return render(request,'my_blog.html',{'blog_data':blog.as_dict(),'blog_desc_data':blog_des})
            return HttpResponseRedirect('/hacks-to-code/home')
        else:
            # if form is not valid
            return JsonResponse(form.errors)
    else:
        form = BlogDescriptionForms()
        #   return JsonResponse({'errors':form.errors})

    return render(request, 'hacks_to_code/write_blog.html', {'form': form})


def view_homepage_blog_list(request, topic_id):
    """ get the list of the blog"""

    if topic_id:
        print('topic _ id ---------', topic_id)
        topic_id = topic_id

    success_user, user_detail = JobUtil.get_user_details('Kripanshu')
    success_topic_list, topic_list = JobUtil.get_topics_details()
    success_topic, topic = JobUtil.get_blog_list_by_id(topic_id)

    print("url ",user_detail)
    if not success_topic_list:
        user_msg = {
                    'success_list': False,
                    'error': 'Not Found',
                    'message': user_detail}
        return render(request, 'hacks_to_code/error_page.html', user_msg)

    if not success_user:
        user_msg = {'success_topic': True,
                    'success_user': False,
                    'success_list': True,
                    'error': 'Not Found',
                    'topics_list': topic_list,
                    'topics': topic
                    }
        return render(request, 'hacks_to_code/home.html', user_msg)

    if not success_topic:
        user_msg = {'success_user': True,
                    'success_list': True,
                    'success_topic': False,
                    'error': 'Topics Not Found',
                    'user_detail': user_detail,
                    'topics_list': topic_list}

        return render(request, 'hacks_to_code/home.html', user_msg)

    user_msg = {
                'success_user': True,
                'success_list': True,
                'success_topic': True,
                'user_detail': user_detail,
                'topics_list': topic_list,
                'topics': topic
                }
    print("topic list ",topic)
    print("topic", topic_list)
    return render(request, 'hacks_to_code/home.html', user_msg)


def view_my_blog(request, blog_id):
    """view my blog"""
    print('--'*40)
    print(blog_id)
    print('--' * 40)
    success_blog, blog_details = JobUtil.get_blog_data(blog_id)
    if not success_blog:
        user_msg = dict(success=False,
                        error=blog_details)
        return JsonResponse(user_msg)
    print('--' * 40)
    print(blog_details.as_dict())
    print('--' * 40)

    tags = blog_details.tags.split(",")


    print('--' * 40)
    print(tags)
    print('--' * 40)


    success_user, user_details = JobUtil.get_user_details(blog_details.as_dict()['user_Id_id'])
    if not success_user:
        user_msg = dict(success=False,
                        error=user_details)
        return JsonResponse(user_msg)
    print('--' * 40)
    print(user_details.as_dict())
    print('--' * 40)
    success_topic, topic_data = JobUtil.get_blog_description(blog_id)
    if not success_topic:
        user_msg = dict(success=False,
                        error=topic_data)
        return JsonResponse(user_msg)
    print('--' * 40)
    print(topic_data.as_dict())
    print('--' * 40)
    print("url ", user_details.profile_pic.url)
    return render(request, 'hacks_to_code/my_blog.html', {'blog_data':blog_details, 'user_data':user_details, 'topic_data':topic_data, 'tags':tags})


def get_info(request):
    """ just show info page"""
    return render(request, 'hacks_to_code/info.html')