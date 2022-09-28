# **Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django**

**Nama   : Jihan Syafa Kamila**

**NPM    : 2106751303**

**Kelas  : B**

# Link Tugas 4

🔗[**To Do List**](https://pbp-tugas2-jihansyafakamila.herokuapp.com/todolist/)

# Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

CSRF (_Cross Site Request Forgery_) merupakan salah satu serangan (_attack_) yang dapat menyerang sebuah situs web. _Built in protection_ yang dimiliki Django, yaitu `csrf_token`, berfungsi adalah untuk mengatasi kemungkinan terjadinya serangan tersebut. Pengimplementasiannya cukup dilakukan dengan menambahkan potongan kode `{% csrf_token %}` ke dalam _tag_ `<form>` di `template`.

```
<form method="POST" action="">
    {% csrf_token %}
    <table>
        <div class="txt_field">
            Username
            <input type="text" name="username" placeholder="Your Username" class="form-control">
        </div>
    ...
```

`{% csrf_token %}` menghasilkan sebuah token di sisi server saat merender halaman sehingga jika terdapat permintaan, maka akan diperiksa apakah permintaan berisi token. 

Apabila `{% csrf_token %}` tidak ditambahkan ke dalam tag `<form>` maka permintaan tidak akan dieksekusi atau web akan _reject_ permintaan dengan mengeluarkan error. Selain itu, _attacker_ dapat menggunakan _user's authenticated state_ untuk memaksa pengeksekusian tindakan atau pengiriman permintaan yang tidak sesuai dengan keingan _user_. Jika permintaan yang tidak diinginkan oleh _user_ tersebut berhasil dieksekusi, maka serangan tersebut dapat membahayakan situs web.

# Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Bagaimana cara membuat <form> secara manual?

Elemen `<form>` dapat dibuat secara manual tanpa menggunakan generator seperti `{{ form.as_table }}`. Berikut adalah gambaran besar cara membuat `<form>` secara manual.

1. Memanfaatkan tag `<form>` untuk membuat form di file HTML.

2. Menentukan _action_ dan _method_ dengan menambahkannya sebagai atribut. _Action_ ini berperan sebagai pengiriman data form untuk diproses. Sedangkan, _method_ ("POST" atau "GET") fungsinya untuk menjelaskan bagaimana data form akan dikirim oleh web.

3. Menambahkan elemen input untuk keperluan form, di mana elemen-elemen input ini nantinya akan diisi oleh _user_.

4. Data yang diterima akan dicatat oleh form sehingga apabila _user_ melakukan _submit_ maka form akan dikirim sesuai dengan deklarasi action dan method yang sudah dilakukan sebelumnya.

# Proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

1.  Input dari user, sesuai dengan permintaan form, akan dibawa oleh _request_ yang nantinya akan disimpan ke dalam suatu variable oleh fungsi tujuan di `views.py`. 

2. Akan diinisasi objek baru sesuai dengan _request_ dari _user_ (input data dari _user_). Objek tersebut dapat disimpan ke dalam database menggunakan perintah `<objek>.save()`

```
if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
```

3. Pengambilan objek dilakukan oleh `views.py` melalui `models.py` yang akan mengambil data yang sesuai dengan data user dari database. Contohnya adalah menggunakan perintah `Task.objects.filter(user=request.user)`. Pada perintah tersebut, dilakukan filter objek agar data yang diambil sesuai dengan _current user_.

4. Selanjutnya data yang tersimpan akan di-_render_ ke HTML untuk menampilkan halaman yang ingin ditampilkan kepada _user_

# Implementasi Langkah-Langkah Pengerjaan Tugas 4

**✅ Membuat suatu aplikasi baru bernama `todolist` di proyek tugas Django yang sudah digunakan sebelumnya.**

Aplikasi django bernama `todolist` dapat dibuat dengan memasukkan command di bawah ke _command promt_ pada direktori Tugas 2 PBP.

```
python manage.py startapp todolist
```

**✅ Menambahkan path `todolist` sehingga pengguna dapat mengakses http://localhost:8000/todolist**

```
urlpatterns = [
...
path('todolist/', include('todolist.urls')),
]
```
Path todolist dapat ditambahkan dengan memasukkan path todolist ke urlpattern pada file `urls.py` yang berada pada folder `project-django`

**✅ Membuat sebuah model Task yang memiliki atribut user, date, title, description.**

Membuat sebuah model Task dapat dilakukan dengan membuat class dan atribut yang dibutuhkan. Hal ini dapat dilakukan dengan menambahkan potongan kode berikut pada `models.py` di dalam folder `todolist`.

```
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
```
Selanjutnya perintah `python manage.py makemigrations` untuk menyiapkan migrasi skema model ke dalam database Django lokal dan `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.

**✅ Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.**

Membuat fungsi bernama `register`, `login_user`, dan `logout_user` pada file `views.py` yang menerima parameter request. Beberapa fungsi ini membutuhkan modul-modul yang dapat digunakan dengan meng-_import_ modul-modul yang dibutuhkan.

- Registrasi
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully made an account!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)
```
Fungsi pada `views.py` ini mengarah ke `register.html`, di mana terdapat form register.

```
<form method="POST" >  
    <setfield>
    {% csrf_token %}  
    <table>  
        {{ form.as_table }}  
        <tr>  
            <td></td>
            <td><input type="submit" name="submit" value="Register"/></td>  
        </tr>  
    </table> 
    </setfield> 
</form>
```

- Login
```
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # melakukan login terlebih dahulu
            login(request, user) 
            # membuat response
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
            # membuat cookie last_login dan menambahkannya ke dalam response
            response.set_cookie('last_login', str(datetime.datetime.now())) 
            return response

        else:
            messages.info(request, 'Wrong username or password!')
    context = {}
    return render(request, 'login.html', context)
```
Fungsi pada `views.py` ini mengarah ke `login.html`, di mana terdapat form register.

```
<form method="POST" action="">
    {% csrf_token %}
    <table>
        <div class="txt_field">
            Username
            <input type="text" name="username" placeholder="Your Username" class="form-control">
        </div>
                
        <div class="txt_field">
            Password
            <input type="password" name="password" placeholder="Your Password" class="form-control">
        </div>

        <tr>
            <input class="btn login_btn" type="SUBMIT" value="Login">
        </tr>
    </table>
</form>
```

- Logout
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response
```

Menambahkan tombol untuk logout di `todolist.html`

```
<a href="{% url 'todolist:logout' %}">
<button class = "logout-button">Logout</button></a></td>
```

**✅ Membuat halaman utama todolist.**

Membuat fungsi bernama `show_todolist`,  pada file `views.py` yang menerima parameter request. 

```
def show_todolist(request):
    todolist_data = Task.objects.filter(user=request.user)
    context = {
        'todolist_data': todolist_data,
        'user' : request.user
    }
    return render(request, "todolist.html", context)
```

Lalu, membuat halaman utama todolist pada file `todolist.html` di `templates`. Halaman todolist ini memuat atribut username, tombol create new task, tombol logout, serta tabel yang berisi judul task, deskripsi task, tanggal pembuatan task, status task, dan opsi untuk menghapus task. Atribut-atribut ini lalu disusun agar tampilan sesuai dengan yang diinginkan



**✅ Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.**

Membuat fungsi bernama `show_todolist`,  pada file `views.py` yang menerima parameter request. 

```
def create_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
        )
        return redirect('todolist:show_todolist')
    return render(request, 'create_task.html')
