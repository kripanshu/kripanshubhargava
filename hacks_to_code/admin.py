from django.contrib import admin
from hacks_to_code.models import ( ListTopicsModels, BlogDescriptionModel, UserProfile, Blog)
# Register your models here.


class ListTopicsModelsAdmin(admin.ModelAdmin):
    list_display = ('id',
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
    list_display = ('topic_id',
                    'name',
                    'description',
                    'topic',
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
    list_display = ('topic_id',
                    'blog_image',
                    'tinymce',
                    'tags',
                    'comments',
                    'flags',
                    'likes_count',
                    'created',
                    'modified',
                    'is_published'
                    )
    save_on_top = True
    readonly_fields = ('modified', 'created')
    list_filter = ('is_published',)

admin.site.register(Blog, BlogAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name',
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

