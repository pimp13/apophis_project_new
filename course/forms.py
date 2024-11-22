from django import forms
from .models import Course

class CourseFilterForm(forms.Form):
    search = forms.CharField(
        required=False,
        max_length=200,
        label='جستجو'
    )
