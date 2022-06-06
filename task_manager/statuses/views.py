from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .models import Status
from .forms import StatusForm

# Create your views here.

class StatusesView(ListView):
    template_name = 'statuses.html'
    model = Status
    context_object_name = 'statuses'


class StatusCreateView(CreateView):
    template_name = 'form.html'
    model = Status
    form_class = StatusForm
    success_url = '/statuses'


class StatusUpdateView(UpdateView):
    model = Status
    template_name = 'form.html'
    form_class = StatusForm
    success_url = '/statuses'


class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'delete.html'
    success_url = '/statuses'