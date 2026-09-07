from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm, ProfileUpdateForm
from batches.models import Enrollment


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Welcome to The ZS-Tech!')
            return redirect('dashboard')
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile(request):
    profile_obj = request.user.studentprofile

    if request.method == 'POST':
        form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=profile_obj,
            user=request.user,
        )
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile_obj, user=request.user)

    return render(
        request,
        'accounts/profile.html',
        {
            'form': form,
            'profile': profile_obj,
        },
    )


@login_required
def dashboard(request):
    enrollments = (
        Enrollment.objects
        .filter(user=request.user)
        .select_related('batch', 'batch__course')
    )
    return render(
        request,
        'accounts/dashboard.html',
        {
            'enrollments': enrollments,
            'profile': request.user.studentprofile,
        },
    )
