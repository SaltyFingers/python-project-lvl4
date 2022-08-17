from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import StatusForm
from .models import Status

# Create your views here.


class StatusesView(LoginRequiredMixin, ListView):
    template_name = "statuses.html"
    model = Status
    context_object_name = "statuses"


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "form.html"
    model = Status
    form_class = StatusForm
    success_url = "/statuses"
    success_message = _("Status created successfully!")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Create status")
        context["button_text"] = _("Create")
        return context


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    template_name = "form.html"
    form_class = StatusForm
    success_url = "/statuses"
    success_message = _("Status updated successfully!")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Update status")
        context["button_text"] = _("Update")
        return context


class StatusDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = "delete.html"
    success_url = "/statuses"
    success_message = _("Status deleted successfully!")

    def form_valid(self, form):
        if self.get_object().tasks.all():
            messages.add_message(
                self.request,
                messages.ERROR,
                _("Status can not be deleted because it is in use"),
            )
        else:
            super(StatusDeleteView, self).form_valid(form)

        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Delete status")
        return context
