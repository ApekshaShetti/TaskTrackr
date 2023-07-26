from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy


class TaskList(ListView):
    model = Task 
    context_object_name = 'task_list'

class TaskDetail(DetailView):
    model = Task 
    context_object_name = 'task'
    template_name = 'Tasks/task.html'
    
class CreateTask(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task_list')  # redirect to task list page


class UpdateTask(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task_list')  # redirect to task list page

class DeleteTask(DeleteView):
    model = Task
    context_object_name = 'task_delete'
    success_url = reverse_lazy('task_list')  # redirect to task list page






