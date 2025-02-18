from django.urls import path
from . import views

urlpatterns = [
    path('student_projects/', views.student_projects, name='student_projects'),
    path('active_projects/', views.active_projects, name='active_projects'),
    path('submit_project/<int:project_id>/', views.submit_project, name='submit_project'),
    path('student_projects/project_detail/<int:project_id>/', views.project_detail, name='project_detail'),
    path('student_projects/submission/<int:submission_id>/', views.submission_detail, name='submission_detail'),
]