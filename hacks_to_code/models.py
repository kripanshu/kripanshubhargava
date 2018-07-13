from django.db import models
import uuid
# For the prototype, set the current schema for now...
from model_utils.models import TimeStampedModel
from collections import OrderedDict

from utils.basic_response import (ok_resp,
                                  err_resp)

# Create your models here.
PROGRAMMING = u'programming language'
TOPIC_CHOICES = ()


class ListTopicsModels(TimeStampedModel):
    """ class to keep record of all the models"""
    name = models.CharField(blank=False,max_length=255)
    description = models.TextField(blank=True)
    username = models.CharField(blank=False,
                                max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(blank=False, default=True)

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):

        super(ListTopicsModels, self).save(*args, **kwargs)

    def as_dict(self):
        """return info dict"""
        od = OrderedDict()

        for attr_name in self.__dict__.keys():

            # check for attributes to skip...
            if attr_name.startswith('_'):
                continue

            val = self.__dict__[attr_name]
            if isinstance(val, models.fields.files.FieldFile):
                # this is a file field...
                #
                val = str(val)  # file path or empty string
                if val == '':
                    val = None
                od[attr_name] = val
            else:
                od[attr_name] = val

        return od

    def get_name_list(self):
            """ get the list of all the names"""
            result = ListTopicsModels.objects.values('name').all()

            if not result:
                return err_resp('could not get the object list as %s' % result)
            else:
                return ok_resp(result)


class BlogDescriptionModel(TimeStampedModel):
    """ all the details and naming related to blogs"""
    topic_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=False, max_length=255)
    topic = models.CharField(blank=False,
                             max_length=255,
                             choices=TOPIC_CHOICES,
                             default=PROGRAMMING)
    topic_image = models.ImageField(upload_to='topic_image', blank=True)
    description = models.TextField(blank=False)
    username = models.CharField(blank=False, max_length=255)
    user_detail = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(blank=False, default=True)


    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):

        super(BlogDescriptionModel, self).save(*args, **kwargs)

    def as_dict(self):
        """return info dict"""
        od = OrderedDict()

        for attr_name in self.__dict__.keys():

            # check for attributes to skip...
            if attr_name.startswith('_'):
                continue

            val = self.__dict__[attr_name]
            if isinstance(val, models.fields.files.FieldFile):
                # this is a file field...
                #
                val = str(val)  # file path or empty string
                if val == '':
                    val = None
                od[attr_name] = val
            else:
                od[attr_name] = val

        return od

    def get_name_list(self):
            """ get the list of all the names"""
            result = ListTopicsModels.objects.values('name').all()

            if not result:
                return err_resp('could not get the object list as %s' % result)
            else:
                return ok_resp(result)
