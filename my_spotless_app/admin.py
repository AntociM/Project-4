from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from .models import Service
from .models import Contact
from .models import Booking

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email',]


@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'requisite']
    ordering = ['name', 'price']
    search_fields = ['name']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'replied']
    search_fields = ['name', 'title', 'email', 'telephone', 'message']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['username', 'service', 'date', 'approved']
    list_filter = ['username', 'service', 'date', 'approved']
    search_fields = ['username', 'service']