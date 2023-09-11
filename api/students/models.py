from django.db import models

# Create your models here.

class Student(models.Model):
    first_name: str = models.CharField(max_length=50)
    last_name: str = models.CharField(max_length=50)
    phone_number: str = models.CharField(max_length=15)
    
    #to add subjects__involved

class Subject(models.Model):
    subject_name: str = models.CharField(max_length=50)
    proffessor_name: str = models.CharField(max_length=50)


