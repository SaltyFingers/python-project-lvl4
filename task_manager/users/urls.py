from django.urls import path

from .views import UserCreateView, UserDeleteView, UsersView, UserUpdateView

app_name = "users"
urlpatterns = [
    path("", UsersView.as_view(), name="list"),
    path("create/", UserCreateView.as_view(), name="create"),
    path("<int:pk>/update/", UserUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", UserDeleteView.as_view(), name="delete"),
]
