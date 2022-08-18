from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from ..my_mixins import MyLoginRequiredMixin
from .forms import LabelForm
from .models import Label


# Create your views here.
class LabelsView(MyLoginRequiredMixin, ListView):
    template_name = "labels.html"
    model = Label
    context_object_name = "labels"


class LabelCreateView(MyLoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "form.html"
    model = Label
    form_class = LabelForm
    success_url = "/labels"
    success_message = _("Label created successfully!")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Create label")
        context["button_text"] = _("Create")
        return context


class LabelUpdateView(MyLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    template_name = "form.html"
    form_class = LabelForm
    success_url = "/labels"
    success_message = _("Label updated successfully!")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Update label")
        context["button_text"] = _("Update")
        return context


class LabelDeleteView(MyLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Label
    template_name = "delete.html"
    success_url = "/labels"
    success_message = _("Label deleted successfully!")

    def form_valid(self, form):
        if self.get_object().tasks.all():
            messages.add_message(
                self.request,
                messages.ERROR,
                _("Label can not be deleted because it is in use"),
            )
        else:
            super(LabelDeleteView, self).form_valid(form)
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Delete label")
        return context
