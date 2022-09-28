from todolist.views import register, login_user, show_todolist, logout_user, create_task, task_status, delete_task
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
]