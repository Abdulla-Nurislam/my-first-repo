# Импортируем необходимые компоненты из Django REST framework
from rest_framework import generics
from .models import Courses
from .serializers import CoursesSerializer


# Представление для списка курсов (GET) и создания нового курса (POST)
class CoursesList(generics.ListCreateAPIView):
    # Получаем все объекты модели Courses
    queryset = Courses.objects.all()
    # Указываем сериализатор для преобразования данных
    serializer_class = CoursesSerializer


# Представление для получения деталей курса (GET), 
# обновления (PUT/PATCH) и удаления (DELETE) конкретного курса
class CoursesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
