from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import TaskForm
from .models import Task
from task_manager.users.models import User


class TasksView(ListView):
    template_name = 'tasks.html'
    model = Task
    context_object_name = 'tasks'

class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    model = Task
    form_class = TaskForm
    success_url = '/tasks'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Task
    form_class = TaskForm
    success_url = '/tasks'


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = '/statuses'
