from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.new),
    path('shows/create', views.create),
    path('shows/<int:id>', views.details),
    path('shows/<int:id>/edit', views.edit),
    path('shows/<int:id>/destroy', views.delete),
    path('shows/<int:id>/update', views.update),
]