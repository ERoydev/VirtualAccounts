from django.db import models
from django.contrib.auth.models import AbstractUser


class AppUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'  # This makes email the unique identifier for login
    REQUIRED_FIELDS = []

    # Set custom related names to avoid conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='appuser_groups',  # Custom related name for groups
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='appuser_permissions',  # Custom related name for user permissions
        blank=True,
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return self.email