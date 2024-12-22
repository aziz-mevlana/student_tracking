from django.urls import path
from . import views

urlpatterns = [
    path('student_projects/', views.student_projects, name='student_projects'),
    path('active_projects/', views.active_projects, name='active_projects'),
    path('submit_project/<int:project_id>/', views.submit_project, name='submit_project'),
]