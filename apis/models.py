from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, phone, pincode, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, phone=phone, pincode=pincode)

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
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
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
