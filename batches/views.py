from django.shortcuts import (
    render,
    get_object_or_404
)

from .models import Batch


def batch_list(request):

    batches = Batch.objects.select_related(
        'course'
    ).all()

    return render(

        request,

        'batches/batch_list.html',

        {
            'batches': batches
        }

    )


def batch_detail(
    request,
    pk
):

    batch = get_object_or_404(
        Batch,
        pk=pk
    )

    return render(

        request,

        'batches/batch_detail.html',

        {
            'batch': batch
        }

    )