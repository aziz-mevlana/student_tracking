from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class ProjectRequest(models.Model):
    CLASS_CHOICES = [
        (1, 'Class 1'),
        (2, 'Class 2'),
        (3, 'Class 3'),
        (4, 'Class 4'),
    ]
    img = models.ImageField(default='default_project.jpg', upload_to='project_images/', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)  # Otomatik olarak oluşturulma zamanını alır
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_requests')
    projects_class = models.IntegerField(choices=CLASS_CHOICES, null=True)
    submission_start = models.DateTimeField(null=True, default=datetime(2025, 1, 1))
    
    def __str__(self):
        return self.title
    

class StudentSubmission(models.Model):
    APPROVED_CHOICES = [
        (0, 'Waiting for Approval'),
        (1, 'Approved'),
        (2, 'Not Approved'),
        
    ]
    project_request = models.ForeignKey(ProjectRequest, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    submission_title = models.CharField(max_length=200, null=True)
    submission_description = models.TextField(null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.IntegerField(choices=APPROVED_CHOICES, default=0)

    def save(self, *args, **kwargs):
        if self.is_approved == 1:
            # Öğrencinin diğer gönderimlerini reddet
            StudentSubmission.objects.filter(student=self.student, project_request=self.project_request).exclude(pk=self.pk).update(is_approved=2)
        super(StudentSubmission, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"Submission by {self.student.username} for {self.project_request.title}"
    