from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class UsersView(TemplateView):
    template_name = 'users.html'

class UserCreateView(TemplateView):
    template_name = 'create.html'