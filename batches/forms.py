from django import forms

from .models import Batch


INPUT_CLASS = 'form-control'


class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = [
            'name',
            'course',
            'start_date',
            'end_date',
            'schedule',
            'duration',
            'instructor',
            'students_count',
            'status',
            'description',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'April 2026 weekday batch',
            }),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'start_date': forms.DateInput(attrs={
                'class': INPUT_CLASS,
                'type': 'date',
            }),
            'end_date': forms.DateInput(attrs={
                'class': INPUT_CLASS,
                'type': 'date',
            }),
            'schedule': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Mon–Fri, 7:00–9:00 PM',
            }),
            'duration': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': '12 weeks',
            }),
            'instructor': forms.TextInput(attrs={
                'class': INPUT_CLASS,
            }),
            'students_count': forms.NumberInput(attrs={
                'class': INPUT_CLASS,
                'min': '0',
            }),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS,
                'rows': 4,
            }),
        }

    def clean(self):
        cleaned = super().clean()
        start = cleaned.get('start_date')
        end = cleaned.get('end_date')
        if start and end and end < start:
            self.add_error('end_date', 'End date cannot be before the start date.')
        return cleaned
