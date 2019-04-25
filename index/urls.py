from django.urls import path, re_path
from index import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
]