from django.shortcuts import render, redirect
from .models import Tour
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


def tours_home(request):
    tours = Tour.objects.all()
    return render(request, 'booking/tours.html', {'tours': tours})


