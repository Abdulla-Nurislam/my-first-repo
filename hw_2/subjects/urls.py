# Импортируем функцию path из django.urls для создания URL-маршрутов
from django.urls import path
# Импортируем классы представлений CoursesList и CoursesDetail из views.py
from .views import CoursesList, CoursesDetail

# Список URL-маршрутов приложения
urlpatterns = [
    # Маршрут для списка всех курсов
    # Пустой путь "" означает корневой URL приложения subjects/
    # CoursesList.as_view() - преобразует класс-представление в функцию представления
    path("", CoursesList.as_view()),

    # Маршрут для детальной информации о конкретном курсе
    # <int:pk> - это параметр пути, где:
    #   int - указывает, что параметр должен быть целым числом
    #   pk - имя параметра (primary key - первичный ключ)
    # Пример URL: subjects/1/ покажет детали курса с id=1
    path("<int:pk>/", CoursesDetail.as_view()),
]
