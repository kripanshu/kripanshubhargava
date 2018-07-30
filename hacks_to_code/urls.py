from django.urls import path, re_path
from hacks_to_code import views

urlpatterns = (

    # homepage/ splash page
    #
    path(r'home',
         views.view_homepage,
         name='view_homepage'),

    # homepage/ splash page
    #
    re_path(r'home/(?P<topic_id>[a-zA-Z0-9_\.-]+$)',
         views.view_homepage_blog_list,
         name='view_homepage_blog_list'),


    # homepage/ splash page
    #
    re_path(r'my-blog/(?P<blog_id>[a-zA-Z0-9_\.-]+$)',
         views.view_my_blog,
         name='view_my_blog'),

    # homepage/ splash page
    #
    path(r'write-blog-details',
         views.view_write_blog_details,
         name='view_write_blog_details'),
)
