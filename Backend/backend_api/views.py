from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Instructor, University
from .serializers import StudentSerializer, InstructorSerializer, UniversitySerializer

# Create your api views for Student, Instructor and University here using serializers and models
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer



