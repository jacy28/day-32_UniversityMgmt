from rest_framework import serializers
from .models import University, Department, Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=['id', 'title', 'credits']

class DepartmentSerializer(serializers.ModelSerializer):
    courses=CourseSerializer(many=True, read_only=True)
    class Meta:
        model=Department
        fields=['id', 'name', 'courses']

class UniversitySerializer(serializers.ModelSerializer):
    departments=DepartmentSerializer(many=True, read_only=True)
    class Meta:
        model=University
        fields=['id', 'name', 'location', 'departments']
