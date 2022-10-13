# **Tugas 6: Javascript dan AJAX**

**Nama   : Jihan Syafa Kamila**

**NPM    : 2106751303**

**Kelas  : B**

# Perbedaan Asynchronous dengan Synchronous Programming

_Asynchronous programming_ adalah proses jalannya sebuah program secara bersamaan tanpa harus menunggu proses antrian karena program tidak melakukan eksekusi baris satu persatu. Pada _asynchronous programming_, program dapat berjalan tanpa harus terikat dengan pekerjaan lain sehinggan suatu program dapat dieksekusi secara paralel.

_Synchronous programming_ adalah proses jalannya program secara _sequential_ di mana program harus menunggu proses antrian karena eksekusi program dilakukan satu per satu sesuai dengan urutan dan prioritasnya. Pada _synchronous programming_, setiap pekerjaan saling terikat, dengan maksud suatu pekerjaan harus menunggu pekerjaan lain selesai terlebih dahulu, sehingga waktu eksekusi program berlangsung lebih lama.

# Penerapan Paradigma Event-Driven Programming dan contohnya

_Event-driven programming_ merupakan suatu paradigma pemrograman yang alur programnya ditentukan oleh suatu event yang merupakan keluaran atau tindakan pengguna, atau bisa berupa pesan dari program lainnya.

Contohnya adalah sebuah _button_ di tekan, maka akan dijalankan fungsi yang sesuai setiap kali _button_ ditekan. Fungsi ini dapat berjalan ketika terdapat suatu _event_, dalam kasus ini _event_ nya adalah menekan tombol atau _click button_. Penerapan pada tugas ini adalah ketika pengguna menekan tombol `Create New Task` maka program akan menampilkan sebuah form. Ketika pengguna mengisi form tersebut dan menekan tombol `Add Task`, program akan menambahkan data baru ke dalam `Todolist`. _Button_ atau tombol yang ditekan ini disebut sebagai _event_.

# Penerapan Asynchronous Programming pada AJAX

AJAX merupakan singkatan dari Asynchronous Javascript and XML dan mengacu pada sekumpulan teknis pengembangan web. Ketika sebuah _event_ terjadi, event tersebut akan mengakibatkan sebuah fungsionalitas AJAX dijalankan. AJAX akan mengirimkan sebuah _request_ ke server, dan melanjutkan eksekusi tanpa menunggu balasan dari server terlebih dahulu. Misalnya, pada penerapan tugas ini ketika mengklik _button_ `Add Task` untuk menambahkan _task_ baru, maka akan dilakukan AJAX POST untuk mengirim data ke server. Setelah server selesai mengolah data tersebut, akan dijalankan callback function yang telah dibuat sebelumnya.

# Implementasi Checklist dan BONUS

1. Membuat _view_ baru yang mengembalikan seluruh data task dalam bentuk JSON.

Membuat fungsi baru bernama `show_json` untuk mengembalikan seluruh data berupa json sesuai dengan `user` yang sedang login.

```
def show_json(request):
    data = Task.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

2. Membuat path `/todolist/json` yang mengarah ke view yang baru dibuat.

Menambahkan potongan kode berikut ke dalam `urlpatterns` di `urls.py`.

```
path('show-json/', show_json, name='show_json'),
```

3. Membuat template baru bernama todolist_ajax.html untuk template yang menerapkan konsep AJAX dan mengarahkan url utama dari /todolist ke todolist_ajax.html

4. Membuat fungsi baru di views.py, yaitu `show_todolist_ajax`, `create_task_ajax`, dan `delete_task_ajax` dan membuat path yang mengarah ke pada fungsi-fungsi tersebut.

5. Mengimplementasikan AJAX dengan menambahkan potongan kode berikut di todolist_ajax.html yang dipanggil pada akhir potongan kode.

```
async function getTodolist() {
        return fetch("{% url 'todolist:show_json' %}").then((res) => res.json())
    }

async function refreshTodolist() {
    document.getElementById("todolistCards").innerHTML = ""
    const todolist = await getTodolist()
    let htmlString = ``

    todolist.forEach((task) => {
        htmlString += `\n
        <div class = "set-responsive">
            <div class = "card">
                <p class = "task-title">${task.fields.title}</p>
                <p class = "task-description">${task.fields.description}</p>
                <p class = "task-date"> Created on : ${task.fields.date}</p>

                <div class="button-task">
                    <button class="button">
                        <a onclick="deleteTodolist(${task.pk})">Delete</a>
                    </button>
                </div>
            </div>
        </div>
        ` 
    })
    document.getElementById("todolistCards").innerHTML = htmlString

    ...

    refreshTodolist()
}
```

6. Membuat fungsi bernama `addTodolist`, `showModal`, `cancelButton`, `deleteTodolist` (menerima parameter id), untuk menerapkan secara berturut-turut penambahan task pada todolist, penampilan modal, penutupan modal ketika button cancel ditekan, dan penghapusan task.

```
function addTodolist() {
        document.getElementById('title_input').value = ''
        document.getElementById('desc_input').value = ''

        document.getElementById('modal_container').style.display = "none"
        fetch("{% url 'todolist:create_task_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#new_form'))
        }).then(refreshTodolist)
        return false
    }

