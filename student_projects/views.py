from django.shortcuts import render
from student_projects.models import ProjectStudents



def student_projects(request):
    context = {
        "student_projects": ProjectStudents.objects.all()
    }
    return render(request, "student_projects/student_projects.html", context)