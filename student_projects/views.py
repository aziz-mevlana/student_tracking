from django.shortcuts import render, get_object_or_404, redirect
from .models import ProjectRequest, StudentSubmission, WeekSubmission
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import timedelta, datetime

def submission_detail(request, submission_id):
    submission = get_object_or_404(StudentSubmission, pk=submission_id)
    return render(request, 'student_projects/student_projects.html', {'submission': submission})

def week_submission(request, submission_id, week_number):
    submission = get_object_or_404(StudentSubmission, pk=submission_id)
    week_submission, created = WeekSubmission.objects.get_or_create(
        submission_request=submission,
        week_number=week_number
    )
    if request.method == 'POST':
        week_submission.submission_link = request.POST['week_submission_link']
        week_submission.submitted_at = timezone.now()
        week_submission.save()
        return redirect('student_projects')  # Başarılı gönderimden sonra yönlendirme
    return render(request, 'student_projects/week_submission_form.html', {'week_submission': week_submission})

def project_detail(request, project_id):
    project = get_object_or_404(ProjectRequest, pk=project_id)
    projects = ProjectRequest.objects.filter(projects_class=request.user.profile.student_class)
    submissions = StudentSubmission.objects.filter(student=request.user)
    approved_submissions = [submission for submission in submissions if submission.is_approved == 1]
    
    return render(request, 'student_projects/student_projects.html', {'project': project,
                                                                    'projects': projects,
                                                                    'approved_submissions': approved_submissions})

def student_projects(request):
    selected_category = request.GET.get('category', None)
    projects = ProjectRequest.objects.filter(projects_class=request.user.profile.student_class)
    submission_message = request.session.pop('submission_message', None)  # mesajı session'dan al ve sil
    submissions = StudentSubmission.objects.filter(student=request.user)
    approved_submissions = [submission for submission in submissions if submission.is_approved == 1]  # Onaylı projeleri filtrele.
    current_time = timezone.now()
    
    # active_week hesaplaması
    active_week = None
    submission_created_at = timezone.now()
    selected_submission = None
    if selected_category:
        try:
            selected_project = ProjectRequest.objects.get(pk=selected_category)
            submission_created_at = selected_project.submission_start
            active_week = (current_time - submission_created_at).days // 7 + 1
        except ProjectRequest.DoesNotExist:
            selected_submission = get_object_or_404(StudentSubmission, pk=selected_category)
            submission_created_at = selected_submission.project_request.submission_start
            active_week = (current_time - submission_created_at).days // 7 + 1

    # submitted_at hesaplaması
    weeks = []
    for week in range(1, 9):
        week_start_date = submission_created_at + timedelta(weeks=week-1)
        week_submission = WeekSubmission.objects.filter(submission_request=selected_submission, week_number=week).first() if selected_submission else None
        week_url = week_submission.submission_link if week_submission else None
        weeks.append({
            'week_url': week_url,
            'week_number': week,
            'submitted_at': week_start_date
        })

    context = {
        'projects': projects,
        'submission_message': submission_message,
        'submissions': submissions,
        'approved_submissions': approved_submissions,
        'selected_category': selected_category,
        'active_week': active_week,  # active_week'i context'e ekleyin
        'weeks': weeks,  # weeks'i context'e ekleyin
    }

    if selected_category:
        try:
            selected_project = ProjectRequest.objects.get(pk=selected_category)
            context['selected_project'] = selected_project
        except ProjectRequest.DoesNotExist:
            selected_submission = get_object_or_404(StudentSubmission, pk=selected_category)
            context['selected_submission'] = selected_submission

    return render(request, 'student_projects/student_projects.html', context)

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
        request.session['submission_message'] = 'Form başarıyla gönderildi!'
        return redirect(reverse('student_projects')) # student_projects'e yönlendir
    return redirect(reverse('student_projects/student_projects'))