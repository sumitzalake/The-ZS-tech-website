from django.contrib.auth.models import User
from django.db import models


class StudentProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    mobile = models.CharField(
        max_length=15,
        blank=True
    )

    education = models.CharField(
        max_length=200,
        blank=True
    )

    profile_photo = models.ImageField(
        upload_to='students/',
        blank=True,
        null=True
    )

    bio = models.TextField(
        blank=True
    )

    github = models.URLField(
        blank=True
    )

    linkedin = models.URLField(
        blank=True
    )

    def __str__(self):

        return self.user.username