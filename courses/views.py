from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)

from .forms import CourseForm
from .models import Course


def course_list(request):

    courses = Course.objects.filter(
        is_active=True
    )

    return render(

        request,

        'courses/course_list.html',

        {
            'courses': courses
        }

    )


def course_detail(
    request,
    pk
):

    course = get_object_or_404(
        Course,
        pk=pk
    )

    return render(

        request,

        'courses/course_detail.html',

        {
            'course': course
        }

    )


@login_required
@permission_required('courses.add_course', raise_exception=True)
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, f'{course.title} has been added.')
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseForm()

    return render(
        request,
        'courses/course_form.html',
        {
            'form': form,
        },
    )