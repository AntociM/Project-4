from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm
from .forms import BookingForm
from .models import Booking


def home_page_view(request):
    context = {}
    return render(request, "index.html", context)

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
            booking.service_type = form.cleaned_data['service_type']
            booking.save()
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})

def booking_display(request):
    bookings = Booking.objects.filter(username=request.user). only('username', 'date', 'service_type', 'mentions', 'approved')

    booking_forms = []

    for booking in bookings:
        form = BookingForm(instance=booking)
        # form.service_type = booking.service_type
        # form.date = booking.date
        # form.mentions = booking.mentions
        booking_forms.append(form)

    return render(request, 'profile-dashboard.html', {
        'bookings': bookings,
        'booking_forms': booking_forms
    })
