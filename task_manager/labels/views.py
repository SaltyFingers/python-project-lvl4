from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Label
from .forms import LabelForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class LabelsView(ListView):
    template_name = 'labels.html'
    model = Label
    context_object_name = 'labels'


class LabelCreateView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    model = Label
    form_class = LabelForm
    success_url = '/labels'


class LabelUpdateView(LoginRequiredMixin, UpdateView):
    model = Label
    template_name = 'form.html'
    form_class = LabelForm
    success_url = '/labels'


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'delete.html'
    success_url = '/labels'
