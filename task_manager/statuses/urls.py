from django.urls import path
from .views import StatusesView, StatusCreateView, StatusUpdateView, StatusDeleteView


app_name = "statuses"
urlpatterns = [
    path("", StatusesView.as_view(), name="list"),
    path("create", StatusCreateView.as_view(), name="create"),
    path("<int:pk>/update/", StatusUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", StatusDeleteView.as_view(), name="delete"),
]
