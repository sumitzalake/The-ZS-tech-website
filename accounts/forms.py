from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import StudentProfile


INPUT_CLASS = 'form-control'


class StyledAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': INPUT_CLASS,
            'placeholder': 'Username',
        })
        self.fields['password'].widget.attrs.update({
            'class': INPUT_CLASS,
            'placeholder': 'Password',
        })


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField()
    mobile = forms.CharField(max_length=15)
    education = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'mobile',
            'education',
            'password1',
            'password2',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'username': 'Choose a username',
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Email address',
            'mobile': 'Mobile number',
            'education': 'Education / college',
            'password1': 'Create password',
            'password2': 'Confirm password',
        }
        for name, field in self.fields.items():
            field.widget.attrs['class'] = INPUT_CLASS
            if name in placeholders:
                field.widget.attrs['placeholder'] = placeholders[name]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            StudentProfile.objects.create(
                user=user,
                mobile=self.cleaned_data['mobile'],
                education=self.cleaned_data['education'],
            )

        return user


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField()

    class Meta:
        model = StudentProfile
        fields = [
            'mobile',
            'education',
            'bio',
            'github',
            'linkedin',
            'profile_photo',
        ]
        widgets = {
            'mobile': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'education': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'bio': forms.Textarea(attrs={'class': INPUT_CLASS, 'rows': 4}),
            'github': forms.URLInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'https://github.com/username',
            }),
            'linkedin': forms.URLInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'https://linkedin.com/in/username',
            }),
            'profile_photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['first_name'].initial = user.first_name
        self.fields['last_name'].initial = user.last_name
        self.fields['email'].initial = user.email
        for name in ('first_name', 'last_name', 'email'):
            self.fields[name].widget.attrs['class'] = INPUT_CLASS

    def save(self, commit=True):
        profile = super().save(commit=False)
        user = profile.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile.save()
        return profile
