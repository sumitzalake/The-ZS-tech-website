from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Batch, Enrollment


def batch_list(request):
    batches = Batch.objects.select_related('course').all()
    return render(request, 'batches/batch_list.html', {'batches': batches})


def batch_detail(request, pk):
    batch = get_object_or_404(Batch.objects.select_related('course'), pk=pk)
    enrollment = None

    if request.user.is_authenticated:
        enrollment = Enrollment.objects.filter(
            user=request.user,
            batch=batch,
        ).first()

        if request.method == 'POST':
            if batch.status == 'completed':
                messages.error(request, 'This batch is already completed.')
            elif enrollment:
                messages.info(request, 'You already applied to this batch.')
            else:
                Enrollment.objects.create(
                    user=request.user,
                    batch=batch,
                    note=request.POST.get('note', '').strip(),
                )
                messages.success(
                    request,
                    'Application submitted! Track it on your dashboard.',
                )
                return redirect('dashboard')

            return redirect('batch_detail', pk=batch.pk)

    return render(
        request,
        'batches/batch_detail.html',
        {
            'batch': batch,
            'enrollment': enrollment,
        },
    )
