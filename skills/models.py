from django.db import models
class Skill(models.Model):
    name = models.CharField(max_length=100)
    description=models.TextField()
    category=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class contactmessage(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject        
    
from django.contrib.auth.models import User


class StudentProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    student_id = models.CharField(max_length=30, unique=True)
    major = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
# Create your models here.
