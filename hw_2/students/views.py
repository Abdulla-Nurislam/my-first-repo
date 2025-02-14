from rest_framework import generics
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer


# Добавляем функцию для рендеринга главной страницы
def index(request):
    # Получаем всех студентов из базы данных
    students = Student.objects.all()
    # Передаем их в шаблон
    return render(request, "students/index.html", {"students": students})


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
