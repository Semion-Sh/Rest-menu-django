from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from pytube import YouTube
from youtube_downloader.models import Video
file_size = 0
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context


def main(request):
    return HttpResponse(render(request, 'youtube_downloader/index_.html'))


def seasonal_menu(request):
    return HttpResponse(render(request, 'youtube_downloader/seasonal_menu.html'))

def banquet_menu(request):
    return HttpResponse(render(request, 'youtube_downloader/banquet_menu.html'))

def wine_map(request):
    return HttpResponse(render(request, 'youtube_downloader/wine_map.html'))

def Alcoholic(request):
    return HttpResponse(render(request, 'youtube_downloader/Alcoholic.html'))

def Beverages(request):
    return HttpResponse(render(request, 'youtube_downloader/Beverages.html'))



def about_as(request):
    return HttpResponse(render(request, 'youtube_downloader/about_as_.html'))


def videos(request):
    return HttpResponse(render(request, 'youtube_downloader/videos_.html'))


def post(request, id: int):
    return HttpResponse(render(request, 'youtube_downloader/description_.html'))


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def download_video(request):
    global file_size
    url = request.GET.get('url')
    if request.method == 'POST':
        try:
            url_input = request.form[url]
            yt = YouTube(url_input)
            file_size = yt.streams.get_by_itag(22).filesize
            yt.streams.filter(progressive=True, file_extension='mp4', only_video=False).order_by('resolution').desc()
            yt = yt.streams.get_highest_resolution().download(output_path='/Users/mac/Desktop/')
            yt = YouTube(url_input)
            title = yt.title
            size = yt.streams.get_by_itag(22).filesize // 1000000
            video = Video(title=title, size=size)
            video.save()
        except:
            return 'Downloading Error'

        # try:
        #     db.session.add(video)
        #     db.session.commit()
        #     return redirect('/videos')
        # except:
        #     return 'Saving Error'
    else:
        return HttpResponse(render(request, 'youtube_downloader/download_video_.html'))



# def post(request, id: int):
#     if id == 1:
#         return HttpResponse(render(request, '../temlates/base_.html'))
#     return HttpResponse('None')
