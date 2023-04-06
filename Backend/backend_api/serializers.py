from rest_framework import serializers
from .models import Student, Instructor, University


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'student_id', 'location', 'email', 'phone', 'university')
    

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('univ_id', 'name', 'location', 'email', 'country', 'instructors')

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ('name', 'email', 'phone', 'university', 'research_area')

