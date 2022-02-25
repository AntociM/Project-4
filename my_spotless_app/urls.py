# from django.contrib import admin
from django.urls import path
from .views import home_page_view
from .views import edit_profile
from .views import profile_dashboard_view
from .views import profile_subscription_view


urlpatterns = [
    path('', home_page_view, name='home'),
    path('profile/edit', edit_profile, name='edit_profile'),
    path('profile/dashboard', profile_dashboard_view, name='dashboard_profile'),
    path('profile/subscription', profile_subscription_view, name='subscription_profile'),
]
