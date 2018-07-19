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
            return ok_resp(obj.as_dict())
        else:
            return err_resp(obj)
