from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from task_manager.users.forms import CreateUserForm
from task_manager.users.models import User


# Create your views here.
class UsersView(ListView):
    template_name = 'users.html'
    model = User
    context_object_name = 'users'

class UserCreateView(CreateView):
    template_name = 'form.html'
    form_class = CreateUserForm
    success_url = '/login'
    success_message = 'User created successfully!'

class UserUpdateView(UpdateView):
    model = User
    template_name = 'form.html'
    form_class = CreateUserForm
    success_url = '/users'
    success_message = 'User updated successfully!'

class UserDeleteView(DeleteView):
    model = User
    template_name = 'delete.html'
    success_url = '/users'
    
    