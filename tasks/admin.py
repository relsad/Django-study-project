# Register your models here.
from django.contrib import admin
from .models import User, Employee, Task

# Register custom User model in the admin
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Task)
