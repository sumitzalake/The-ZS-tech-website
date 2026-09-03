from django.shortcuts import render


def home(request):

    context = {
        'students': 500,
        'batches': 15,
        'projects': 50,
        'internships': 100,
        'certificates': 350,
    }

    return render(
        request,
        'core/home.html',
        context
    )