from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (CreateView,
                                  DeleteView,
                                  DetailView,
                                  UpdateView)
from django_filters.views import FilterView

from ..my_mixins import MyLoginRequiredMixin, MyUserPassesTestMixin
from .forms import FilterTask, TaskForm
from .models import Task


class TasksView(MyLoginRequiredMixin, FilterView):
    template_name = "tasks.html"
    model = Task
    filterset_class = FilterTask
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Tasks")
        context["button_text"] = _("Show")
        return context


class ViewTaskView(MyLoginRequiredMixin, DetailView):
    template_name = "view_task.html"
    model = Task
    context_object_name = "task"

    def get_context_data(self, **kwargs):
        context = super(ViewTaskView, self).get_context_data()
        context["labels"] = self.get_object().labels.all()
        return context


class TaskCreateView(MyLoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "form.html"
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:list")
    success_message = _("Task created successfully!")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Create task")
        context["button_text"] = _("Create")
        return context


class TaskUpdateView(MyLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "form.html"
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:list")
    success_message = _("Task updated successfully!")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Update task")
        context["button_text"] = _("Update")
        return context


class TaskDeleteView(MyLoginRequiredMixin,
                     MyUserPassesTestMixin,
                     SuccessMessageMixin,
                     DeleteView):
    model = Task
    template_name = "delete.html"
    success_url = reverse_lazy("tasks:list")
    success_message = _("Task deleted successfully!")

    no_permission_url = "/tasks"
    no_permission_message = _("Task can only be deleted by it's author!")

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Delete task")
        return context
