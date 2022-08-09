from django import forms
from .models import Task
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from task_manager.users.models import User
from django.utils.translation import gettext_lazy as _
import django_filters


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "status", "description", "executor", "labels"]
        labels = {
            "id": _("id"),
            "name": _("Name"),
            "description": _("Description"),
            "status": _("Status"),
            "executor": _("Executor"),
            "labels": _("Labels"),
        }


class FilterTask(django_filters.FilterSet):

    all_statuses = Status.objects.values_list("id", "name").all()
    status = django_filters.filters.ChoiceFilter(
        label=_("Status"), choices=all_statuses
    )

    all_executors = User.objects.values_list("id", "username").all()
    executor = django_filters.filters.ChoiceFilter(
        label=_("Executor"), choices=all_executors
    )

    all_labels = Label.objects.values_list("id", "name").all()
    labels = django_filters.filters.ChoiceFilter(label=_("Labels"),
                                                 choices=all_labels)

    self_filter = django_filters.filters.BooleanFilter(
        label=_("Only my taks"),
        widget=forms.CheckboxInput(),
        method="filter_my_tasks"
        )

    def filter_my_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        else:
            return queryset

    class Meta:
        model = Task
        fields = ["status", "executor", "labels"]
