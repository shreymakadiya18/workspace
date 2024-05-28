from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    manager = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='managed_projects')
    
    def __str__(self):
        return self.name

class ProjectMembership(models.Model):
    ROLE_CHOICES = [
        ('Manager', 'Manager'),
        ('Developer', 'Developer'),
    ]
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.role} - {self.project.name}"

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    due_date = models.DateField()
    assigned_to = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='tasks')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    status = models.CharField(max_length=255, choices=[('To Do', 'To Do'), ('In Progress', 'In Progress'), ('Done', 'Done')])

    def __str__(self):
        return self.name
