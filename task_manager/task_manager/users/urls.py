from django.contrib import admin
from django.urls import path
from task_manager.users.views import UsersView, UserCreateView

urlpatterns = [
    path('', UsersView.as_view()),
    path('/create', UserCreateView.as_view())
]