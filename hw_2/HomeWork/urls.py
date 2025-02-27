from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.student_list, name='students'),
    path('courses/', views.course_list, name='courses'),
] 