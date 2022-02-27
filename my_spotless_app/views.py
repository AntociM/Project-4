from django.shortcuts import render
from django.core import exceptions
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm
from .forms import BookingForm, ContactForm
from .models import Booking, Service


def home_page_view(request):
    context = {}
    return render(request, "index.html", context)


def services_view(request):
    services = Service.objects.all()
    context = {'services': services}
    return render(request, "services.html", context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(data=request.POST, instance=request.user)
        update = form.save(commit=False)
        update.user = request.user
        update.save()
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'profile-edit.html', {'form': form})


def profile_dashboard_view(request):
    context = {
        'user': request.user
    }
    return render(request, "profile-dashboard.html", context)


def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = Booking()
            booking.username = request.user.username
            booking.date = form.cleaned_data['date']
            booking.mentions = form.cleaned_data['mentions']
            booking.service = form.cleaned_data['service']
            booking.save()
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})


def booking_display(request):
    if request.method == 'POST':
        bookings = Booking.objects.all()
        instance = None
        for booking in bookings:
            if str(booking.pk) in request.POST:
                instance = booking
                break

        if instance is None:
            raise exceptions.FieldError()

        form = BookingForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
    
    bookings = Booking.objects.filter(username=request.user)
    bookings_collection = []

    for booking in bookings:
        form = BookingForm(instance=booking)
        bookings_collection.append(
            {
                'form': form,
                'entry': booking
            }
        )

    return render(request, 'profile-dashboard.html', {
        'bookings': bookings_collection
    })


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
