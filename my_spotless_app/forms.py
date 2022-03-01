from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import CustomUser
from .models import Booking
from .models import Contact
from .models import Service


class DateInput(forms.DateInput):
    input_type = 'date'

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    password = None
    HOUSING_TYPE = [
        ('ap', 'Apartment'),
        ('condo', 'Condo'),
        ('villa', 'Villa'),
        ('single', 'Single-family'),
        ('mansion', 'Mansion'),
        ('cottage', 'Cottage'),
        ('tiny', 'Tiny House'),
    ]
    housing_type = forms.ChoiceField(choices=HOUSING_TYPE)

    class Meta:
        model = CustomUser
        fields = ('username',  'first_name', 'last_name', 'email',
                  'phone', 'address', 'housing_type', 'surface_sqm')


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
        max_length=12, label='Phone number')
    address = forms.CharField(max_length=100, label='Address')
    city = forms.CharField(max_length=60, label='City')
    postcode = forms.CharField(max_length=5, label='Postcode')
    housing_type = forms.ChoiceField(choices=HOUSING_TYPE)
    surface_sqm = forms.IntegerField(validators=[MinValueValidator(20), MaxValueValidator(500)])

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone = self.cleaned_data['phone']
        user.address = self.cleaned_data['address']
        user.city = self.cleaned_data['city']
        user.postcode = self.cleaned_data['postcode']
        user.housing_type = self.cleaned_data['housing_type']
        user.surface_sqm = self.cleaned_data['surface_sqm']
        user.save()
        return user

    class Meta:
        model = CustomUser


class ServiceModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class BookingForm(forms.ModelForm):
    service = ServiceModelChoiceField(queryset=Service.objects.all())

    class Meta:
        model = Booking
        fields = ['service', 'date', 'mentions']
        widgets = {
            'date': DateInput(),
        }


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'telephone', 'title', 'message']
