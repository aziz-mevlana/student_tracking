from django.contrib import admin
from .models import ProjectRequest, StudentSubmission

@admin.register(ProjectRequest)
class ProjectRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'deadline', 'created_at')
    list_filter = ('teacher',)

@admin.register(StudentSubmission)
class StudentSubmissionAdmin(admin.ModelAdmin):
    list_display = ('project_request', 'student', 'submitted_at', 'is_approved')
    list_filter = ('project_request', 'is_approved')
    search_fields = ('student__username', 'project_request__title')
