from django.urls import path, include
from . import views


urlpatterns = [
    path('list/<str:month_delta>/', views.callist, name='cal'),
    path('<str:date>/', views.showday, name='date'),
]