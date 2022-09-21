from django.shortcuts import render
import mywatchlist
from mywatchlist.models import MyWatchlist
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    data_watchlist = MyWatchlist.objects.all()

    amount = 0
    for movie in data_watchlist:
        if movie.watched == "Watched":
            amount += 1
    if amount >= 5:
        message = "Selamat, kamu sudah banyak menonton!"
    else:
        message = "Wah, kamu masih sedikit menonton!"

    context = {
        'list_data': data_watchlist,
        'nama': 'Jihan Syafa Kamila',
        'NPM' : '2106751303',
        'message' : message
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MyWatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")