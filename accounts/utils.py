from .models import StudentProfile


def get_or_create_student_profile(user):
    profile, _ = StudentProfile.objects.get_or_create(user=user)
    return profile
