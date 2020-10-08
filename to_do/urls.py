from django.urls import path
from to_do import views

urlpatterns = [
    path('tasks/', views.TasksViewSet.as_view(), name='tasks'),
]
