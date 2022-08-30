from django.contrib import admin, messages
from youtube_downloader.models import Manage, Category
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ManageAdminForm(forms.ModelForm):
    # content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Manage
        fields = '__all__'


@admin.register(Manage)
class ManageAdmin(admin.ModelAdmin):
    form = ManageAdminForm
    save_as = True
    save_on_top = True
    list_display = ('title', 'price', 'category', 'get_photo', 'views', 'add_date')
    list_editable = ['price']
    ordering = ['add_date']
    search_fields = ['title']
    readonly_fields = ('views', 'add_date', 'get_photo')
    list_filter = ('category', )
    fields = ('title', 'price', 'category', 'photo', 'get_photo', 'views', 'add_date')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}"width=50px>')
        return '-'
    # get_photo.short_description = 'photo'

admin.site.register(Category)

# /Users/mac/Desktop/MyDjandoProjects/downloader/manage.py

