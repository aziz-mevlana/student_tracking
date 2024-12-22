from django.db import models
from django.contrib.auth.models import User

class ProjectRequest(models.Model):
    CLASS_CHOICES = [
        (1, 'Class 1'),
        (2, 'Class 2'),
        (3, 'Class 3'),
        (4, 'Class 4'),
        (5, 'Class 5'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_requests')
    projects_class = models.IntegerField(choices=CLASS_CHOICES, null=True)

    def __str__(self):
        return self.title

class StudentSubmission(models.Model):
    project_request = models.ForeignKey(ProjectRequest, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    submission_title = models.CharField(max_length=200, null=True)
    submission_description = models.TextField(null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Submission by {self.student.username} for {self.project_request.title}"