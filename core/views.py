from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm
from courses.models import Course
from batches.models import Batch


def home(request):
    context = {
        'students': 500,
        'batches': 15,
        'projects': 50,
        'internships': 100,
        'certificates': 350,
        'featured_courses': Course.objects.filter(is_active=True)[:3],
        'open_batches': Batch.objects.exclude(status='completed')[:3],
    }
    return render(request, 'core/home.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Thanks! We received your message and will reply soon.',
            )
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})
