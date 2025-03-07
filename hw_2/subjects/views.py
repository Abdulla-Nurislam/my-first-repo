from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer

# Create your views here.

# HTML Views
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'subjects/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'subjects/course_detail.html', {'course': course})

# API Views
class CourseListAPI(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailAPI(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
