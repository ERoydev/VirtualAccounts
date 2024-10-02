from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser

# I need to create my UserManager to handle missing username because i want to use Email as username
class AppUserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

class AppUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

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

    # I assign the custom userManager
    objects = AppUserManager()

    def __str__(self):
        return self.email