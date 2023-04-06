from django.db import models

# Student model
class Student(models.Model):
    name = models.CharField(max_length=100)
    rollnum = models.IntegerField()
    location = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    university = models.ForeignKey('University', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
# University model
class University(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    country = models.CharField(max_length=100)
    instructors = models.ManyToManyField('Instructor', related_name='university_from_instructor')

    def __str__(self):
        return self.name
    
# Instructor model
class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    university = models.ForeignKey('University', on_delete=models.CASCADE)
    research_area = models.CharField(max_length=100)


    def __str__(self):
        return self.name
