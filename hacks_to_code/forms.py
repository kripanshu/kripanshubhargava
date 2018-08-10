import json
from tinymce import TinyMCE
from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from hacks_to_code.models import (ListTopicsModels, UserProfile , BlogDescriptionModel, Blog)
from hacks_to_code.hacks_to_code_constants import  (MACHINE_LEARNING_ID, FRAMEWORKS_AND_TOOLS_ID,PROGRAMMING_LANGUAGES_ID,
                                                    STATISTICAL_LEARNING_ID, TECHNOLOGY_ID, MITAL_ID, KRIPANSHU_ID)

CHOICES =(MACHINE_LEARNING_ID,
          FRAMEWORKS_AND_TOOLS_ID,
          PROGRAMMING_LANGUAGES_ID,
          STATISTICAL_LEARNING_ID,
          TECHNOLOGY_ID)

CHOICES_USER = (MITAL_ID, KRIPANSHU_ID)


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class BlogDescriptionForms(forms.Form):
    """Form to get details """

    name = forms.CharField(required=True, label='Name', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'validate',
                                                         'type':'text',
                                                         'id':'name',
                                                          'placeholder': 'Enter the Blog Title',
                                                          'font-family': 'Lato, sans-serif'}))
    topic_id = forms.ModelChoiceField(queryset=ListTopicsModels.objects.all(), initial='ml001',
                                      widget=forms.Select(attrs={'class' : 'Select',
                                                                  'font-family': 'Lato, sans-serif'}))
    topic_image = forms.FileField(required=False)
    user_id = forms.ModelChoiceField(queryset=UserProfile.objects.all(), initial='Kripanshu',
                                     widget=forms.Select(attrs={'class' : 'Select',
                                                                'font-family': 'Lato, sans-serif'}))
    description = forms.CharField(required=True, max_length=255, label='Description',
                                  widget=forms.Textarea(attrs={'class': 'materialize-textarea',
                                                                'type':'text',
                                                                'id':'description',
                                                               'placeholder': 'Describe your blog briefly',
                                                               'font-family': 'Lato, sans-serif'}))
    # is_published = forms.BooleanField(required=False, label='Publish ?', widget=forms.CheckboxInput(attrs={'class' : 'form-control'}))
    blog_image = forms.FileField(required=False)
    tags = forms.CharField(required=True, max_length=255, label='Tags',
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Python, Java, ...',
                                                         'font-family': 'Lato, sans-serif'}))
    tinymce = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10,
                   'font-family': 'Lato, sans-serif',
                   'placeholder': 'Write here ...'}
        )
    )

    def get_cleaned_blog_image(self):
        blog_image = self.cleaned_data.get('blog_image')
        if blog_image is None:
            raise forms.ValidationError(
                _('Image not uploaded'))

        return blog_image

    def get_cleaned_tags(self):
        tags = self.cleaned_data.get('tags')
        # b = tags.split(',')
        # words = []
        # for item in b:
        #     words.append(item.strip())
        if tags is None:
            raise forms.ValidationError(
                _('No tag found'))
        return tags

    def get_cleaned_tinymce(self):
        tinymce = self.cleaned_data.get('tinymce')
        if tinymce is None:
            raise forms.ValidationError(
                _('Write a blog'))

        return tinymce

    def get_cleaned_name(self):
        name = self.cleaned_data.get('name')
        print('name ', name)
        if not name:
            raise forms.ValidationError(
                _('That is not a valid name.'))
        return name

    def get_cleaned_topic_image(self):
        topic_image = self.cleaned_data.get('topic_image')
        if topic_image is None:
            print("No image uploaded")
            raise forms.ValidationError(
                _('No image uploaded'))
        print(' topic image', topic_image)
        return topic_image

    def get_cleaned_description(self):
        desc = self.cleaned_data.get('description')
        if not desc:
            raise forms.ValidationError(
                _('That is not a valid description.'))
        return desc

    # def get_cleaned_published(self):
    #     pub = self.cleaned_data.get('is_published')
    #     if not pub:
    #         raise forms.ValidationError(
    #             _('Value should be either true or false.'))
    #     return pub


    def get_cleaned_topic_id(self):
        topic_id = self.cleaned_data.get('topic_id')
        print('---------topuc ----', topic_id)
        if not topic_id:
            raise forms.ValidationError(
                _('Topic ID not found'))
        # for topic in topic_id:
        #     print("------topic-------",topic)

        return topic_id

    def get_cleaned_user_id(self):
        user_id = self.cleaned_data.get('user_id')
        print('-------u ser ID----', user_id)
        if not user_id:
            raise forms.ValidationError(
                _('Topic ID not found'))
        # for user in user_id:
        #     print("------topic-------", user)

        return user_id






"""
fab run_shell
from hacks_to_code.forms import BlogDescriptionForms

data = dict(name='Calculate ECDF',
            description='To calculate the ecdf fof the given file in r',
            is_published=True)
f = BlogDescriptionForms(data)
f.is_valid()
f.errors

"""