from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('subjects/', include('subjects.urls')),
] 