from django.db import models

# Create your models here.

class Student(models.Model):
    studentName = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, null=True )
    grade = models.CharField(max_length=20)

    def __str__(self):
        return([self.studentName, self.gender, self.grade])

class Teacher(models.Model):
    teacherName = models.CharField(max_length=200)
    course = models.CharField(max_length=20)

    def __str__(self):
        return([self.teacherName, self.course])

class Employee(models.Model):
    employeeName = models.CharField(max_length=200)
    job = models.CharField(max_length=20)

    def __str__(self):
        return([self.employeeName, self.job])