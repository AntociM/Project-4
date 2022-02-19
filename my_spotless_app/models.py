import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField

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
    user=self._create_user(username, email, password, True, True, **extra_fields)
    return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)


class Member(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, unique=True, null=True, related_name='registered')
    registered = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now=True)

class Membership(models.Model):
    MEMBERSHIP_CHOICES = [
        ('B', 'Basic'),
        ('P', 'Plus'),
        ('U', 'Ultra'),
    ]
    STATUS = ((0, "Inactive"), (1, "Active"))
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default='Basic')
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

class Services(models.Model):
    class Frequency(models.IntegerChoices):
        Weekly = 1
        Bimonnthly = 2
        Monthly = 3
    
    frequency = models.IntegerField(choices=Frequency.choices)
    name = models.CharField(max_length=100)
    duration = models.DurationField()
    services_frequency = models.IntegerField(choices=Frequency.choices)

class Upcoming(models.Model):
    APPROVED = ((0, 'No'), (1, 'Yes'))
    username = models.CharField(max_length=30)
    date = models.DateField(default=datetime.date.today)
    mentions = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    approved = models.IntegerField(choices=APPROVED, default=False)

    class Meta:
        ordering: ['date'] 
    
    def __str__(self):
        return self.mentions

class Contact(models.Model):
    REPLIED = ((0, 'No'), (1, 'Yes'))
    name = models.CharField(max_length=100, null=False, blank=False)
    telephone = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(max_length=50, blank=False, help_text='Email must include "@"')
    message = models.TextField(blank=False, null=False)
    replied = models.IntegerField(choices=REPLIED, default=False)
    created = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)













