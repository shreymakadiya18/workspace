from django.contrib import admin

# Register your models here.
# from .models import UserProfile, Project, ProjectMembership, Task
from .models import UserProfile, Project, ProjectMembership, Task,Room,Message

admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(ProjectMembership)
admin.site.register(Task)
admin.site.register(Room)
admin.site.register(Message)
