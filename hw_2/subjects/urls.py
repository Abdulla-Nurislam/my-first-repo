from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course-list'),
    path('<int:pk>/', views.course_detail, name='course-detail'),
    path('api/', views.CourseListAPI.as_view(), name='course-list-api'),
    path('api/<int:pk>/', views.CourseDetailAPI.as_view(), name='course-detail-api'),
] 