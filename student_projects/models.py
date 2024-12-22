from django.db import models



class ProjectStudents(models.Model):
    CLASS_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, 'G'),
    ]

    projects_title = models.CharField(max_length=50)
    projects_description = models.CharField(max_length=250)
    projects_class = models.IntegerField(choices=CLASS_CHOICES)
    projects_last_date = models.DateField(null=True)
    
    
    
    def __str__(self):
        return self.projects_title
