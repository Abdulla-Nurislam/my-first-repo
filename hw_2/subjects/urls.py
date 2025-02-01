from django.urls import path
from .views import CoursesList, CoursesDetail

urlpatterns = [
    path('', CoursesList.as_view()),
    path('<int:pk>/', CoursesDetail.as_view()),
]
