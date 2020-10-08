from .models import Task
from rest_framework.generics import ListCreateAPIView
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status


class TasksViewSet(ListCreateAPIView):

    serializer_class = TaskSerializer

    def get_queryset(self):
        tasks = Task.objects.all()
        return tasks
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)