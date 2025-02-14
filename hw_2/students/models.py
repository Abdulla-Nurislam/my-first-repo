# Импортируем модуль models из Django, который содержит всё необходимое для создания моделей базы данных
from django.db import models


# Создаём модель Student (студент), которая наследуется от models.Model
# models.Model даёт нашему классу все необходимые функции для работы с базой данных
class Student(models.Model):
    # Определяем поля (свойства) модели Student
    # CharField - это тип поля для хранения текста
    # max_length=100 означает, что текст не может быть длиннее 100 символов
    name = models.CharField(max_length=100)  # Имя студента
    surname = models.CharField(max_length=100)  # Фамилия студента
    major = models.CharField(max_length=100)  # Специальность студента

    # IntegerField - это тип поля для хранения целых чисел
    year_of_study = models.IntegerField()  # Год обучения (например, 1, 2, 3, 4)

    faculty = models.CharField(max_length=100)  # Факультет студента

    # Этот метод определяет, как объект Student будет отображаться в виде строки
    # Например, при выводе в админ-панели Django или при печати объекта
    def __str__(self):
        # Возвращаем строку, которая содержит имя и фамилию студента
        # f"..." - это f-строка, которая позволяет вставлять значения переменных внутрь строки
        return f"{self.name} {self.surname}"
