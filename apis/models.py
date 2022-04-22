from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import ValidationError
from django.db import models


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, phone, pincode, address, city, state, country, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        if len(password) < 8:
            raise ValidationError('Password should be at least 8 characters long')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, phone=phone, pincode=pincode, address=address, city=city, state=state,
                          country=country)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, phone, pincode,  password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, phone, pincode, password)

        user.is_superuser = True
        user.is_staff = True

        user.save()
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    pincode = models.CharField(max_length=6)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone', 'pincode']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email


class Content(models.Model):
    """Content created by user"""
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=300)
    summary = models.CharField(max_length=60)
    document = models.URLField()
    categories = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representation of content"""
        return self.title

