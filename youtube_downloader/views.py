from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from youtube_downloader.models import Manage
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context


def main(request):
    return HttpResponse(render(request, 'youtube_downloader/index_.html'))


def seasonal_menu(request):
    seasonal_manages = Manage.objects.filter(category=1)
    return HttpResponse(render(request, 'youtube_downloader/seasonal_menu.html', {
        'seasonal_manages': seasonal_manages
    }))


def banquet_menu(request):
    banquet = Manage.objects.filter(category=4)
    return HttpResponse(render(request, 'youtube_downloader/banquet_menu.html', {
        'banquet': banquet
    }))


def wine_map(request):
    winne_manage = Manage.objects.filter(category=5)
    return HttpResponse(render(request, 'youtube_downloader/wine_map.html', {
        'winne_manage': winne_manage
    }))


def Alcoholic(request):
    alcoholic_manage = Manage.objects.filter(category=6)
    return HttpResponse(render(request, 'youtube_downloader/Alcoholic.html', {
        'alcoholic_manage': alcoholic_manage
    }))


def Beverages(request):
    beverages = Manage.objects.filter(category=7)
    return HttpResponse(render(request, 'youtube_downloader/Beverages.html', {
        'beverages': beverages
    }))



def about_as(request):
    return HttpResponse(render(request, 'youtube_downloader/about_as_.html'))


def videos(request):
    return HttpResponse(render(request, 'youtube_downloader/videos_.html'))


def post(request, id: int):
    return HttpResponse(render(request, 'youtube_downloader/description_.html'))
