# Импортируем функцию path из django.urls для создания URL-маршрутов
from django.urls import path

# Импортируем наши представления (views) для работы со списком студентов и деталями студента
from .views import StudentList, StudentDetail

# urlpatterns - это список всех URL-маршрутов нашего приложения
urlpatterns = [
    # Путь '' (пустая строка) означает корневой URL приложения students/
    # StudentList.as_view() - преобразует наш класс StudentList в представление
    # Этот маршрут будет отображать список всех студентов
    path("", StudentList.as_view()),
    # Путь '<int:pk>/' будет обрабатывать URL вида students/1/, students/2/ и т.д.
    # int:pk означает, что мы ожидаем целое число, которое будет передано в представление как pk (primary key)
    # Этот маршрут будет отображать детальную информацию о конкретном студенте
    path("<int:pk>/", StudentDetail.as_view()),
]
