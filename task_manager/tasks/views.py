from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django_filters.views import FilterView

from .forms import FilterTask, TaskForm
from .models import Task


class TasksView(LoginRequiredMixin, FilterView):
    template_name = "tasks.html"
    model = Task
    filterset_class = FilterTask
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Tasks")
        context["button_text"] = _("Show")
        return context


class ViewTaskView(LoginRequiredMixin, DetailView):
    template_name = "view_task.html"
    model = Task
    context_object_name = "task"

    def get_context_data(self, **kwargs):
        context = super(ViewTaskView, self).get_context_data()
        context["labels"] = self.get_object().labels.all()
        return context

class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "form.html"
    model = Task
    form_class = TaskForm
    success_url = "/tasks"
    success_message = _("Task created successfully!")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Create task")
        context["button_text"] = _("Create")
        return context


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "form.html"
    model = Task
    form_class = TaskForm
    success_url = "/tasks"
    success_message = _("Task updated successfully!")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Update task")
        context["button_text"] = _("Update")
        return context


class TaskDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = "delete.html"
    success_url = "/tasks"
    success_message = _("Task deleted successfully!")

    def form_valid(self, form):
        if self.request.user == self.get_object().author:
            super(TaskDeleteView, self).form_valid(form)
        else:
            messages.add_message(self.request, messages.ERROR,
                                 _("Task can only be deleted by it's author!"))
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Delete task")
        return context
