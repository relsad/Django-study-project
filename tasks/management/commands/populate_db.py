# tasks/management/commands/populate_sample_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from tasks.models import Task, Employee
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Populate database with sample data for testing'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        # Create admin user if it doesn't exist
        if not User.objects.filter(username="admin").exists():
            admin_user = User.objects.create_superuser(username="admin", password="adminpassword", email="admin@example.com")
            admin_user.save()
        else:
            admin_user = User.objects.get(username="admin")

        # Create manager user and associate with Employee instance
        if not User.objects.filter(username="manager").exists():
            manager_user = User.objects.create_user(username="manager", password="managerpassword", email="manager@example.com")
            manager_user.save()

            # Correct assignment: create Employee instance linked to the User
            manager_employee = Employee.objects.create(user=manager_user, position="Manager")
        else:
            manager_user = User.objects.get(username="manager")
            manager_employee = Employee.objects.get(user=manager_user)

        # Create employee1 user and associate with Employee instance
        if not User.objects.filter(username="employee1").exists():
            employee1_user = User.objects.create_user(username="employee1", password="employee1password", email="employee1@example.com")
            employee1_user.save()

            # Correct assignment: create Employee instance linked to the User
            employee1 = Employee.objects.create(user=employee1_user, position="Software Engineer")
        else:
            employee1_user = User.objects.get(username="employee1")
            employee1 = Employee.objects.get(user=employee1_user)

        # Create employee2 user and associate with Employee instance
        if not User.objects.filter(username="employee2").exists():
            employee2_user = User.objects.create_user(username="employee2", password="employee2password", email="employee2@example.com")
            employee2_user.save()

            # Correct assignment: create Employee instance linked to the User
            employee2 = Employee.objects.create(user=employee2_user, position="UI/UX Designer")
        else:
            employee2_user = User.objects.get(username="employee2")
            employee2 = Employee.objects.get(user=employee2_user)

        # Create tasks for employee1 and assign Employee instances (not User)
        task1 = Task.objects.create(
            title="Task 1 for Employee 1",
            description="Complete the backend implementation for the project.",
            assigned_to=employee1,  # Correct: Assign to Employee instance
            deadline=datetime.now() + timedelta(days=5),
            status='PENDING'
        )
        task2 = Task.objects.create(
            title="Task 2 for Employee 1",
            description="Write unit tests for the backend.",
            assigned_to=employee1,  # Correct: Assign to Employee instance
            deadline=datetime.now() + timedelta(days=7),
            status='PENDING'
        )

        # Create tasks for employee2 and assign Employee instances
        task3 = Task.objects.create(
            title="Task 1 for Employee 2",
            description="Design the wireframe for the new feature.",
            assigned_to=employee2,  # Correct: Assign to Employee instance
            deadline=datetime.now() + timedelta(days=3),
            status='PENDING'
        )
        task4 = Task.objects.create(
            title="Task 2 for Employee 2",
            description="Create UI components for the new feature.",
            assigned_to=employee2,  # Correct: Assign to Employee instance
            deadline=datetime.now() + timedelta(days=6),
            status='PENDING'
        )

        # Create task for the manager and assign Employee instance
        task5 = Task.objects.create(
            title="Manager's Task",
            description="Review all team tasks and provide feedback.",
            assigned_to=manager_employee,  # Correct: Assign to Employee instance
            deadline=datetime.now() + timedelta(days=10),
            status='IN_PROGRESS'
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated database with sample data'))
