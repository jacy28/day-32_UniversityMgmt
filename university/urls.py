from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import UniversityViewSet, DepartmentViewSet, CourseViewSet

# Base router
router = DefaultRouter()
router.register(r"universities", UniversityViewSet, basename="university")
router.register(r"courses", CourseViewSet, basename="course")

# Nested router for departments under universities
university_router = NestedDefaultRouter(router, r"universities", lookup="university")
university_router.register(r"departments", DepartmentViewSet, basename="university-departments")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(university_router.urls)),
]
