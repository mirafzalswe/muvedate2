from django.contrib import admin
from django.db import models
from mdeditor.widgets import MDEditorWidget

from .models import Page, Video,Tutorial


from django.contrib import admin
from .models import Page, Tutorial, Video

class TutorialInline(admin.StackedInline):
    model = Tutorial
    can_delete = True
    verbose_name_plural = 'Tutorials'
    fk_name = 'page'
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget},
    }

    def get_max_num(self, request, obj=None, **kwargs):
        max_num = 10
        if obj and obj.title:
            return max_num - 8
        return max_num

class VideoInline(admin.StackedInline):
    model = Video
    can_delete = True
    verbose_name_plural = 'videos'
    fk_name = 'page'
    def get_max_num(self, request, obj=None, **kwargs):
        max_num = 10
        if obj and obj.title:
            return max_num - 8


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'type')
    empty_value_display = '-empty-'
    search_fields = ['title']

    inlines = [
        TutorialInline,
        VideoInline,
    ]
admin.site.register(Video)
admin.site.register(Tutorial)