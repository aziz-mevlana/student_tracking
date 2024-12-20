from django.urls import path
from . import views


urlpatterns = [    
    path("student_projects", views.student_projects, name="student_projects"),
 
]