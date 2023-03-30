# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Tour, Booking
from .forms import BookingForm, EditBookingForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def tours_home(request):
    """
    A function to open tour main page
    and provide existent tours
    """
    tours = Tour.objects.all()
    context = {
        'tours': tours,
    }
    return render(request, 'booking/tours.html', context)


@login_required()
def booking(request, tour_id):
    """
    A function to open tour booking page
    and provide booking form
    function checks booking availability
    """
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['tour_date']
            if len(Booking.objects.filter(tour_date=date)) < tour.max_seats:
                booking = form.save(commit=False)
                booking.user = request.user
                booking.tour = tour
                booking.save()
                messages.info(request, "You've booked a trip successfully")
                return redirect('bookings')
            else:
                messages.info(request, "The Selected Day Is Full!")
    else:
        form = BookingForm()
    context = {
        'form': form,
        'tour': tour
    }
    return render(request, 'booking/book-a-trip.html', context)


@login_required()
def user_bookings(request):
    """
    A function to open user bookings page
    and provide already booked trips
    """
    bookings = Booking.objects.filter(user=request.user)
    context = {
        'bookings': bookings,
    }
    return render(request, 'booking/bookings.html', context)


def edit_booking(request, booking_id):
    """
    A function to open edit booking page
    and provide edit booking form
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        form = EditBookingForm(request.POST, instance=booking)
        if form.is_valid():
            date = form.cleaned_data['tour_date']
            if len(Booking.objects.filter(tour_date=date)) < \
                    booking.tour.max_seats:
                form.save()
                messages.info(request, "The booking have been updated")
                return redirect('bookings')
            else:
                messages.info(request, "The Selected Day Is Full!")
    else:
        form = EditBookingForm(instance=booking)
    context = {
        'post': booking,
        'form': form
    }
    return render(request, 'booking/edit-booking.html', context)


def delete_booking(request, booking_id):
    """
    A function to open delete booking confirmation page
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        messages.info(request, "The booking have been deleted")
        return redirect('bookings')
    context = {
        'booking': booking,
    }
    return render(request, 'booking/delete-booking.html', context)
