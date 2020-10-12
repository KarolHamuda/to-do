from .models import Task
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
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

class TaskViewSet(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return task

    def get(self, request, pk):

        task = self.get_queryset(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        
        task = self.get_queryset(pk)
        serializer = TaskSerializer(task, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):

        task = self.get_queryset(pk)
        if request:
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        