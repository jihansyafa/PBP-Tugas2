from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from todolist.models import Task


@login_required(login_url='/todolist/login/')
def show_todolist(request):
    todolist_data = Task.objects.filter(user=request.user)
    context = {
        'todolist_data': todolist_data,
        'user' : request.user,
        'last_login': request.COOKIES['last_login']
    }
    return render(request, "todolist.html", context)


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


@login_required(login_url='/todolist/login/')
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


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response