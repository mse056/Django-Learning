from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.sey_hello),
    path('', views.home, name='home'),
    path('Todo/', views.all_Todos, name='Todos'),
    path('detail/<int:todo_id>/', views.detail, name='details'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('update/<int:todo_id>/', views.update, name='update'),
    path('create/', views.create),
]