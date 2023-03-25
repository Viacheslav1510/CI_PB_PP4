# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestHomeViews(TestCase):
    """
    A class for testing home app views
    """
    def setUp(self):
        """
        SetUp function to create user and login user
        """
        self.user = User.objects.create_user(
            username='albajessica', email='foo@gmail.com',
            password='bartolito')
        self.user.save()
        self.client.login(username='albajessica', password='bartolito')

    def test_get_home_page(self):
        """
        Test to get home page
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_get_contact_page(self):
        """
        Test to get contact page
        """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact-us.html')

    def test_user_can_send_message(self):
        """
        Test to check possibility send message
        """
        response = self.client.post(
            reverse('contact'), {
                'first_name': 'Tom ',
                'last_name': 'Cruise',
                'email': "tom@gmail.com",
                'message': 'I\'m Tom Cruise'
            })
        self.assertEquals(response.status_code, 200)
