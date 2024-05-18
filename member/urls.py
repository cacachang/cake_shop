from django.urls import path
from . import views
from .views import (UserListView, UserCreateView, UserUpdateView, UserDeleteView)

urlpatterns = [
    path('users/', views.index, name="index"),
    path('users/<int:id>/', views.show, name="show"),
    path('users/new/', UserCreateView.as_view(), name="new"),
    path('users/<int:id>/edit/', UserUpdateView.as_view(), name="edit"),
    path('users/<int:id>/delete/', UserDeleteView.as_view(), name="delete"),
]
