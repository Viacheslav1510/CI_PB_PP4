from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestAccountsViews(TestCase):
    """
    A class for testing Accounts app views
    """

    def test_get_sign_up_page(self):
        """
        Test to get sign up page
        """
        response = self.client.get('/sign_up/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/sign_up.html')

    def test_get_logout_confirmation_page(self):
        self.client.login(username='Hulk', password='qwerty6922')
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/logout.html')

    def test_user_can_sign_up(self):
        """
        Test to register user
        """
        response = self.client.post(
            reverse('accounts-register'), {
                        'username': "Hulk",
                        'email': 'hulk@gmail.com',
                        'password1': 'qwerty6922',
                        'password2': 'qwerty6922',
                    })
        self.assertEquals(response.status_code, 302)
