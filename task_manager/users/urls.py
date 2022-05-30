from django.contrib import admin
from django.urls import path
from task_manager.users.views import UsersView, UserCreateView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('', UsersView.as_view()),
    path('create', UserCreateView.as_view()),
    path('<int:pk>/update', UserUpdateView.as_view()),
    path('<int:pk>/delete', UserDeleteView.as_view())
]