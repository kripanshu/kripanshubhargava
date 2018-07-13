from django.urls import path
from web_part import views

urlpatterns = (

    # homepage/ splash page
    #
    path('',
         views.view_homepage,
         name='view_homepage'),
)
