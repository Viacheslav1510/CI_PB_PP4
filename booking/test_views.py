from django.test import TestCase
from django.urls import reverse
from .models import Tour, Booking
from .forms import EditBookingForm
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
import datetime


class TestBookingViews(TestCase):
    """
    A class for testing booking views
    """

    def setUp(self):
        """
        SetUp function to create user, login and create tour and booking
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

    def test_get_tours_home_page(self):
        """
        Test to get tours main page
        """
        response = self.client.get('/tours/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/tours.html')

    def test_get_book_a_tour_page(self):
        """
        Test to get booking page
        """
        id = self.tour.id
        response = self.client.get(reverse('book-trip', args=[id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/book-a-trip.html')

    def test_get_edit_booking_page(self):
        """
        Test to get edit booking page
        """
        id = self.booking.id
        response = self.client.get(reverse('edit-booking', args=[id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/edit-booking.html')

    def test_get_delete_booking_page(self):
        """
        Test to get delete booking page
        """
        id = self.booking.id
        response = self.client.get(reverse('delete-booking', args=[id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/delete-booking.html')

    def test_user_can_book_tour(self):
        """
        Test to check user able to book a trip
        """
        id = self.tour.id
        response = self.client.post(
            reverse('book-trip', args=(id,)), {
                'name': 'Tom Cruise',
                'phone': '+480684647491',
                'email': "tom@gmail.com",
                'tour_date': datetime.date(2023, 4, 16)
            })
        self.assertRedirects(response, '/bookings/')
        self.assertEquals(response.status_code, 302)

    def test_user_can_edit_booking(self):
        """
        Test to check booking update
        """
        id = self.booking.id
        response = self.client.post(
            reverse('edit-booking', args=[id]), {
                'phone': '+480684647492',
                'tour': 1,
                'tour_date': datetime.date(2023, 4, 17)
            })
        self.assertEquals(response.status_code, 302)
        self.booking.refresh_from_db()
        self.assertEquals(self.booking.phone, '+480684647492')

    def test_can_delete_booking(self):
        """
        Test to delete booking
        """
        id = self.booking.id
        response = self.client.post(reverse('delete-booking',
                                    args=[id]))
        self.assertRedirects(response, reverse('bookings'), status_code=302)

    def test_can_show_message_date_is_full_create_booking_page(self):
        """
        Test to check is message shown on booking creation page
        when date to book is full
        """
        id = self.tour.id
        response = self.client.post(
            reverse('book-trip', args=(id,)), {
                'name': 'Tom Cruise',
                'phone': '+480684647491',
                'email': "tom@gmail.com",
                'tour_date': datetime.date(2023, 4, 15)
            })
        self.assertEquals(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)

    def test_can_show_message_date_is_full_edit_booking_page(self):
        """
        Test to check is message shown on booking update page
        when date to book is full
        """
        id = self.booking.id
        response = self.client.post(
            reverse('edit-booking', args=[id]), {
                'phone': '+480684647492',
                'tour': 1,
                'tour_date': datetime.date(2023, 4, 15)
            })
        self.assertEquals(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
