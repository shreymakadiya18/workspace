from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Task, UserProfile, ProjectMembership
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('projects')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('project_list')
    else:
        form = AuthenticationForm()
    return render(request, 'projects/login.html', {'form': form})

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('projects')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('project_list')
    else:
        form = UserCreationForm()

    return render(request, 'projects/signup.html', {'form': form})

@login_required
def project_list(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    print(request.user)
    print(request)
    memberships = ProjectMembership.objects.filter(user_profile=user_profile)
    projects = [membership.project for membership in memberships]
    return render(request, 'projects/project_list.html', {'projects': projects})

@login_required
def task_list(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    user_profile = get_object_or_404(UserProfile, user=request.user)
    membership = get_object_or_404(ProjectMembership, user_profile=user_profile, project=project)

    if membership.role == 'Developer':
        tasks = project.tasks.filter(assigned_to=user_profile)
    else:
        tasks = project.tasks.all()
    return render(request, 'projects/task_list.html', {'project': project, 'tasks': tasks})

@login_required
def mark_task_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if task.assigned_to.user == request.user:
        task.status = 'Done'
        task.save()
    return redirect('task_list', project_id=task.project.id)

# def login_view(request):
#     if request.user.is_authenticated:
#         return redirect('projects')
    
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('project_list')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'projects/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
