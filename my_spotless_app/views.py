from django.shortcuts import render
from django.core import exceptions
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm
from .forms import BookingForm, ContactForm
from .models import Booking, Service
from django.contrib import messages
from datetime import datetime


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
            booking_date = datetime.combine(booking.date, datetime.min.time())
            days = (booking_date - datetime.today()).days
            if booking_date <= datetime.today():
                messages.error(
                    request, 'You are trying to'
                    'make a booking on an past date.'
                    'Please choose another date.')
            elif days <= 2:
                messages.error(
                    request, 'You are trying to make'
                    'a booking with one day notice.'
                    'Please choose another date.')
            else:
                messages.success(
                    request, 'Booking completed. Someone will contact you.')
                booking.save()
            # send_booking_confirmation(request.user, booking)

    form = BookingForm()

    return render(request, 'booking.html', {'form': form})


def booking_display(request):
    if request.method == 'POST':
        bookings = Booking.objects.all()
        found_booking = 0
        for booking in bookings:
            if f'update{str(booking.pk)}' in request.POST:
                found_booking = 1
                form = BookingForm(request.POST, instance=booking)
                if form.is_valid():
                    booking_date = datetime.combine(
                        booking.date, datetime.min.time())
                    days = (booking_date - datetime.today()).days

                    # Check if the service has not been changed
                    if 'service' in form.changed_data:
                        messages.error(
                            request, 'You are not allowed'
                            'to change the service type.')
                    elif 'date' in form.changed_data and booking_date <= datetime.today():
                        messages.error(
                            request, 'You are trying to modify an old booking. ')
                    elif 'date' in form.changed_data and days <= 1:
                        messages.error(
                            request, 'You are trying to make a booking with '
                            'one day notice. Please choose another date.')
                    else:
                        form.save()
                        messages.success(
                            request, 'Booking successfully updated!')

                else:
                    messages.error(request, 'Data introduced is invalid')
                    # send_booking_update(request.user, booking)
                break
            if f'delete{str(booking.pk)}' in request.POST:
                # send_booking_cancelation(request.user, booking)
                found_booking = 1
                booking.delete()
                messages.success(request, 'Booking successfully removed!')
                break
        if not found_booking:
            messages.error(
                request, 'Did not find booking. Please contact support!')

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
