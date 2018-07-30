import pandas as pd
import json
from collections import OrderedDict

from hacks_to_code.models import (UserProfile, Blog, BlogDescriptionModel, ListTopicsModels, TOPIC_CHOICES)
from utils.basic_response import (ok_resp,
                                  err_resp,
                                  err_resp_with_data)


class JobUtil(object):
    """ this is the utility class for view"""

    @staticmethod
    def get_user_details():
        """This is to get user details
        ** for now user authentication is not done is users
        are manually added.
        """
        user_obj = UserProfile()
        success, obj = user_obj.get_objects_by_username('kripanshu')

        if success:
            return ok_resp(obj)
        else:
            return err_resp(obj)

    @staticmethod
    def get_topics_details():
        """ list of topics"""
        topic_obj = ListTopicsModels()
        success, obj = topic_obj.get_all_objects()

        if success:
            print("topics", obj)
            return ok_resp(obj)
        else:
            return err_resp(obj)


    @staticmethod
    def get_blog_list_by_id(topic_id):
        """ list of blogs for a topic"""

        blog_obj = BlogDescriptionModel()
        success, blog_list = blog_obj.get_objects_by_topic_id(topic_id)

        if success:
            for obj in blog_list:
                print("blog list", obj.as_dict())
            return ok_resp(blog_list)
        else:
            return err_resp(blog_list)


    @staticmethod
    def add_blog_description(**data):
        """ add the blog desc"""
        print(" data submitted", data)
        blog_obj = BlogDescriptionModel(**data)
        blog_obj.save()

        if blog_obj.id:
            return ok_resp(blog_obj.as_dict())

        else:
            return err_resp(blog_obj)

