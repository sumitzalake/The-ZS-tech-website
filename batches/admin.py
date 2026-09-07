from django.contrib import admin

from .models import Batch, Enrollment


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
    list_filter = ('status', 'course')
    search_fields = ('name', 'instructor')


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'batch', 'status', 'created_at')
    list_filter = ('status', 'batch')
    search_fields = ('user__username', 'user__email', 'batch__name')
    list_editable = ('status',)
