from django.urls import path, include
from . import views

app_name = 'firstapp'

urlpatterns = [
    path('test', views.index, name='index')
]