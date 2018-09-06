from django.urls import path
from jobbot import views

urlpatterns = (

    # homepage/ splash page
    #
    path('',
         views.homepage,
         name='homepage'),
)
