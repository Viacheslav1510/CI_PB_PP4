from django import forms
from django.core.validators import MaxValueValidator
import datetime
from .models import Booking


class DateInput(forms.DateInput):
    """This class provides a calendar widget that the user can
    pick the booking date.
    """
    input_type = 'date'


class BookingForm(forms.ModelForm):
    """This class generates a form from the Booking model
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
