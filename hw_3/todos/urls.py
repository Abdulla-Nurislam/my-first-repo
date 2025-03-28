from django.urls import path
from . import views

urlpatterns = [
    path('', views.todos_list, name='todos_list'),
    path('todo/<int:pk>/', views.todo_detail, name='todo_detail'),
    path('todo/create/', views.todo_create, name='todo_create'),
    path('todo/<int:pk>/delete/', views.todo_delete, name='todo_delete'),
    path('todo/<int:pk>/toggle/', views.toggle_status, name='toggle_status'),
] 