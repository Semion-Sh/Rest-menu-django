from django.contrib import admin, messages
from youtube_downloader.models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['photo', 'price', 'title']
    list_editable = ['price']
    ordering = ['price']
    list_per_page = 2
    actions = ['set_salle_20']
    search_fields = ['title']

    def size_status(self, video):
        if video.price > 4:
            return 'heavy'

    # def set_salle_20(self, request: qs: QuerySet):
    #     qs.update(currency=Video.)
    #     self.message_user(
    #         request,
    #         f'price - 20% DONE'
    #     )

