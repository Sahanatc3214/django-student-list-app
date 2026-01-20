from django import forms
from App import models
from App .models import Student

class StudentForm(forms.ModelForm):
    students=Student.objects.all()
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'course', 'skills']