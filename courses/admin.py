from django.contrib import admin

from .models import Course, Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'duration',
        'fees',
        'is_active',
    )


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'course',
        'category',
        'order',
    )

    list_filter = (
        'category',
        'course',
    )