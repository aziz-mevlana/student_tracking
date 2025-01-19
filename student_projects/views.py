from django.shortcuts import render, get_object_or_404, redirect
from .models import ProjectRequest, StudentSubmission
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages  # mesajlar için import ekleyin

def student_projects(request):
    projects = ProjectRequest.objects.filter(projects_class=request.user.profile.student_class)
    submission_message = request.session.pop('submission_message', None) # mesajı session'dan al ve sil
    submissions = StudentSubmission.objects.filter(student=request.user)
    approved_submissions = [submission for submission in submissions if submission.is_approved]  # Onaylı projeleri filtrele.
    return render(request, 'student_projects/student_projects.html', {'projects': projects, 
                                                                      'submission_message': submission_message, 
                                                                      'submissions': submissions,
                                                                      'approved_submissions': approved_submissions} )

def active_projects(request):
    current_time = timezone.now()
    active_projects = ProjectRequest.objects.filter(deadline__gte=current_time)
    return render(request, 'student_projects/active_projects.html', {'projects': active_projects})


def submit_project(request, project_id):
    if request.method == 'POST':
        project = get_object_or_404(ProjectRequest, pk=project_id)
        student = request.user
        submission_title_1 = request.POST['title_1']
        submission_description_1 = request.POST['description_1']
        StudentSubmission.objects.create(
            project_request=project,
            student=student,
            submission_title=submission_title_1,
            submission_description=submission_description_1,
            submitted_at=timezone.now()
        )
        submission_title_2 = request.POST['title_2']
        submission_description_2 = request.POST['description_2']
        StudentSubmission.objects.create(
            project_request=project,
            student=student,
            submission_title=submission_title_2,
            submission_description=submission_description_2,
            submitted_at=timezone.now()
        )
        submission_title_3 = request.POST['title_3']
        submission_description_3 = request.POST['description_3']
        StudentSubmission.objects.create(
            project_request=project,
            student=student,
            submission_title=submission_title_3,
            submission_description=submission_description_3,
            submitted_at=timezone.now()
        )
        request.session['submission_message'] = 'Form başarıyla gönderildi!'
        return redirect(reverse('student_projects')) # student_projects'e yönlendir
    return redirect(reverse('student_projects/student_projects'))