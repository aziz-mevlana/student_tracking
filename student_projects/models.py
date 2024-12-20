from django.db import models

class ProjectStudents(models.Model):
    projects_title = models.CharField(max_length=50)
    projects_description = models.CharField(max_length=250)
    projects_topic = models.CharField(max_length=250)
    #ogrenci id
    
    
    def __str__(self):
        return self.projects_title
