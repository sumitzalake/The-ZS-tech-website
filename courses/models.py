from django.db import models


class Course(models.Model):

    title = models.CharField(
        max_length=200
    )

    short_description = models.CharField(
        max_length=300
    )

    description = models.TextField()

    duration = models.CharField(
        max_length=100
    )

    fees = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.title


class Module(models.Model):

    CATEGORY_CHOICES = [

        ('frontend', 'Frontend'),

        ('database', 'Database'),

        ('backend', 'Backend'),

        ('uiux', 'UI/UX'),

    ]


    course = models.ForeignKey(

        Course,

        on_delete=models.CASCADE,

        related_name='modules'

    )


    title = models.CharField(
        max_length=200
    )


    category = models.CharField(

        max_length=20,

        choices=CATEGORY_CHOICES

    )


    description = models.TextField(
        blank=True
    )


    order = models.PositiveIntegerField(
        default=1
    )


    def __str__(self):

        return self.title


    class Meta:

        ordering = [
            'order'
        ]