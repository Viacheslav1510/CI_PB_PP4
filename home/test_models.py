from django.test import TestCase
from django.contrib.auth.models import User
from .models import ContactModel


class TestContactModel(TestCase):
    def setUp(self):
        """
        SetUp function to create user, login and create post
        """
        self.user = User.objects.create_user(
                username='albajessica', email='foo@gmail.com',
                password='bartolito')
        self.user.save()
        self.client.login(username='albajessica', password='bartolito')
        self.contact = ContactModel.objects.create(
            user=self.user,
            first_name='Tom ',
            last_name='Cruise',
            email=self.user.email,
            message='I\'m Tom Cruise'
        )

    def test_booking_string_method_returns_right_string(self):
        contact = self.contact
        string = f"{self.contact.first_name} {self.contact.last_name}, "
        string += f"{self.contact.created_date}"
        self.assertEqual(
            str(contact),
            string
        )
