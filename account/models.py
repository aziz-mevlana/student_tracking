from django.db import models
from django.contrib.auth.models import User
import random

class Profile(models.Model):
    CLASS_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    token = models.CharField(max_length=6 ,null=True)
    is_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=16, null=True)
    last_name = models.CharField(max_length=16, null=True)
    student_class = models.IntegerField(choices=CLASS_CHOICES, null=True)
    

    def generate_random_token(self):
        # 6 haneli rastgele bir sayı oluştur
        return ''.join(random.choices('0123456789', k=6))

    def save(self, *args, **kwargs):
        # Token alanı boş ise rastgele bir token oluştur
        if not self.token:
            self.token = self.generate_random_token()
        super().save(*args, **kwargs)  # Ana sınıfın save metodunu çağır
    
    
    def __str__(self):
        return f'{self.user.username}'
    