# from django.contrib import admin
from django.urls import path
from .views import home_page_view
from .views import edit_profile


urlpatterns = [
    path('', home_page_view, name='home'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]
