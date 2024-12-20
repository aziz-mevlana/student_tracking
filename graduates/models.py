from django.db import models
from django.utils.text import slugify

class Category(models.Model): #!!!!!!!!!uniq
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True)

    def __str__(self):
        return f"{self.name}" #objeyi title ile adlandirir
    
    def save(self, *args, **kwarhs):
        self.slug = slugify(self.name)
        super().save(*args, **kwarhs)
        
        
        
        
class GraduatingStudents(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    img = models.ImageField(upload_to="graduates")
    graduation_date = models.DateField()
    description = models.TextField()
    email = models.EmailField()
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True)
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE) # CASCADE #SET_DEFAULT

    #sosyal medya hesaplari
    #cv
    def save(self, *args, **kwarhs):
        self.slug = slugify(self.name + "-" + self.surname) #!!!!!!!!!!!!!!! calisiyor ama Stirng
        super().save(*args, **kwarhs)
    
    def __str__(self):
        return self.name
    
    
