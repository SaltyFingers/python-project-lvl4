from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import UserForm
from .models import User


# Create your views here.
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


class UserUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = User
    template_name = "form.html"
    form_class = UserForm
    success_url = "/users"
    success_message = _("User updated successfully!")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Update user")
        context["button_text"] = _("Update")
        return context


class UserDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = User
    template_name = "delete.html"
    success_url = "/users"
    success_message = _("User deleted successfully!")

    def form_valid(self, form):
        if self.request.user.id == self.get_object().id:
            super(UserDeleteView, self).form_valid(form)
        else:
            messages.add_message(
                self.request,
                messages.ERROR,
                _("User can only be deleted by himself"),
            )

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
