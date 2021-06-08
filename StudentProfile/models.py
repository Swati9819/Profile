from django.db import models

# Create your models here.
class student_profile(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 70, unique = True)
    branch_of_study = models.CharField(max_length = 50)
    Gender_choices = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = models.CharField(max_length = 1, choices = Gender_choices)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'