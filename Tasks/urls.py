from django.urls import path
from .views import TaskList, TaskDetail, CreateTask, UpdateTask, DeleteTask

urlpatterns = [
    path('',TaskList.as_view(), name='task_list'),
    path('task/<int:pk>/',TaskDetail.as_view(), name='task'),  # dynamic routing
    path('create-task/',CreateTask.as_view(), name='create-task'),
    path('update-task/<int:pk>/',UpdateTask.as_view(), name='update-task'),
    path('delete-task/<int:pk>/',DeleteTask.as_view(), name='delete-task'),
]