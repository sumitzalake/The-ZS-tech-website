from django.contrib import admin

from .models import Batch


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):

    list_display = (

        'name',

        'course',

        'start_date',

        'end_date',

        'instructor',

        'students_count',

        'status',

    )


    list_filter = (

        'status',

        'course',

    )


    search_fields = (

        'name',

        'instructor',

    )