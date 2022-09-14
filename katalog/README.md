# **PBP Tugas 2**

**Nama   : Jihan Syafa Kamila**

**NPM    : 2106751303**

**Kelas  : B**



## Link deploy Tugas 2 : 
**http://pbp-tugas2-jihansyafakamila.herokuapp.com/katalog/**

#

## Bagan Alur Request ke Web Aplikasi Berbasis Django
![Gambar]('../../BaganTugas2.png?raw=true')

Penjelasan :

1. Ketika *client* atau *user* melakukan *request* URL, sesuai dengan halaman yang ingin ditampilkan, maka *request* tersebut akan diproses melalui urls.py.

2. Pada urls.py terdapat definisi alamat URL yang di *request* beserta fungsi yang akan melakukan *handle* setiap *route*.

3. Permintaan akan diproses di views.py yang memiliki fungsi untuk memanggil data dari Models dan menyusun tampilan data pada Template. 

4. Database akan mengembalikan data ke Models yang nantinya dapat di-*import* oleh Views.

5. Templates dapat menerima data yang dikirim dari Views. Templates ini berisikan *file* HTML yang tampilannya akan dikembalikan ke Django dan ditampilkan kepada *client*. 

#

## Alasan menggunakan Virtual Environment

- *Virtual environment* merupakan sebuah *tools* atau alat yang berfungsi untuk pembuatan lingkungan yang terisolasi untuk sebuah proyek. *Virtual environment* ini akan mengisolasi *dependencies* yang dibutuhkan oleh sebuah proyek yang terisolasi atau terpisah dari proyek yang lain. Dengan demikian, perubahan yang dilakukan pada satu proyek tidak akan mempengaruhi proyek lain.

- Sebuah aplikasi web berbasis Django tetap dapat dibuat tanpa menggunakan *virtual environment*. Namun, tetap perlu dipastikan bahwa modul-modul atau *libraries* global yang berada di perangkat, tempat untuk menjalankan aplikasi, memiliki *dependencies* yang sama dengan *dependencies* yang dibutuhkan oleh aplikasi tersebut.

#

## Implementasi Langkah-Langkah Pengerjaan Tugas 2


1. Membuat fungsi `show_catalog()` yang menerima parameter "request" pada *file* `views.py` yang berada di folder `katalog`.

``` 
def show_catalog(request):
    data_katalog_item = CatalogItem.objects.all()
    context = {
        'list_barang': data_katalog_item,
        'nama': 'Jihan Syafa Kamila',
        'NPM' : '2106751303'
    }
    return render(request, "katalog.html", context)  
```
Di dalam show_katalog() ini, objek-objek dari class CatalogItem disimpan dalam variabel data_katalog_item. Lalu, data-data tersebut disimpan dalam sebuah dictionary bernama "context" dengan key-nya, yaitu 'list_barang', 'nama', dan 'NPM' yang akan di-'render' ke dalam `katalog.html`

2. Membuat sebuah *routing* untuk memetakan fungsi. *Routing* dilakukan dengan mengisi *file* `urls.py` yang ada pada folder katalog dengan potongan kode sebagai berikut.

```
from django.urls import path
from katalog.views import show_catalog

app_name = 'katalog'

urlpatterns = [
    path('', show_catalog, name='show_catalog'),
]
```
Isi dari urlpatterns dimodifikasi dengan menambahkan path baru. Selain itu, pada `urls.py` di folder `project_django`, juga ditambahkan path dengan parameter "katalog/" yang mengarahkan kepada alamat katalog.url.

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path('katalog/', include('katalog.urls')),
]
```

3. Memetakan data yang di-render dari fungsi show_catalog() ke dalam HTML. Memetakan data ke HTML ini dilakukan dengan memodifikasi isi dari *file* `katalog.html`

```
<h5>Name: </h5>
<p>{{nama}}</p>

<h5>Student ID: </h5>
<p>{{NPM}}</p>
```

```
{% for barang in list_barang %}
<tr>
    <td>{{barang.item_name}}</td>
    <td>{{barang.item_price}}</td>
    <td>{{barang.item_stock}}</td>
    <td>{{barang.rating}}</td>
    <td>{{barang.description}}</td>
    <td>{{barang.item_url}}</td>
</tr>
{% endfor %}
```

4. Melakukan **aplikasi katalog** deployment ke Heroku. Hal ini dilakukan dengan pertama membuat aplikasi di Heroku. Kedua, menyimpan informasi API key dan nama aplikasi yang telah dibuat ke dalam settings-secret repository project milik kita sebagai data pribadi. Ketiga, melakukan deploy ke Heroku pada actions repository. Setelah berhasil, kita dapat mengakses link proyek aplikasi. Dengan demikian, kita tidak perlu lagi menjalankan aplikasi secara lokal dan aplikasi yang telah kita buat dapat dilihat oleh publik.