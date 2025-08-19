from django.db import models

# Create your models here.
class University(models.Model):
    name=models.CharField(max_length=255)
    location=models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Department(models.Model):
    university=models.ForeignKey(University, related_name='departments', on_delete=models.CASCADE)
    name=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.university}"
    
class Course(models.Model):
    department=models.ForeignKey(Department, related_name='courses', on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    credits=models.IntegerField()

    def __str__(self):
        return f"{self.title} - {self.department.name}"