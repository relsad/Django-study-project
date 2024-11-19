# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user model with additional role field
class User(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    # Override the groups and user_permissions fields to prevent reverse accessor clash
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='tasks_user_set',  # Unique related name
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='tasks_user_permissions_set',  # Unique related name
        blank=True
    )

    def __str__(self):
        return self.username


# Model for Employee (related to User)
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

# Model for Task
class Task(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return self.title