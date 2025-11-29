from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as lazy_text

from django.core.validators import FileExtensionValidator
from django.utils import timezone

class MemoTable(models.Model):
    title = models.CharField(max_length=255,
    help_text = 'Memo title (max 25 characters)'
    
    
    )
    description = models.TextField(max_length=255,
        help_text = 'Detailed description of the memo'
    )
    reference_data = models.CharField(
        max_length = 50,
        unique=True,
        db_index=True,
        help_text = 'Reference data (max 50 characters)'
    )
    month = models.CharField(
        max_length=50,
        db_index=True,
        help_text = 'Month of the memo'
    
    )
    year = models.CharField(
        max_length=50,
        db_index = True,
        help_text = 'Year of the memo'
        )
    
    recent = models.BooleanField(
        default=True,
        db_index=True,
        help_text = 'Recent memo'
        
        )  
    file = models.FileField(
        upload_to='pdf/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        help_text="PDF file only, max 10MB"
    )

    created_at = models.DateTimeField(
        auto_now=True,
        help_text='When the nemo was lasted updated'
    )


    updated_at = models.DateTimeField(
        auto_now=True,
        help_text='When the memo was lasted updated'
    )

  
    class Meta:
        db_table = 'memo_table'
        ordering = ['-month']
        verbose_name = 'Memo'
        verbose_name_plural = 'Memo'

        indexes = [
            models.Index(fields=['month', 'year']),
            models.Index(fields=['recent', '-created_at']),
            models.Index(fields=['title']),
        ]

    def __str__(self):
        return f'{self.reference_data} - {self.title}'

    def __repr__(self):
        return f"Memo: {self.reference_data}"

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)




class AdminUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(lazy_text("email address"), unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='employee_id')


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'admin user'
        verbose_name_plural = 'admin users'