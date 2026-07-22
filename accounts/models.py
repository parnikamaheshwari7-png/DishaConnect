from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractUser):

    username = None

    # ---------------------------
    # User Roles
    # ---------------------------
    class Roles(models.TextChoices):
        USER = "USER", "User"
        GUIDE = "GUIDE", "Guide"
        ADMIN = "ADMIN", "Admin"

    # ---------------------------
    # Languages
    # ---------------------------
    class Languages(models.TextChoices):
        ENGLISH = "EN", "English"
        HINDI = "HI", "Hindi"

    # ---------------------------
    # Themes
    # ---------------------------
    class Themes(models.TextChoices):
        LIGHT = "LIGHT", "Light"
        DARK = "DARK", "Dark"
        SYSTEM = "SYSTEM", "System"

    # ---------------------------
    # Guide Approval Status
    # ---------------------------
    class ApprovalStatus(models.TextChoices):
        PENDING = "PENDING", "Pending"
        APPROVED = "APPROVED", "Approved"
        REJECTED = "REJECTED", "Rejected"

    # ---------------------------
    # Basic Information
    # ---------------------------
    role = models.CharField(
        max_length=10,
        choices=Roles.choices,
        default=Roles.USER,
    )

    email = models.EmailField(
        unique=True
    )

    mobile_number = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    # ---------------------------
    # Preferences
    # ---------------------------
    preferred_language = models.CharField(
        max_length=2,
        choices=Languages.choices,
        default=Languages.ENGLISH
    )

    preferred_theme = models.CharField(
        max_length=10,
        choices=Themes.choices,
        default=Themes.SYSTEM
    )

    # ---------------------------
    # Verification
    # ---------------------------
    is_verified = models.BooleanField(
        default=False
    )

    # ---------------------------
    # Guide Approval
    # ---------------------------
    is_approved = models.BooleanField(
        default=True
    )

    approval_status = models.CharField(
        max_length=10,
        choices=ApprovalStatus.choices,
        default=ApprovalStatus.APPROVED
    )

    approved_by = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_guides'
    )

    approved_at = models.DateTimeField(
        null=True,
        blank=True
    )

    rejection_reason = models.TextField(
        blank=True,
        null=True
    )

    # ---------------------------
    # Timestamps
    # ---------------------------
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    # ---------------------------
    # Authentication Settings
    # ---------------------------
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
    
class Expertise(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name
    
class GuideProfile(models.Model):

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="guide_profile"
    )

    expertise = models.ManyToManyField(
        Expertise,
        blank=True
    )

    qualification = models.CharField(
        max_length=255
    )

    experience_years = models.PositiveIntegerField(
        default=0
    )

    bio = models.TextField()

    languages_known = models.CharField(
        max_length=255,
        blank=True
    )

    linkedin_url = models.URLField(
        blank=True,
        null=True
    )

    is_available = models.BooleanField(
        default=True
    )

    max_active_queries = models.PositiveIntegerField(
        default=10
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Guide Profile - {self.user.email}"