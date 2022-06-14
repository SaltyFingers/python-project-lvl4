from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import TaskForm
from .models import Task


class TasksView(LoginRequiredMixin, ListView):
    template_name = 'tasks.html'
    model = Task
    context_object_name = 'tasks'

class TaskCreateView(LoginRequiredMixin,
                     SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    model = Task
    form_class = TaskForm
    success_url = '/tasks'
    success_message = _('Task created successfully!')


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Create task')
        context['button_text'] = _('Create')
        return context


class TaskUpdateView(LoginRequiredMixin,
                     SuccessMessageMixin, UpdateView):
    template_name = 'form.html'
    model = Task
    form_class = TaskForm
    success_url = '/tasks'
    success_message = _('Task updated successfully!')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Update task')
        context['button_text'] = _('Update')
        return context


class TaskDeleteView(LoginRequiredMixin,
                     SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = '/tasks'
    success_message = _('Task deleted successfully!')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Delete task')
        return context
