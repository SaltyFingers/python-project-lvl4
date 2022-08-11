# from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class LoginView(SuccessMessageMixin, LoginView):
    template_name = "form.html"
    success_message = _("Successfully logged in!")
    next_page = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Sing in")
        context["button_text"] = _("Log in")
        return context


class LogoutView(LogoutView):
    next_page = "/"

    def dispatch(self, request, *args, **kwargs):
        messages.add_message(request, messages.INFO,
                             _("Successfully logged out!"))
        return super().dispatch(request, *args, **kwargs)
