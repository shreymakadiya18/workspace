# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.login_view, name='login'),
#     path('signup/', views.signup_view, name='signup'),
#     path('logout/', views.logout_view, name='logout'),
#     path('projects/', views.project_list, name='project_list'),
#     path('projects/<int:project_id>/tasks/', views.task_list, name='task_list'),
#     path('tasks/<int:task_id>/done/', views.mark_task_done, name='mark_task_done'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('projects/', views.project_list, name='project_list'),
    # path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    # path('projects/<int:project_id>/tasks/', views.task_list, name='task_list'),
    path('tasks/<int:task_id>/done/', views.mark_task_done, name='mark_task_done'),
    path('projects/<int:project_id>/add_task/', views.add_task, name='add_task'),
    path('',views.add_task)
]


