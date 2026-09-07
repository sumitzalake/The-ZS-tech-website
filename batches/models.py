from django.db import models
from django.contrib.auth.models import User

from courses.models import Course


class Batch(models.Model):

    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]

    name = models.CharField(max_length=100)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='batches',
    )
    start_date = models.DateField()
    end_date = models.DateField()
    schedule = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    instructor = models.CharField(max_length=150)
    students_count = models.PositiveIntegerField(default=0)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='upcoming',
    )
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Enrollment(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='enrollments',
    )
    batch = models.ForeignKey(
        Batch,
        on_delete=models.CASCADE,
        related_name='enrollments',
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
    )
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'batch')
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} → {self.batch.name}'
