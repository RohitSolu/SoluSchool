from django.contrib import admin
from .models import Result, Student, Subject, Result, Issuer

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "date_of_birth", "cls","registration_number")
    list_filter = ("name", "date_of_birth", "cls","registration_number")
    search_fields = ("name", "date_of_birth", "cls","registration_number")
    
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("name", "subject")
    list_filter = ("name","subject")
    search_fields = ("name","subject")

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "cls", "subject_code")
    list_filter = ("name", "cls", "subject_code")
    search_fields = ("name", "cls", "subject_code")   

admin.site.register(Issuer)

