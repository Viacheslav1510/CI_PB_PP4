from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tour, Booking
from .forms import BookingForm, EditBookingForm


def tours_home(request):
    tours = Tour.objects.all()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_form = form.save(commit=False)
            booking_form.user = request.user
            booking_form.save()
            return redirect('home')
        else:
            messages.error(request, "Please enter correct data")
            return render(request, 'booking/tours.html', {'form': form})
    else:
        form = BookingForm()
    context = {
        'tours': tours,
        'form': form
    }
    return render(request, 'booking/tours.html', context)


@login_required()
def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    context = {
        'bookings': bookings,
    }
    return render(request, 'booking/bookings.html', context)


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        form = EditBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('bookings')
    else:
        form = EditBookingForm(instance=booking)
    context = {
        'post': booking,
        'form': form
    }
    return render(request, 'booking/edit-booking.html', context)