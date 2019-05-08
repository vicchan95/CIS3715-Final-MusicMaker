from django.urls import path

from . import views

app_name = 'generators'
urlpatterns = [
    path('', views.DetailView.as_view(), name = 'generator')
]