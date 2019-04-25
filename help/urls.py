from django.urls import path, re_path
from help import views

urlpatterns = [
    re_path(r'^$', views.help, name='help'),
]