from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.views import generic
# from django.urls import reverse_lazy
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
        'user':request.user
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
    
