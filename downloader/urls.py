"""downlos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from youtube_downloader.views import main, post, Beverages, about_as, videos, seasonal_menu, banquet_menu, wine_map, Alcoholic
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = 'adminka'
admin.site.index_title = 'adminka'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', main),
    path('seasonal_menu/', seasonal_menu),
    path('banquet_menu/', banquet_menu),
    path('wine_map/', wine_map),
    path('alcoholic/', Alcoholic),
    path('beverages/', Beverages),
    path('about_as/', about_as),
    path('videos/', videos),
    path('videos/', include('youtube_downloader.urls')),
    # path('download_video/', download_video),
    path('video/', include('youtube_downloader.urls')),
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
