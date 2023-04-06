from django.db import models

# Student model
class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='Student Name')
    student_id = models.IntegerField(primary_key=True, verbose_name='Student ID or Roll number')
    location = models.CharField(max_length=100, verbose_name='Student Address')
    email = models.EmailField(max_length=100, verbose_name='Student Email')
    phone = models.IntegerField()
    university = models.ForeignKey('University', on_delete=models.CASCADE, verbose_name='University Name of the student', null=True)

    def __str__(self):
        return self.name
    
# University model
class University(models.Model):
    univ_id = models.IntegerField(primary_key=True, verbose_name='Unique ID of the University')
    name = models.CharField(max_length=100, verbose_name='University Name')
    location = models.CharField(max_length=100, verbose_name='Address of the University')
    email = models.EmailField(max_length=100, verbose_name='Contact email of the university', null=True)
    country = models.CharField(max_length=100, verbose_name='Country where the University is located')
    instructors = models.ManyToManyField('Instructor', related_name='university_from_instructor')

    def __str__(self):
        return self.name
    
# Instructor model
class Instructor(models.Model):
    instr_id = models.IntegerField(primary_key=True, verbose_name='Unique ID of the Instructor')
    name = models.CharField(max_length=100, verbose_name='Instructor Name')
    email = models.EmailField(max_length=100, verbose_name='Email ID of the Instructor')
    phone = models.IntegerField(verbose_name='Phone number of the Instructor')
    university = models.ForeignKey('University', on_delete=models.CASCADE, verbose_name='University Name of the Instructor', null=True)
    research_area = models.CharField(max_length=100, verbose_name='Research Area of the Instructor')

    def __str__(self):
        return self.name
