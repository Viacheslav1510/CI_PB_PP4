from django.urls import path
from . import views


urlpatterns = [
    path('tours/', views.tours_home, name='tours'),
    path('bookings/', views.user_bookings, name='bookings')
]
