from django.contrib import admin
from hacks_to_code.models import ( ListTopicsModels, BlogDescriptionModel)
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
                    'username',
                    'user_detail',
                    'created',
                    'modified',
                    'is_published',
                    'topic_image'
                    )

    save_on_top = True
    readonly_fields = ('modified', 'created')
    list_filter = ('is_published',)

admin.site.register(BlogDescriptionModel, BlogDescriptionModelAdmin)


