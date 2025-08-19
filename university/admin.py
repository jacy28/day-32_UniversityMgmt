from django.contrib import admin
from .models import University, Department, Course

# Register your models here.
admin.site.register(University)
admin.site.register(Department)
admin.site.register(Course)