# from django.shortcuts import render
from multiprocessing import context
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginView(TemplateView):
    template_name = ''
    pass


class LogoutView(TemplateView):
    template_name = ''
    pass
