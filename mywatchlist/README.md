# **Tugas 3: Pengimplementasian Data Delivery Menggunakan Django**

**Nama   : Jihan Syafa Kamila**

**NPM    : 2106751303**

**Kelas  : B**

# Link Tugas 3

🔗[**HTML**](https://pbp-tugas2-jihansyafakamila.herokuapp.com/mywatchlist/html/)

🔗[**XML**](https://pbp-tugas2-jihansyafakamila.herokuapp.com/mywatchlist/xml/)

🔗[**JSON**](https://pbp-tugas2-jihansyafakamila.herokuapp.com/mywatchlist/json/)

# Perbedaan antara JSON, XML, dan HTML

1. JSON (_JavaScript Object Notation_) merupakan format data yang menerjemahkan bahasa pemrograman sehingga dapat digunakan untuk menyimpan dan mengirim data dari sebuah server yang nantinya dapat ditampilkan di halaman sebuah web. Data pada JSON disimpan dalam bentuk _key_ dan _value_.

Contoh :

```
{
    "watched": "Watched", 
    "title": "Harry Potter and The Philosopher's Stone", 
    "rating": "5", 
    "release_date": "November 19th, 2001", 
    "review": "Harry Potter an The Philosopher's Stone, a mix of fantasy and adventure, is the perfet opening for the rest of the Harry Potter Movies. Watching this movie was magical and it is definitely a fun watch."
}
```

2. XML (_Extensible Markup Language_) merupakan bahasa markup yang juga digunakan untuk menyimpan dan mengirim data. Berbeda dengan JSON, XML memiliki format yang mirip dengan HTML, yaitu informasi yang dibungkus di dalam _tag_. Namun, meskipun mirip dengan HTML, XML dirancang untuk fokus pada pengiriman dan penyimpanan data sedangkan HTML dirancang untuk fokus pada penampilan data.

Contoh :

```
<django-objects version="1.0">
<object model="mywatchlist.mywatchlist" pk="1">
<field name="watched" type="CharField">Watched</field>
<field name="title" type="TextField">Harry Potter and The Philosopher's Stone</field>
<field name="rating" type="CharField">5</field>
<field name="release_date" type="CharField">November 19th, 2001</field>
<field name="review" type="TextField">Harry Potter an The Philosopher's Stone, a mix of fantasy and adventure, is the perfet opening for the rest of the Harry Potter Movies. Watching this movie was magical and it is definitely a fun watch.</field>
</object>
```

3.  HTML (_Hypertext Markup Language_) merupakan sebuah bahasa markup standar yang digunakan untuk membuat halaman web. Berbeda dengan XML dan JSON, HTML tidak memiliki sintaks penyimpanan dan pengiriman data. Selain itu, elemen-elemen pada HTML ini akan memberi pemberitahuan kepada browser untuk menampilkan konten pada halaman sebuah situs web.

Contoh :

```
<h5>Name: Jihan Syafa Kamila</h5>
<h5>Student ID: 2106751303</h5>
```

# Mengapa kita memerlukan _data delivery_ dalam pengimplementasian sebuah platform?
Sebuah aplikasi membutuhkan cara untuk menyimpan data ke dalam database. Hal ini dikarenakan adanya perubahan-perubahan yang menyangkut data, seperti menyimpan atau mengirim data dari suatu stack ke stack lain. HTML, XML, serta JSON berfungsi sebagai perantara pertukaran data antara back-end dengan front-end. _Data delivery_ memungkinkan pengambilan data dari back-end dapat dilakukan dengan cepat yang nantinya akan ditampilkan pada front-end.

# Pengimplementasian Checklist dari Tugas 3

📝 Membuat suatu aplikasi baru bernama `mywatchlist` di proyek Django Tugas 2 pekan lalu

Aplikasi django bernama mywatchlist dapat dibuat dengan memasukkan command di bawah ke _command promt_ pada direktori Tugas 2 PBP.

```python manage.py startapp mywatchlist```

📝 Menambahkan path `mywatchlist` sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist

```
urlpatterns = [
...
path('mywatchlist/', include('mywatchlist.urls')),
]
```
Path mywatchlist dapat ditambahkan dengan memasukkan path mywatchlist ke urlpattern pada file `urls.py` yang berada pada folder `project-django`

📝 Membuat sebuah model MyWatchList yang memiliki atribut sebagai watched, title, rating, release_date, rdan review

Membuat sebuah model MyWatchList dapat dilakukan dengan membuat class dan atribut yang dibutuhkan untuk setiap tipe data watched, title, rating, release_date, dan review. Hal ini dapat dilakukan dengan menambahkan potongan kode berikut pada `models.py` di dalam folder `mywatchlist`.

```
class MyWatchlist(models.Model):
    watched = models.CharField(max_length=30)
    title = models.TextField()
    rating = models.CharField(max_length=5)
    release_date = models.CharField(max_length=50)
    review = models.TextField()
```

Selanjutnya perintah `python manage.py makemigrations` untuk menyiapkan migrasi skema model ke dalam database Django lokal dan `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.

📝 Menambahkan minimal 10 data untuk objek MyWatchList

Folder bernama `fixtures` perlu dibuat terlebih dahulu di dalam folder `mywatchlist`. Di dalam folder fixtures itu, dibuat file JSON baru bernama intial_mywatchlist_data.json yang berisikan data dan atribut-atribut terkait sebuah film.

```
[
    {
        "model": "mywatchlist.mywatchlist",
        "pk": 1,
        "fields": {
            "watched": "Watched",
            "title": "Harry Potter and The Philosopher's Stone",
            "rating": 5,
            "release_date": "November 19th, 2001",
            "review": "Harry Potter an The Philosopher's Stone, a mix of fantasy and adventure, is the perfet opening for the rest of the Harry Potter Movies. Watching this movie was magical and it is definitely a fun watch."
        }
    },
    ...
]
```
Setelah itu perlu ditambahkan perintah `python manage.py loaddata initial_mywatchlist_data.json` untuk memasukkan data tersebut ke dalam database Django lokal. Selanjutnya potongan kode `release: sh -c 'python manage.py migrate` dan `python manage.py loaddata initial_mywatchlist_data.json` ditambahkan pada file `Procfile`.

📝 Menyajikan data yang telah dibuat sebelumnya dalam tiga format, yaitu HTML, JSON, dan XML.

Membuat 3 fungsi di file `views.py` dalam folder mywatchlist, yaitu show_mywatchlist, show_json, dan show_xml untuk menyajikan data dalam fromat HTML, JSON, dan XML.

- HTML

```
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
```

- JSON

```
def show_json(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

- XML

```
def show_xml(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

📝 Membuat routing sehingga data di atas dapat diakses melalui URL.

Menambahkan path berikut ini ke urlpatterns untuk melakukan routing untuk menampilkan halaman HTML, JSON, dan XML pada browser.

```
from django.urls import path
from mywatchlist.views import show_mywatchlist, show_xml, show_xml_by_id, show_json, show_json_by_id

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
]
```

# Screeshot pengaksesan URL menggunakan Postman

- HTML
![Screenshot (482)](https://user-images.githubusercontent.com/88375711/191636208-75fb1b8d-889b-4346-b3ce-0bae2a359eb1.png)

- XML
![Screenshot (483)](https://user-images.githubusercontent.com/88375711/191636212-0cd7faaa-d611-4c4d-a422-62a70438ffa1.png)

- JSON
![Screenshot (484)](https://user-images.githubusercontent.com/88375711/191636215-9dd8e012-77ae-494d-bda5-91e49fceb1b5.png)