function showModal() {
    document.getElementById('modal_container').style.display = "flex"
}

function cancelButton() {
    document.getElementById('modal_container').style.display = "none"
}

function deleteTodolist(id) {
    let url = "/todolist/delete-task-ajax/" + id;
    fetch(url).then(refreshTodolist)
}

document.getElementById('new-task-button').onclick = showModal
document.getElementById('btn_cancel').onclick = cancelButton
document.getElementById('create_task').onclick = addTodolist

```

7. Membuat modal yang akan membuka sebuah form ketika tombol `Add Task` diklik.

```
<div id="modal_container" class="modal_container"> 
    <div id="modal" class="modal">
        <div class = "create_task">

            <h1>Create New Task</h1>

            <form id="new_form" method="POST" action="/todolist/create-task-ajax/">
                <setfield>
                {% csrf_token %}
                <table>
                    <div class="txt_field">
                        Task Title :
                        <input id="title_input" type="text" name="title" placeholder="Enter Your Task Title" class="form-control">
                    </div>
                            
                    <div class="txt_field">
                        Description :
                        <input id="desc_input" type="text" name="description" placeholder="Enter Your Task Description" class="form-control">
                    </div>

                    <input id="create_task" class="btn create_task" type="SUBMIT" value="Add Task">

                </table>
                </setfield>
            </form>
            <button id="btn_cancel" class="btn btn_cancel">Cancel</button>
        </div>
    </div>
</div>
```

Berikut adalah _styling_ dari modal pada file `todolist.css`

```
.modal_container {
    background-color: rgba(0, 0, 0, 0.733);
    top: 0;
    left: 0;
    height: 100vh;
    width: 100vw;
    position: fixed;
    display: flex;
    justify-content: center;
    align-items: center;
    display: none;
    transition: 1s;
}

.modal {
    background-color: #ffffff;
    position: fixed;
    max-width: 100%;
    padding-left: 30px;
    padding-right: 30px;
    padding-bottom: 30px;
    border-radius: 10px 10px 10px 10px;
    overflow: hidden;
    text-align: center;
}

form .txt_field {
    position: center;
    border-bottom: 2px solid #adadad;
    margin: 30px;
    padding: 5px;
}
  
.txt_field input {
    width: 100%;
    padding: 0 5px;
    height: 40px;
    font-size: 16px;
    border-radius: 15px;
    border: none;
    outline: none;
    background: none;
}

input[type="SUBMIT"] {
    width: 30%;
    height: 40px;
    border: 1px solid;
    background: #d17ea3;
    border-radius: 15px;
    font-size: 14px;
    color: #ffffff;
    font-weight: bold; 
    font-family: 'Poppins';
    margin-bottom: 15px;
}
  
input[type="submit"]:hover {
    border-color: #000000;
    transition: .5s;
    cursor: pointer;
}

.btn_cancel {
    background-color: #707070;
    width: 30%;
    height: 40px;
    border: 1px solid;
    border-radius: 15px;
    font-size: 14px;
    color: #ffffff;
    font-weight: bold; 
    font-family: 'Poppins';
    margin-bottom: 15px;
}

.btn_cancel:hover {
    border-color: #000000;
    transition: .5s;
    cursor: pointer;
}
```

Form modal akan terhubung pada path `create-task-ajax/` yang mengarah kepada fungsi `create_task_ajax` di `views.py`.

Modal akan tertutup secara otomatsi ketika pengguna berhasil menambahkan task baru.

- BONUS
Untuk implementasi bonus, saya membuat fungsi `delete_task_ajax`.

```
@login_required(login_url="/todolist/login/")
def delete_task_ajax(request, id):
    task = Task.objects.filter(user=request.user).get(id=id)
    task.delete()
    return HttpResponse(b"DELETED", status=204)

```

Lalu menambahkan path baru yang mengarah pada fungsi di atas.

```
path('delete-task-ajax/<int:id>', delete_task_ajax, name='delete_task_ajax'),
```

Pada file `todolist_ajax.html` dibuat sebuah fungsi bernama `deleteTodolist` yang menerima parameter id (potongan kode ada di poin nomor 6). Fungsi ini akan menutup modal ketika button `cancel` ditekan.