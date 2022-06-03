from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .models import Status

# Create your views here.

class StatusesView(ListView):
    template_name = 'statuses.html'
    model = Status
    context_object_name = 'statuses'