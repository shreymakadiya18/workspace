from django.contrib import admin

# Register your models here.
from .models import UserProfile, Project, ProjectMembership, Task

admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(ProjectMembership)
admin.site.register(Task)
