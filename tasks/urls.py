from django.urls import path
from .views import task_view

urlpatterns = [
    path('task/', task_view, name='task-view'),
]