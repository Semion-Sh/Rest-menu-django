from django.contrib import admin, messages
from youtube_downloader.models import Manage, Category
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ManageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Manage
        fields = '__all__'


@admin.register(Manage)
class ManageAdmin(admin.ModelAdmin):
    form = ManageAdminForm
    save_as = True
    save_on_top = True
    list_display = ('title', 'price', 'photo', 'category', 'views', 'add_date')
    list_editable = ['price']
    ordering = ['add_date']
    search_fields = ['title']
    readonly_fields = ('views', 'add_date', 'photoo')
    list_filter = ('category', )
    fields = ('title', 'price', 'photo', 'category', 'views', 'add_date', 'photoo')

    def photoo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photoo.url}"width=50px>')
        return '-'
    photoo.short_description = 'фото'


admin.site.register(Category)

# /Users/mac/Desktop/MyDjandoProjects/downloader/manage.py

