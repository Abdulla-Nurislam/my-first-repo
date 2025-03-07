from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} (Преподаватель: {self.author})"
