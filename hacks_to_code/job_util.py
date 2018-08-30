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
    def get_user_details_by_username(username):
        """This is to get user details
        ** for now user authentication is not done is users
        are manually added.
        """
        user_obj = UserProfile()
        success, obj = user_obj.get_objects_by_username(username)

        if success:
            return ok_resp(obj)
        else:
            return err_resp(obj)

    @staticmethod
    def get_user_details_by_id(user_id):
        """This is to get user details
        ** for now user authentication is not done is users
        are manually added.
        """
        user_obj = UserProfile()
        success, obj = user_obj.get_objects_by_id(user_id)

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

    @staticmethod
    def add_blog(my_id, **data):
        """add the blog"""
        print('data we get Blog des id ---------', my_id)
        print('data we get from form', data)
        blog_id = BlogDescriptionModel.objects.get(id=my_id)
        print("blog_id instance we get", blog_id)
        # if not success:
        #     return err_resp(blog_id)
        # print('blog_id', blog_id)
        #
        # input_data = dict(blog_id=blog_id,user_Id=data.get('user_Id'),
        #                 blog_image=data.get('blog_image'),
        #                 tags=data.get('tags'),
        #                 tinymce=data.get('tinymce'))
        blog_obj = Blog(blog_id=blog_id, **data)
        blog_obj.save()

        if blog_obj.id:
            return ok_resp(blog_obj)

        else:
            return err_resp(blog_obj)

    @staticmethod
    def delete_blog_desc(blog_id):
        """ delete blog desc model"""
        success, blog_del = BlogDescriptionModel.delete_blog_description(blog_id)

        if success:
            return ok_resp(blog_del)
        else:
            return err_resp(blog_del)

    @staticmethod
    def get_blog_data(blog_id):
        """ get the blog"""
        obj = Blog()
        success, blog_data = obj.get_objects_by_blog_id(blog_id)

        if not success:
            return err_resp(blog_data)

        return ok_resp(blog_data)

    @staticmethod
    def get_blog_description(blog_id):
        obj = BlogDescriptionModel()
        success, blog_des_data = obj.get_objects_by_blog_id(blog_id)
        if not success:
            return err_resp(blog_des_data)
        print(" topic_data ---", blog_des_data)
        return ok_resp(blog_des_data)


    # @staticmethod
    # def get_home_collection(topic_id):
    #     """ get details for home needed for home"""
    #     user_detail = {}
    #     topics_list = {}
    #     final = []
    #     blog_lists = {}
    #     # success_user, user_detail = JobUtil.get_user_details(1)
    #     success_topic_list, topic_list = JobUtil.get_topics_details()
    #     success_topic, topic = JobUtil.get_blog_list_by_id(topic_id)
    #     print("This is creating problem", topic)
    #     if not success_topic_list:
    #         return err_resp(topic_list)
    #
    #     if not success_topic:
    #         print("no suchtopicfound")
    #         blog_lists = []
    #         return err_resp(topic)
    #
    #     print("This is creating problem", topic)
    #
    #     for items in topic:
    #         print("item list", items)
    #
    #         user_id = items.user_Id_id
    #         success_user, user_obj = JobUtil.get_user_details(user_id)
    #         if not success_user:
    #             pass
    #
    #         blog_lists[str(items.id)]['user_detail'] = user_obj.as_dict()
    #         blog_lists[str(items.id)]['topic'] = items.as_dict()
    #
    #         final.append(blog_lists)
    #
    #     # print(final)
    #     return ok_resp(final)


"""
from hacks_to_code.models import (UserProfile, Blog, BlogDescriptionModel, ListTopicsModels, TOPIC_CHOICES)
from utils.basic_response import (ok_resp,
                                  err_resp,
                                  err_resp_with_data)
from hacks_to_code.job_util import JobUtil
import json

success, obj = JobUtil.get_home_collection('ft001')
print(json.dumps(obj))
                                  

"""


