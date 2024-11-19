from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Task, Employee
from .serializers import TaskSerializer, EmployeeSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_manager:
            return Task.objects.all()  # Managers can see all tasks
        elif user.is_authenticated:
            # Employees can see only their own tasks
            employee = Employee.objects.get(user=user)
            return Task.objects.filter(assigned_to=employee)
        return Task.objects.none()  # No tasks if user is not authenticated

    def perform_create(self, serializer):
        # Allow the manager to assign a task to an employee
        employee = Employee.objects.get(user=self.request.data['assigned_to'])
        serializer.save(assigned_to=employee)


