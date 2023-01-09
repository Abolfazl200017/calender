from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.callist, name='cal'),
    path('day=<int:day_num>/', views.showday, name='day_cal')
]