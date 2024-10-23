from django.shortcuts import render
from .models import Task
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskSerializer
from rest_framework import status
# Create your views here.


class TaskCreate(APIView):
    def get(self, request):
        task_objects = Task.objects.all()
        serialize_data = TaskSerializer(task_objects, many=True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)


    def post(self, request):
        serialize_objects = TaskSerializer(data=request.data)
        if serialize_objects.is_valid():
            # Save the objects to the database
            serialize_objects.save()
            return Response(serialize_objects.data, status=status.HTTP_201_CREATED)
        return Response(
            serialize_objects.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, *args, **kwargs):
        task_instance = Task.objects.filter(pk=self.kwargs['pk']).first()
        print(task_instance, 'working')
        # serialize_data = TaskSerializer(data=task_instance)
        serialize_data = TaskSerializer(instance=task_instance, data=request.data)

        if serialize_data.is_valid():
            serialize_data.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, *args, **kwargs):
        task_instance = Task.objects.filter(pk=self.kwargs['pk']).first()
        print(task_instance, 'working')
        serialize_data = TaskSerializer(instance=task_instance, data=request.data)
        # serialize_data = TaskSerializer(data=task_instance)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)