from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = "app1"

urlpatterns = [
    path('', views.index, name='index')
]
