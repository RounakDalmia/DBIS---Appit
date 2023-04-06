from django.urls import path, include
from rest_framework import routers
from . import views

# Creating routes for Student, Instructor and University
router = routers.DefaultRouter()

router.register(r'student', views.StudentViewSet)
router.register(r'univ', views.UniversityViewSet)
router.register(r'instr', views.InstructorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]