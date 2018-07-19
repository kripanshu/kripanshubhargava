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


# Create your views here.


def view_homepage(request):
    """Opens the homepage/resume"""
    success, user_detail = JobUtil.get_user_details()

    if not success:
        user_msg = {'error': 'Not Found',
                    'message': user_detail}
        return render(request, 'error_page.html', user_msg)
    user_msg = {'success': True,
                'message': user_detail}
    return render(request, 'home.html', user_msg)


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

def view_write_my_blog(request):
    """ write the blog"""
    return render(request, 'write_blog.html')