from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tour
from .forms import BookingForm


@login_required()
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

