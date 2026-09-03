from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from .models import StudentProfile


class RegistrationForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=50
    )

    last_name = forms.CharField(
        max_length=50,
        required=False
    )

    email = forms.EmailField()

    mobile = forms.CharField(
        max_length=15
    )

    education = forms.CharField(
        max_length=200
    )


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


    def save(self, commit=True):

        user = super().save(
            commit=False
        )

        user.first_name = (
            self.cleaned_data['first_name']
        )

        user.last_name = (
            self.cleaned_data['last_name']
        )

        user.email = (
            self.cleaned_data['email']
        )


        if commit:

            user.save()


            StudentProfile.objects.create(

                user=user,

                mobile=self.cleaned_data[
                    'mobile'
                ],

                education=self.cleaned_data[
                    'education'
                ]

            )


        return user