from django.contrib import admin

from .models import StudentProfile


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):

    list_display = (

        'user',

        'mobile',

        'education',

    )

    search_fields = (

        'user__username',

        'user__email',

    )