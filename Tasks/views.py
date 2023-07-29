from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class Login(LoginView):
    template_name = 'Tasks/login.html'
    fields = '__all__'
    redirect_authenticated_user = True   # the page will be redirected once loggedin

    def get_success_url(self):
        return reverse_lazy('task_list')


class Register(FormView):
    template_name = 'Tasks/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True   # the page will be redirected once loggedin
    success_url = reverse_lazy('task_list')  # redirect to task list page


    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task_list')
        return super(Register,self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Task 
    context_object_name = 'task_list'

    # this function is created so that the user will be able to see only their data and not of anyone else
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = context['task_list'].filter(user=self.request.user)
        context['count'] = context['task_list'].filter(status=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['task_list'] = context['task_list'].filter(title__startswith=search_input)

        context['search_input'] = search_input
        return context

# class TaskDetail(LoginRequiredMixin, DetailView):
#     model = Task 
#     context_object_name = 'task'
#     template_name = 'Tasks/task.html'
    
class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title','description','status']
    success_url = reverse_lazy('task_list')  # redirect to task list page

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask, self).form_valid(form)

class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title','description','status']
    success_url = reverse_lazy('task_list')  # redirect to task list page

class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task_delete'
    success_url = reverse_lazy('task_list')  # redirect to task list page






