from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from youtube_downloader.models import Manage, Review
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context
from django.views.generic import ListView, DeleteView, CreateView
from .forms import Review
# ----------------------------------
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine, MetaData
# import psycopg2
#
# Base = declarative_base()
# meta = MetaData()
#
#
# engine = create_engine("postgresql+psycopg2://gvaoqrlriwfoad:055f19b677f01b0411151ab91809d03ff4007515e82a428cb9f4148d8badfa54@ec2-52-207-15-147.compute-1.amazonaws.com/dcl69hnioedc5p")
# conn = engine.connect()
#
#
# session = sessionmaker(bind=engine)
# s = session()
# -------------------------------------
def main(request):
    return HttpResponse(render(request, 'youtube_downloader/index_.html'))


def seasonal_menu(request):
    seasonal_manages = Manage.objects.filter(category=1)
    return HttpResponse(render(request, 'youtube_downloader/seasonal_menu.html', {
        'seasonal_manages': seasonal_manages
    }))


def banquet_menu(request):
    banquet = Manage.objects.filter(category=2)
    return HttpResponse(render(request, 'youtube_downloader/banquet_menu.html', {
        'banquet': banquet
    }))


def wine_map(request):
    winne_manage = Manage.objects.filter(category=5)
    return HttpResponse(render(request, 'youtube_downloader/wine_map.html', {
        'winne_manage': winne_manage
    }))


class Alcoholic(ListView):
    template_name = 'youtube_downloader/Alcoholic.html'
    model = Manage
    context_object_name = 'alcoholic_manage'
    # allow_empty = False
    def get_queryset(self):
        # return super().get_queryset().filter(category=4)
        return Manage.objects.filter(category=4)




def Beverages(request):
    beverages = Manage.objects.filter(category=7)
    return HttpResponse(render(request, 'youtube_downloader/Beverages.html', {
        'beverages': beverages
    }))


def about_as(request):
    if request.method == 'POST':
        form = Review(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            feedback = Review(
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                review=form.cleaned_data['review'],
                rating=form.cleaned_data['rating']
            )
            feedback.save()
            return HttpResponseRedirect('/about_as')
    form = Review()
    return HttpResponse(render(request, 'youtube_downloader/about_as_.html', {
        'form': form
    }))


def videos(request):
    return HttpResponse(render(request, 'youtube_downloader/videos_.html'))


def post(request, id: int):
    return HttpResponse(render(request, 'youtube_downloader/description_.html'))


# def product(request, id: int):
#     product = Manage.objects.get(pk=id)
#     a = 0
#     context = {
#         'product': product
#     }
#     session_key = request.session.session_key
#     if not session_key:
#         request.session["session_key"]=123
#         request.session.cycle_key()
#         print(request.session.session_key)
#     return render(request, 'youtube_downloader/manage.html', context)

class Product(DeleteView):
    template_name = 'youtube_downloader/manage.html'
    model = Manage
    # product = Manage.objects.get(pk=id)
    # a = 0
    # context = {
    #     'product': product
    # }
    # session_key = request.session.session_key
    # if not session_key:
    #     request.session["session_key"]=123
    #     request.session.cycle_key()
    #     print(request.session.session_key)
    # return render(request, 'youtube_downloader/manage.html', context)
# --------------------------------------------------------------------------------------

# def basket_adding(request):
#     return_dict = dict()
#     session_key = request.session.session_key
#     data = request.POST
#     product_id = data.get("product_id")
#     nmb = data.get("nmb")
#     is_delete = data.get("is_delete")
#     if is_delete == 'true':
#         ProductInBasket.objects.filter(id=product_id).update(is_active=False)
#
#     else:
#         new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id,
#                                                                      is_active=True, defaults={"nmb": nmb})
    #     if not created:
    #         new_product.nmb += int(nmb)
    #     new_product.save(force_update=True)
    #
    # products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    # products_total_nmb = products_in_basket.count()
    # return_dict["products_total_nmb"] = products_total_nmb
    #
    # return_dict["products"] = list()
    # for item in products_in_basket:
    #     product_dict = dict()
    #     product_dict["id"] = item.id
    #     product_dict["name"] = item.product.name
    #     product_dict["price_per_item"] = item.price_per_item
    #     product_dict["nmb"] = item.nmb
    #     return_dict["products"].append(product_dict)
    # return JsonResponse(return_dict)
