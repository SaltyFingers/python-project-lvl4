from django.urls import path
from .views import UsersView, UserCreateView, UserUpdateView, UserDeleteView


app_name='users'
urlpatterns = [
    path('', UsersView.as_view()),
    path('create', UserCreateView.as_view(), name='create'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete')
]