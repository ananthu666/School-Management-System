from django.contrib.auth.models import AbstractUser
from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Custom_User(AbstractUser):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    username=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    def __str__(self):
        return self.username
    
    
    

class Subject(models.Model):
    subname = models.CharField(max_length=100)
    teacher = models.ForeignKey('Custom_User', on_delete=models.CASCADE, null=True, limit_choices_to={'role': 'teacher'})
    class Meta:
        unique_together = ('subname', 'teacher')
    def __str__(self):
        return self.subname

class Mark(models.Model):
    student = models.ForeignKey(Custom_User, on_delete=models.CASCADE,limit_choices_to={'role': 'student'})
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.FloatField(
        validators=[
            MinValueValidator(0.0, message="Mark cannot be less than 0."),
            MaxValueValidator(100.0, message="Mark cannot be greater than 100.")
        ]
    )

    class Meta:
        unique_together = ('student', 'subject')

    def __str__(self):
        return f"{self.student.username} - {self.subject.name}: {self.marks_obtained}"

