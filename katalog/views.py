from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    data_katalog_item = CatalogItem.objects.all()
    context = {
        'list_barang': data_katalog_item,
        'nama': 'Jihan Syafa Kamila',
        'NPM' : '2106751303'
    }
    return render(request, "katalog.html", context)
