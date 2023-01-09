from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.callist, name='cal'),
    path('<str:date>/', views.showday, name='date'),
    path('<str:date>/<int:order>', views.todo, name='todo'),
]