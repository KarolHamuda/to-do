from django.urls import path, re_path
from to_do import views

urlpatterns = [
    path('tasks/', views.TasksViewSet.as_view(), name='tasks'),
    path('tasks/<uuid:pk>', views.TaskViewSet.as_view(), name='task')
]
