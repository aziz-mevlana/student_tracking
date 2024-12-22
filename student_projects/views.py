from django.shortcuts import render, get_object_or_404, redirect
from .models import ProjectRequest, StudentSubmission
from django.utils import timezone
from django.contrib.auth.models import User

def project_request_list(request):
    requests = ProjectRequest.objects.all()
    return render(request, 'student_projects/student_projects.html', {'requests': requests})

def student_projects(request):
    projects = ProjectRequest.objects.all()
    return render(request, 'student_projects/student_projects.html', {'projects': projects})

def active_projects(request):
    current_time = timezone.now()
    active_projects = ProjectRequest.objects.filter(deadline__gte=current_time)
    return render(request, 'student_projects/active_projects.html', {'projects': active_projects})

def submit_project(request, project_id):
    if request.method == 'POST':
        project = get_object_or_404(ProjectRequest, id=project_id)
        student = request.user
        submission_title = request.POST['title']
        submission_description = request.POST['description']
        StudentSubmission.objects.create(
            project_request=project,
            student=student,
            submission_title=submission_title,
            submission_description=submission_description,
            submitted_at=timezone.now()
        )
        return render(request, 'student_projects/student_projects.html', {'success': True})
    return redirect('project_request_list')