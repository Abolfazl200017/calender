from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_todo, name='show_todo'),
    path('add/', views.add_todo, name='add_todo'),
    path('edit/', views.edit_todo, name='edit_todo'),
]