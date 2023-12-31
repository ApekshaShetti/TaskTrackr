from django.urls import path
from .views import TaskList, CreateTask, UpdateTask, DeleteTask, Login, Register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',Login.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('register/',Register.as_view(), name='register'),
    path('',TaskList.as_view(), name='task_list'),
    # path('task/<int:pk>/',TaskDetail.as_view(), name='task'),  # dynamic routing
    path('create-task/',CreateTask.as_view(), name='create-task'),
    path('update-task/<int:pk>/',UpdateTask.as_view(), name='update-task'),
    path('delete-task/<int:pk>/',DeleteTask.as_view(), name='delete-task'),
]