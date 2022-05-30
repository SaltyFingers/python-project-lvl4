# from django.shortcuts import render
from multiprocessing import context
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginView(LoginView):
    template_name = 'form.html'
    success_message = 'Successfully logged in'
    next_page = 'index'
    pass


class LogoutView(LogoutView):
    
    def dispatch(self, request, *args, **kwargs):
        messages.add_message(request, messages.INFO, 'Вышли')
        return super().dispatch(request, *args, **kwargs)
