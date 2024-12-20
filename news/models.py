from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class News(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to="news")
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True)
    
    def __str__(self):
        return f"{self.title}" #objeyi title ile adlandirir
    
    def save(self, *args, **kwarhs):
        self.slug = slugify(self.title)
        super().save(*args, **kwarhs)


class Category(models.Model): #!!!!!!!!!!! uniq
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True)

    def __str__(self):
        return f"{self.name}" #objeyi title ile adlandirir
    
    def save(self, *args, **kwarhs):
        self.slug = slugify(self.name)
        super().save(*args, **kwarhs)

    
