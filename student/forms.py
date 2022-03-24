from dataclasses import fields
from .models import Student, Subject, Result, Issuer
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','roll_no','registration_number','fathers_name','mothers_name','address','cls','date_of_birth','character_of_student']

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=255,label='Search Student:')

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name','cls','subject_code','credit_hour']

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['name','subject','grade_point','grade','final_grade','remarks','date_of_result']

class IssuerForm(forms.ModelForm):
    class Meta:
        model = Issuer
        fields = ['name','designation','date_of_issue']