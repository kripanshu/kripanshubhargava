from django.db import models
import uuid
import jsonfield
# For the prototype, set the current schema for now...
from model_utils.models import TimeStampedModel
from collections import OrderedDict
from tinymce import HTMLField
from utils.basic_response import (ok_resp,
                                  err_resp)

# Create your models here.
PROGRAMMING = u'programming language'
TOPIC_CHOICES = ()

DEFAULT_TOPIC_IMAGE = 'backup/htc_icon.png'
DEFAULT_BLOG_IMAGE = 'backup/back.jpg'
DEFAULT_PROFILE_IMAGE = 'backup/meicon.png'


class UserProfile(TimeStampedModel):
    """ user details"""
    name = models.CharField(blank=False, max_length=255)
    username = models.CharField(unique=True, blank=False, max_length=255)
    user_Id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=False, default=DEFAULT_PROFILE_IMAGE)
    followers = jsonfield.JSONField(default=None,
                                    blank=True,
                                    load_kwargs=dict(object_pairs_hook=OrderedDict)) # contains list of user ID's
    followers_count = models.IntegerField(default=0, blank=True)
    about_me = models.TextField(blank=True, max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    validate = models.BooleanField(blank=False, default=True)

    def __str__(self):
        return '%s' % (self.username)

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        self.profile_pic = kwargs.get('profile_pic')
        if not self.profile_pic:
            self.profile_pic = DEFAULT_PROFILE_IMAGE

        super(UserProfile, self).save(*args, **kwargs)

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

    def get_all_objects(self):
        """return all objects"""
        result = UserProfile.objects.all()

        if not result:
            return err_resp('could not get the object list as %s' % result)
        else:
            return ok_resp(result)


    def get_objects_by_username(self, username):
        """return object by username"""
        result = UserProfile.objects.filter(username=username).first()

        if not result:
            return err_resp('could not get the object for id %s' % username)

        else:
            return ok_resp(result)


    def get_objects_by_id(self, id):
        """ return object by id"""

        result = UserProfile.objects.filter(id=id).first()

        if not result:
            return err_resp('could not get the object for id %s' % id)

        else:
            return ok_resp(result)


class ListTopicsModels(TimeStampedModel):
    """ class to keep record of all the models"""
    topic_id = models.CharField(blank=False, max_length=255, default='ml001')
    name = models.CharField(blank=False, unique=True, max_length=255)
    description = models.TextField(blank=True)
    username = models.CharField(blank=False,
                                max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(blank=False, default=True)

    class Meta:
        ordering = ('-created',)
        #verbose_name = 'Topics'# topics models'
        verbose_name_plural = 'List topics models'

    def __str__(self):
        return '%s' % str(self.topic_id)

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

    def get_all_objects(self):
        """return all objects"""
        result = ListTopicsModels.objects.all()

        if not result:
            return err_resp('could not get the object list as %s' % result)
        else:
            return ok_resp(result)


    def get_objects_by_id(self, topic_id):
        """return object by id"""
        result = ListTopicsModels.objects.filter(topic_id=topic_id).first()

        if not result:
            return err_resp('could not get the object for id %s' % topic_id)

        else:
            return ok_resp(result)

    def delete_user(self, user_id):
        """delete user record"""
        result = UserProfile.objects.filter(user_Id=user_id).delete()
        if not result:
            return err_resp('could not delete user %s' % user_id)

        else:
            return ok_resp(result)


class BlogDescriptionModel(TimeStampedModel):
    """ all the details and naming related to blogs"""
    blog_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    topic_id = models.ForeignKey(ListTopicsModels, on_delete=models.PROTECT)
    name = models.CharField(unique=True, blank=False, max_length=255, default='Blog Name not Given')
    user_Id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=uuid.uuid4)
    topic_image = models.ImageField(upload_to='topic_image', blank=False, default=DEFAULT_TOPIC_IMAGE)
    description = models.TextField(blank=False, default='No description Given')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(blank=False, default=True)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '%s' % self.blog_id

    def save(self, *args, **kwargs):
        # self.user_Id = '8fafa644-8d54-4776-87f3-a3707ca979e4'
        # print('topic image', self.topic_image)

        if self.topic_image is None:
            self.topic_image = DEFAULT_TOPIC_IMAGE

        self.blog_id = uuid.uuid4()

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
            result = BlogDescriptionModel.objects.values('name').filter(is_published=True)

            if not result:
                return err_resp('could not get the object list as %s' % result)
            else:
                return ok_resp(result)

    def get_all_objects(self):
        """return all objects"""
        result = BlogDescriptionModel.objects.filter(is_published=True).all()

        if not result:
            return err_resp('could not get the object list as %s' % result)
        else:
            return ok_resp(result)


    def get_objects_by_topic_id(self, topic_id):
        """return object by id"""
        topic = ListTopicsModels.objects.filter(topic_id=topic_id).first()
        if not topic:
            return err_resp('not topic found for given topic_id')
        result = BlogDescriptionModel.objects.filter(topic_id=topic, is_published=True)

        if not result:
            return err_resp('could not get the object for id %s' % topic_id)

        else:
            return ok_resp(result)

    def get_objects_by_blog_id(self, blog_id):
        """return object by id"""
        result = BlogDescriptionModel.objects.filter(blog_id=blog_id, is_published=True).first()

        if not result:
            return err_resp('could not get the object for id %s' % blog_id)

        else:
            return ok_resp(result)

    def delete_blog_description(self, blog_id):
        """delete user record"""
        result = BlogDescriptionModel.objects.filter(blog_id=blog_id).delete()
        if not result:
            return err_resp('could not delete user %s' % blog_id)

        else:
            return ok_resp(result)


class Blog(TimeStampedModel):
    """ blog content"""
    user_Id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=uuid.uuid4)
    blog_id = models.ForeignKey(BlogDescriptionModel, on_delete=models.PROTECT)
    blog_image = models.ImageField(upload_to='blog_image', blank=False, default=DEFAULT_BLOG_IMAGE)
    likes_count = models.IntegerField(blank=True, default=0)
    comments = jsonfield.JSONField(default=None,
                                   blank=True,
                                   load_kwargs=dict(object_pairs_hook=OrderedDict))
    flags = jsonfield.JSONField(default=None,
                                blank=True,
                                load_kwargs=dict(object_pairs_hook=OrderedDict))
    tags = jsonfield.JSONField(default=None,
                               blank=False,
                               load_kwargs=dict(object_pairs_hook=OrderedDict))
    tinymce = HTMLField('Content')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)



    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        if self.blog_image is None:
            self.blog_image = DEFAULT_BLOG_IMAGE

        super(Blog, self).save(*args, **kwargs)

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

    def get_all_objects(self):
        """return all objects"""
        result = Blog.objects.all()

        if not result:
            return err_resp('could not get the object list as %s' % result)
        else:
            return ok_resp(result)

    def get_objects_by_topic_id(self, topic_id):
        """return object by id"""
        result = Blog.objects.filter(topic_id=topic_id).first()

        if not result:
            return err_resp('could not get the object for id %s' % topic_id)

        else:
            return ok_resp(result)

    def get_objects_by_blog_id(self, blog_id):
        """return object by id"""
        obj = BlogDescriptionModel.objects.get(blog_id=blog_id)

        if not obj:
            return err_resp('could not find the object for id in Blog Description model %s' % blog_id)

        result = Blog.objects.filter(blog_id=obj).first()

        if not result:
            return err_resp('could not get the object for id %s' % blog_id)

        else:
            return ok_resp(result)

    def delete_blog(self, blog_id):
        """delete user record"""
        result = Blog.objects.filter(blog_id=blog_id).delete()
        if not result:
            return err_resp('could not delete user %s' % blog_id)

        else:
            return ok_resp(result)


