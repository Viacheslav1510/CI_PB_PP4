from django.contrib import admin
from .models import Tour, Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Tour)
class TourModelAdmin(admin.ModelAdmin):
    list_display = ('tour_name', 'price')


@admin.register(Booking)
class BookingModelAdmin(admin.ModelAdmin):
    list_display = ('tour', 'name', 'tour_date', 'created_date')
