from django.contrib import admin
from hacks_to_code.models import ( ListTopicsModels, BlogDescriptionModel, UserProfile, Blog)
# Register your models here.


class ListTopicsModelsAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'topic_id',
                    'name',
                    'description',
                    'username',
                    'created',
                    'modified',
                    'is_published')

    save_on_top = True
    readonly_fields = ('modified', 'created')
    list_filter = ('is_published',)


admin.site.register(ListTopicsModels, ListTopicsModelsAdmin)


class BlogDescriptionModelAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'topic_id',
                    'blog_id',
                    'name',
                    'description',
                    'user_Id',
                    'created',
                    'modified',
                    'is_published',
                    'topic_image'
                    )

    save_on_top = True
    readonly_fields = ('modified', 'created')
    list_filter = ('is_published',)

admin.site.register(BlogDescriptionModel, BlogDescriptionModelAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'blog_id',
                    'blog_image',
                    'tinymce',
                    'tags',
                    'comments',
                    'flags',
                    'likes_count',
                    'created',
                    'modified'
                    )
    save_on_top = True
    readonly_fields = ('modified', 'created')


admin.site.register(Blog, BlogAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'username',
                    'user_Id',
                    'about_me',
                    'profile_pic',
                    'followers',
                    'followers_count',
                    'created',
                    'modified',
                    'validate')

    save_on_top = True
    readonly_fields = ('modified', 'created')
    list_filter = ('validate',)

admin.site.register(UserProfile, UserProfileAdmin)

