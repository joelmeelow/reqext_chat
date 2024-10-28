# models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.db.models.signals import post_save
from django.db.models import F
from display.models import Items  # Ensure this import matches your structure

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, username=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    username = models.CharField(max_length=100, verbose_name="username")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


class pharmauser(models.Model):
    """Pharmacist model that references the User model."""
    pharmacist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    title = models.CharField(max_length=15, verbose_name="pharmacist title")
    experience = models.IntegerField(default=1)
    specialization = models.CharField(max_length=300, default=None, verbose_name="pharmacist specialization")
    pharm_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    """Profile for users that may include payment information."""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)


class CountQueryset(models.QuerySet):
    def with_counts(self):
        return self.order_by('-count')


class PharmacistClicked(models.Model):
    """Tracks the number of clicks on each pharmacist by users."""
    pharmacist = models.ForeignKey(pharmauser, on_delete=models.CASCADE)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    objects = CountQueryset.as_manager()

    def __str__(self):
        return f'{self.pharmacist} clicked by {self.client}'

    @classmethod
    def increment_click_count(cls, pharmauser, user):
        """Increment the click count for a pharmacist by a user."""
        count = cls.objects.filter(pharmacist=pharmauser, client=user)
        if count.exists():
            count.update(count=F('count') + 1)
        else:
            cls.objects.create(pharmacist=pharmauser, client=user, count=1)
