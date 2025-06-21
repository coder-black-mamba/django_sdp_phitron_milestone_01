from django.urls import path
from .views import task_view, manager_dashboard_view, user_dashboard_view

urlpatterns = [
    path('task/', task_view, name='task-view'),
    path('manager-dashboard/', manager_dashboard_view, name='manager-dashboard-view'),
    path('user-dashboard/', user_dashboard_view, name='user-dashboard-view'),
]