from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.views import generic
# from django.urls import reverse_lazy
from .forms import CustomUserChangeForm


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
