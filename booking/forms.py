# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms
from django.core.validators import MaxValueValidator
import datetime
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Booking
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class DateInput(forms.DateInput):
    """
    A class to provide a calendar widget that the user can
    pick the booking date.
    """
    input_type = 'date'


class BookingForm(forms.ModelForm):
    """
    A class to generate a form from the Booking model
    """

    tour_date = forms.DateField(
        validators=[MaxValueValidator(
            datetime.date.today() + datetime.timedelta(days=30)
        )],
        widget=DateInput(attrs={
            'type': 'date',
            'max': datetime.date.today() + datetime.timedelta(days=30),
            'min': datetime.date.today() + datetime.timedelta(days=1)
            })
        )

    class Meta:
        model = Booking
        fields = ('name', 'phone',
                  'email', 'tour_date')
        widgets = {'date': DateInput()}


class EditBookingForm(forms.ModelForm):
    """
    A class to generate a form for edit booking page
    """
    tour_date = forms.DateField(
        validators=[MaxValueValidator(
            datetime.date.today() + datetime.timedelta(days=30)
        )],
        widget=DateInput(attrs={
            'type': 'date',
            'max': datetime.date.today() + datetime.timedelta(days=30),
            'min': datetime.date.today() + datetime.timedelta(days=1)
            })
        )

    class Meta:
        model = Booking
        fields = ('phone', 'tour', 'tour_date')
        widgets = {'date': DateInput()}
