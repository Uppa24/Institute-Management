from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class StudentData(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    mobile=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    education=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    skills=models.CharField(max_length=200)
    place=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
