from django.urls import path
from . import views

urlpatterns = [
    path('', views.go_home, name='home'),
    path('search', views.search_bar, name='search'),
]