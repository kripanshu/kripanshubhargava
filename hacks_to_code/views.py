import json, collections
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
from django.http import \
    (JsonResponse, HttpResponse,
     Http404, HttpResponseRedirect,
     QueryDict)
# Create your views here.


def view_homepage(request):
    """Opens the homepage/resume"""
    return render(request, 'home.html')


def view_my_blog(request):
    """Opens the homepage/resume"""
    return render(request, 'my_blog.html')