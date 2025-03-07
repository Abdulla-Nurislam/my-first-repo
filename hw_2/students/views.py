from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

# Create your views here.

# HTML Views
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})

# API Views
class StudentListAPI(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailAPI(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
