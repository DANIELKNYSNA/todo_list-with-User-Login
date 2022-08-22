from typing import Optional
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from base.models import Task
# Create your views here.
class TaskList(ListView):
  model = Task
  context_object_name: Optional[str] = 'tasks'

class TaskDetail(DetailView):
  model = Task
  context_object_name: Optional[str] = 'task'
  template_name: str = 'base/task.html'

class TaskCreate(CreateView):
  model = Task
  fields = '__all__'
  success_url: Optional[str] = reverse_lazy('tasks')
  # context_object_name: Optional[str] = 'create'
  # template_name: str = 'base/create.html'