```

Lalu, membuat halaman untuk form create new task todolist pada file `create_task.html` di `templates`. Form dibuat secara manual, di mana tampilan disesuaikan dengan apa yang ingin diperlihatkan kepada _user_.

**✅ Membuat routing sehingga beberapa fungsi dapat diakses melalui URL masing-masing.**

Menambahkan path berikut ini ke urlpatterns untuk melakukan routing sehingga fungsi `show_todolist`, `login_user`, `register`, `create_task`, `delete_task` dan `logout_user` dapat diakses.

```
urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('create-task/', create_task, name='create_task'),
    path('task-status/<int:id>', task_status, name='task_status'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
    path('logout/', logout_user, name='logout'),
]
```

**✅ Melakukan deployment ke Heroku supaya dapat diakses melalui internet**

Terlebih dahulu melakukan add, commit, dan push ke repository github. Pada tugas ini, tinggal dilakukan deploy karena kita menggunakan aplikasi Heroku yang sama dengan tugas sebelumnya, Setelah berhasil, kita dapat mengakses link proyek aplikasi melalui link herokuapp yang kita buat.

**✅ Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.**

![user2_todolist](https://user-images.githubusercontent.com/88375711/192874500-7d530ef0-fd1f-478d-a2a3-466b8243e1ac.jpg)
![User1_todolist](https://user-images.githubusercontent.com/88375711/192874506-6fdbd656-72c4-48e9-88ec-ae8b2ff66e0a.jpg)


# Implementasi Bonus

- Membuat atribut is_finished pada model Task (dengan default value False).

```
is_finished = models.BooleanField(default=False)
```

- Membuat dua kolom baru pada tabel task yang berisi status penyelesaian task dan tombol untuk mengubah status penyelesaian suatu task menjadi Selesai atau Belum Selesai.

```
{% for task in todolist_data %}
<tr>
    <td>
        <button><a href="task-status/{{task.pk}}">Change</a></button>
    </td>

    {% if task.is_finished == True%}
    <td>✅Done</td>
    {% else %}
    <td>❌Not Done</td>
    {% endif %}

    ...
```
Button ubah status akan diproses oleh fungsi` task_status` dengan potongan kode berikut.

```
def task_status(request, id):
    task = Task.objects.get(id=id)
    task.is_finished = not task.is_finished
    task.save(update_fields=["is_finished"])
    return redirect('todolist:show_todolist')
```

- Menambahkan kolom baru pada tabel task yang berisi tombol untuk menghapus suatu task.

```
<td>
    <a href="delete-task/{{task.pk}}"><button>🗑️</button></a></td>
</td>
```

Button hapus akan diproses oleh fungsi `delete_task` dengan perintah `task.delete()`.