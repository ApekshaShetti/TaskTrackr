from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

class Login(LoginView):
    template_name = 'Tasks/login.html'
    fields = '__all__'
    redirect_authenticated_user = True   # the page will be redirected once loggedin

    def get_success_url(self):
        return reverse_lazy('task_list')

class TaskList(LoginRequiredMixin, ListView):
    model = Task 
    context_object_name = 'task_list'

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task 
    context_object_name = 'task'
    template_name = 'Tasks/task.html'
    
class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task_list')  # redirect to task list page


class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task_list')  # redirect to task list page

class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task_delete'
    success_url = reverse_lazy('task_list')  # redirect to task list page






