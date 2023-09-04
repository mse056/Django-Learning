from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.sey_hello),
    path('', views.home),
    path('Todo/', views.all_Todos),
    path('detail/<int:todo_id>/', views.detail)
]