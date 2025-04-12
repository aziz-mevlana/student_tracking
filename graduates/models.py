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
    name = models.CharField(max_length=50, verbose_name="Adı")
    surname = models.CharField(max_length=50, verbose_name="Soyadı")
    img = models.ImageField(upload_to="graduates", verbose_name="Fotoğraf")
    graduation_date = models.DateField(verbose_name="Mezuniyet Tarihi")
    description = models.TextField(verbose_name="Açıklama")
    email = models.EmailField(verbose_name="Email")
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True)
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE, verbose_name="Kategori") # CASCADE #SET_DEFAULT

    # Sosyal medya hesapları
    linkedin = models.URLField(blank=True, null=True, verbose_name="LinkedIn")
    github = models.URLField(blank=True, null=True, verbose_name="GitHub")
    twitter = models.URLField(blank=True, null=True, verbose_name="Twitter")
    instagram = models.URLField(blank=True, null=True, verbose_name="Instagram")
    website = models.URLField(blank=True, null=True, verbose_name="Web Sitesi")
    
    # CV dosyası
    cv_file = models.FileField(upload_to="cv_files", blank=True, null=True, verbose_name="CV Dosyası")
    
    def save(self, *args, **kwarhs):
        self.slug = slugify(self.name + "-" + self.surname) #!!!!!!!!!!!!!!! calisiyor ama Stirng
        super().save(*args, **kwarhs)
    
    def __str__(self):
        return f"{self.name} {self.surname}"
    
    class Meta:
        verbose_name = "Mezun Öğrenci"
        verbose_name_plural = "Mezun Öğrenciler"
        ordering = ['-graduation_date', 'name']
    
    
