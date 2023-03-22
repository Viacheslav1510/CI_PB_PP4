from django.test import TestCase
from .models import Tour, Booking
from django.contrib.auth.models import User
import datetime


class TestBookingModels(TestCase):
    def setUp(self):
        """
        SetUp function to create user, login and create post
        """
        self.user = User.objects.create_user(
                username='albajessica', email='foo@gmail.com',
                password='bartolito')
        self.user.save()
        self.client.login(username='albajessica', password='bartolito')
        self.tour = Tour.objects.create(
            tour_name='Test tour',
            price=140,
            max_seats=1,
        )
        self.tour.save()
        self.booking = Booking.objects.create(
            user=self.user,
            tour=self.tour,
            name='Tom Cruise',
            email='tom@gmail.com',
            phone='+480684647491',
            tour_date=datetime.date(2023, 4, 15)
        )

    def test_post_string_method_returns_right_string(self):
        booking = self.booking
        string = f"Tour: {self.booking.tour}, name: {self.booking.name}, "
        string += f"date: {self.booking.tour_date}"
        self.assertEqual(
            str(booking),
            string
        )
