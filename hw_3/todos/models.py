from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    due_date = models.DateTimeField(verbose_name='Срок выполнения')
    status = models.BooleanField(default=False, verbose_name='Статус')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
