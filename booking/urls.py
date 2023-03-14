from django.urls import path
from . import views


urlpatterns = [
    path('tours/', views.tours_home, name='tours'),
    path('book-trip/<int:tour_id>/', views.booking, name='book-trip'),
    path('bookings/', views.user_bookings, name='bookings'),
    path(
        'edit-booking/<int:booking_id>/',
        views.edit_booking,
        name='edit-booking'
    ),
    path(
        'delete-booking/<int:booking_id>/',
        views.delete_booking,
        name='delete-booking'
    ),
]
