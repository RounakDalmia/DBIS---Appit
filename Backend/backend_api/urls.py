from django.urls import path, include
from rest_framework import routers
from . import views

# Creating routes for Student, Instructor and University
router = routers.DefaultRouter()

router.register(r'students', views.StudentViewSet)
router.register(r'universities', views.UniversityViewSet)
router.register(r'instructors', views.InstructorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]