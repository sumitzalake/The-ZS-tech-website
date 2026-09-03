from django.contrib.auth import login

from django.contrib import messages

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm


def register(request):

    if request.method == 'POST':

        form = RegistrationForm(
            request.POST
        )

        if form.is_valid():

            user = form.save()

            login(
                request,
                user
            )

            messages.success(
                request,
                'Welcome to The ZS-Tech!'
            )

            return redirect('home')

    else:

        form = RegistrationForm()


    return render(
        request,
        'accounts/register.html',
        {
            'form': form
        }
    )


@login_required
def profile(request):

    return render(
        request,
        'accounts/profile.html'
    )