from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import CreateUserForm
from .models import User


# Create your views here.
class UsersView(ListView):
    template_name = 'users.html'
    model = User
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Users')
        return context

class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    form_class = CreateUserForm
    success_url = '/login'
    success_message = _('User created successfully!')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Registration')
        context['button_text'] = _('Register')
        return context


class UserUpdateView(SuccessMessageMixin,
                     LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'form.html'
    form_class = CreateUserForm
    success_url = '/users'
    success_message = _('User updated successfully!')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Update user')
        context['button_text'] = _('Update')
        return context

class UserDeleteView(SuccessMessageMixin, 
                     LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'delete.html'
    success_url = '/users'
    success_message = _('User deleted successfully!')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Delete user')
        return context
    