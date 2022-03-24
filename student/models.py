from django.db import models
from django.db.models import Avg
import datetime

CLS_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
)
GRADE_CHOICES = (
    ("A+", "A+"),
    ("A", "A"),
    ("B+", "B+"),
    ("B", "B"),
    ("C+", "C+"),
    ("C", "C"),
    ("D+", "D+"),
    ("D", "D"),
    ("NG", "NG"),
)
CHAR_CHOICES = (
    ("Theory", "Theory"),
    ("Practical", "Practical"),       
)
DESIGNATION_CHOICES = (
    ("Principal", "Principal"),
    ("Vice-Principal", "Vice-Principal"),
    ("Admin", "Admin"),
)

class Student(models.Model):
    name = models.CharField(max_length=255)
    roll_no = models.IntegerField(primary_key=True,default='10')
    registration_number = models.IntegerField(default='111')
    fathers_name = models.CharField(max_length=255)
    mothers_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    cls = models.CharField(max_length=10, choices = CLS_CHOICES, default=10)
    date_of_birth = models.DateField(default=datetime.date.today)
    character_of_student = models.CharField(max_length=50, choices=CHAR_CHOICES, default='Good')
    

    class Meta:
      verbose_name_plural = "students"


    def __str__(self):
        return self.name

    
class Subject(models.Model):
    name = models.CharField(max_length=255)
    cls = models.CharField(max_length=10, choices = CLS_CHOICES, default=10)
    subject_code = models.CharField(max_length=10)
    credit_hour = models.FloatField(max_length=10)
   
    

    def __str__(self):
        return self.name

class Result(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade_point = models.FloatField(max_length=10)
    grade = models.CharField(max_length=10, choices=GRADE_CHOICES, default='A+')
    final_grade = models.CharField(max_length=10, choices=GRADE_CHOICES, default='A+')
    remarks = models.CharField(max_length=40)
    date_of_result = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name.name
    
    

class Issuer(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50, choices= DESIGNATION_CHOICES, default='Principal')
    date_of_issue = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name
    
    