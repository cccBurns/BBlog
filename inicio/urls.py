from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:pk>', views.post, name="post"),
    path('form_post/', views.formulario, name="formPost")
]