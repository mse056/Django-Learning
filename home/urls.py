from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.sey_hello),
    path('', views.home)
]