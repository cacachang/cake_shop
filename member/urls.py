from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.index, name="index"),
    path('users/<int:id>/', views.show, name="show"),
    path('users/new/', views.new, name="new"),
    path('users/<int:id>/edit/', views.edit, name="edit"),
    path('users/<int:id>/delete/', views.delete, name="delete")
]
