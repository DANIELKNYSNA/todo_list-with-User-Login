from typing import Optional
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from base.models import Task
# Create your views here.
class TaskList(ListView):
  model = Task
  context_object_name: Optional[str] = 'tasks'

class TaskDetail(DetailView):
  model = Task
  context_object_name: Optional[str] = 'task'
  template_name: str = 'base/task.html'

