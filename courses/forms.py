from django import forms

from .models import Course


INPUT_CLASS = 'form-control'


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title',
            'short_description',
            'description',
            'duration',
            'fees',
            'is_active',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Python Full Stack',
            }),
            'short_description': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'One-line summary for the course card',
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS,
                'rows': 5,
                'placeholder': 'What students will learn',
            }),
            'duration': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': '12 weeks',
            }),
            'fees': forms.NumberInput(attrs={
                'class': INPUT_CLASS,
                'min': '0',
                'step': '0.01',
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }
