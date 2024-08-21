from django.urls import path
from . import views

urlpatterns = [
    path('', views.foto_list, name='foto_list'),
]