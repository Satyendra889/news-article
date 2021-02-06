from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:pk>/', views.list_detail),
    path('insert/', views.insert, name='insert')
]