from django.urls import path, re_path
from . import views

urlpatterns = [
  re_path(r'^$', views.Client_list, name='Сlient_list'),
  re_path(r'^client/new/$', views.Client_new, name='Client_new'),
  #re_path(r'^contract/$', views.Contract_list, name='Contract_list'),
  #re_path(r'^imychestvo/$', views.Imychestvo_list, name='Imychestvo(_list'),
]
