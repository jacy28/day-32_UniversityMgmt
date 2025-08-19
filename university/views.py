from rest_framework import viewsets
from .models import University, Department, Course
from .serializers import UniversitySerializer, DepartmentSerializer, CourseSerializer

class UniversityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows universities to be viewed or edited.
    """
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows departments to be viewed or edited.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        """
        If accessed via nested route under a university, filter by university_id
        """
        university_id = self.kwargs.get('university_pk')
        if university_id:
            return self.queryset.filter(university_id=university_id)
        return self.queryset

class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
