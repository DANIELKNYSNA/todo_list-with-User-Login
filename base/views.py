from typing import Optional
from django.shortcuts import render
from django.views.generic.list import ListView

from base.models import Task
# Create your views here.
class TaskList(ListView):
  model = Task
  context_object_name: Optional[str] = 'tasks'

  
