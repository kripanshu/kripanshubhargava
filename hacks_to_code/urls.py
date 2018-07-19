from django.urls import path
from hacks_to_code import views

urlpatterns = (

    # homepage/ splash page
    #
    path(r'home',
         views.view_homepage,
         name='view_homepage'),

    # homepage/ splash page
    #
    path(r'my-blog',
         views.view_my_blog,
         name='view_my_blog'),

    # homepage/ splash page
    #
    path(r'write-my-blog',
         views.view_write_my_blog,
         name='view_write_my_blog'),
)
