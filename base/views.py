from ast import Dict
from typing import Any, Optional
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy

from base.models import Task
# Create your views here.

class CustomLoginView(LoginView):
  template_name: str = 'base/login.html'
  fields = '__all__'
  redirect_authenticated_user: bool = True

  def get_success_url(self) -> str:
    return reverse_lazy('tasks')
  
  
      

class RegisterView(FormView):
  template_name: str = 'base/register.html'
  form_class = UserCreationForm
  success_url: Optional[str] = reverse_lazy('tasks')

  def form_valid(self, form):
    user = form.save()
    if user is not None:
      login(self.request, user)
    return super(RegisterView, self).form_valid(form)

  def get(self,*args: Any, **kwargs: Any):
    if self.request.user.is_authenticated:
      return redirect('tasks')
    return super(RegisterView, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
  model = Task
  context_object_name: Optional[str] = 'tasks'

  def get_context_data(self, **kwargs: Any):
    context = super().get_context_data(**kwargs)
    context['tasks'] = context['tasks'].filter(user=self.request.user)
    context['count'] = context['tasks'].filter(complete=False).count()
    return context

class TaskDetail(LoginRequiredMixin, DetailView):
  model = Task
  context_object_name: Optional[str] = 'task'
  template_name: str = 'base/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
  model = Task
  fields = ['title', 'description', 'complete']
  success_url: Optional[str] = reverse_lazy('tasks')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
  model = Task
  fields = ['title', 'description', 'complete']
  success_url: Optional[str] = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin, DeleteView):
  model = Task
  context_object_name: Optional[str] = 'task'
  success_url: Optional[str] = reverse_lazy('tasks')


  