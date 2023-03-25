# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Tour, Booking
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@admin.register(Tour)
class TourModelAdmin(admin.ModelAdmin):
    """
    A class to register Tour Model in admin panel
    and display fields
    """
    list_display = ('tour_name', 'max_seats', 'price')
    search_fields = ['tour_name', 'price']


@admin.register(Booking)
class BookingModelAdmin(admin.ModelAdmin):
    """
    A class to register Booking Model in admin panel
    and display fields
    """
    list_display = ('tour', 'name', 'tour_date', 'created_date')
    search_fields = ['tour__tour_name', 'user__username', 'name', 'tour_date']
