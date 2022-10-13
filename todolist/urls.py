from todolist.views import create_task_ajax, delete_task_ajax, register, login_user, show_todolist, logout_user, create_task, show_todolist_ajax, task_status, delete_task, show_json
from django.urls import path

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('create-task/', create_task, name='create_task'),
    path('task-status/<int:id>', task_status, name='task_status'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
    path('logout/', logout_user, name='logout'),
    path('json/', show_todolist_ajax, name='show_todolist_ajax'),
    path('show-json/', show_json, name='show_json'),
    path('create-task-ajax/', create_task_ajax, name='create_task_ajax'),
    path('delete-task-ajax/<int:id>', delete_task_ajax, name='delete_task_ajax'),
]