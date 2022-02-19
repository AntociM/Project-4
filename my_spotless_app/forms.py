from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomSignupForm(SignupForm):

    
    HOUSING_TYPE = [
        ('ap', 'Apartment'),
        ('condo', 'Condo'),
        ('villa', 'Villa'),
        ('single', 'Single-family'),
        ('mansion', 'Mansion'),
        ('cottage', 'Cottage'),
        ('tiny', 'Tiny House'),
    ]
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    phone = forms.CharField(
        max_length=15, label='Phone number')
    address = forms.CharField(max_length=100, label='Address')
    housing_type = forms.ChoiceField(choices=HOUSING_TYPE)
    surface_sqm=forms.IntegerField()

    

    def signup(self, request, user):
        # user=super(CustomSignupForm, self).save(request)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.save()
        return user
    
    class Meta:
        model = CustomUser
