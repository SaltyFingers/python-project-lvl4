from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from ..my_mixins import MyLoginRequiredMixin, MyUserPassesTestMixin
from .forms import UserForm
from .models import User


class UsersView(ListView):
    template_name = "users.html"
    model = User
    context_object_name = "users"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Users")
        return context


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = "form.html"
    form_class = UserForm
    success_url = "/login"
    success_message = _("User created successfully!")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Registration")
        context["button_text"] = _("Register")
        return context


class UserUpdateView(SuccessMessageMixin,
                     MyLoginRequiredMixin,
                     MyUserPassesTestMixin,
                     UpdateView):
    model = User
    template_name = "form.html"
    form_class = UserForm
    success_url = "/users"
    success_message = _("User updated successfully!")

    no_permission_url = "/users"
    no_permission_message = _("You do not have rights to changhe another user")

    def test_func(self):
        return self.request.user == self.get_object()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Update user")
        context["button_text"] = _("Update")
        return context


class UserDeleteView(SuccessMessageMixin,
                     MyLoginRequiredMixin,
                     MyUserPassesTestMixin,
                     DeleteView):
    model = User
    template_name = "delete.html"
    success_url = "/users"
    success_message = _("User deleted successfully!")

    no_permission_url = "/users"
    no_permission_message = _("You do not have rights to changhe another user")

    def test_func(self):
        return self.request.user == self.get_object()

    def form_valid(self, form):
        if self.get_object().tasks.all() or self.get_object().works_on.all():
            messages.add_message(
                self.request,
                messages.ERROR,
                _("User can not be deleted because it is in use"),
            )
        else:
            super(UserDeleteView, self).form_valid(form)
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Delete user")
        return context
