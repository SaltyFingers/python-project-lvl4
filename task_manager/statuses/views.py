from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import StatusForm
from .models import Status

# Create your views here.

class StatusesView(ListView):
    template_name = 'statuses.html'
    model = Status
    context_object_name = 'statuses'


class StatusCreateView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    model = Status
    form_class = StatusForm
    success_url = '/statuses'


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    template_name = 'form.html'
    form_class = StatusForm
    success_url = '/statuses'


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'delete.html'
    success_url = '/statuses'
