import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField

class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(
            username, email, password, True, True, **extra_fields)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    # TODO add validation
    phone = models.CharField(max_length=12, null=True)
    address = models.CharField(max_length=100, null=True)
    housing_type = models.CharField(max_length=20, null=True)
    surface_sqm = models.IntegerField(null=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

class Service(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, primary_key=True)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='SEK')
    description = models.TextField(blank=False, null=False)
    requisite = models.TextField(blank=False, null=False)
    picture_url = models.TextField(blank=False, null=False)


class Booking(models.Model):
    APPROVED = ((0, 'No'), (1, 'Yes'))

    username = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    mentions = models.TextField(blank=True)
    approved = models.IntegerField(choices=APPROVED, default=False)

    class Meta:
        ordering: ['date']

    def __str__(self):
        return self.mentions


class Contact(models.Model):
    REPLIED = ((0, 'No'), (1, 'Yes'))
    name = models.CharField(max_length=100, null=False, blank=False)
    telephone = PhoneNumberField(null=False, blank=False, unique=False)
    email = models.EmailField(
        max_length=50, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False, default=None)
    message = models.TextField(blank=False, null=False)
    replied = models.IntegerField(choices=REPLIED, default=False)
    created = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)


