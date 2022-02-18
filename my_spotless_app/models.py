import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, blank=False, null=False)
    phone = PhoneNumberField(null=False, blank=False)
    username = models.CharField(max_length=30, unique=True)
    housing_type = models.CharField(max_length=200)
    house_sqm = models.IntegerField(default=0)

    def __str__(self):
        return self.username

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













