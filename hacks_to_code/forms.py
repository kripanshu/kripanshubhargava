import json

from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from hacks_to_code.models import (ListTopicsModels, UserProfile , BlogDescriptionModel, Blog)


class BlogDescriptionForms(forms.Form):
    """Form to get details """

    name = forms.CharField(required=True, label='Name', max_length=100)
    topic_id = forms.ModelMultipleChoiceField(queryset=ListTopicsModels.objects.all(), initial='ml001')
    topic_image = forms.ImageField(required=False, label='Topic Image')
    user_id = forms.ModelMultipleChoiceField(queryset=UserProfile.objects.all(), initial='Kripanshu')
    description = forms.CharField(required=True, max_length=255, label='Description')
    is_published = forms.BooleanField(required=False, label='Publish ?')


    def get_cleaned_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError(
                _('That is not a valid name.'))
        return name

    def get_cleaned_topic_image(self):
        topic_image = self.cleaned_data.get('topic_image')

        return topic_image

    def get_cleaned_description(self):
        desc = self.cleaned_data.get('description')
        if not desc:
            raise forms.ValidationError(
                _('That is not a valid description.'))
        return desc

    def get_cleaned_published(self):
        pub = self.cleaned_data.get('is_published')
        if not pub:
            raise forms.ValidationError(
                _('Value should be either true or false.'))
        return pub


    def get_cleaned_topic_id(self):
        topic_id = self.cleaned_data.get('topic_id')
        if not topic_id:
            raise forms.ValidationError(
                _('Topic ID not found'))
        for e in topic_id:
            print("------topic-------",e)

            return e

    def get_cleaned_user_id(self):
        user_id = self.cleaned_data.get('user_id')
        if not user_id:
            raise forms.ValidationError(
                _('Topic ID not found'))
        for e in user_id:
            print("------topic-------", e)

            return e








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