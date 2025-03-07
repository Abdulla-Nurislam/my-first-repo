from django.urls import path
from . import views

urlpatterns = [
    # HTML URLs
    path('', views.student_list, name='student-list'),
    path('<int:pk>/', views.student_detail, name='student-detail'),
    
    # API URLs
    path('api/', views.StudentListAPI.as_view(), name='student-list-api'),
    path('api/<int:pk>/', views.StudentDetailAPI.as_view(), name='student-detail-api'),
] 