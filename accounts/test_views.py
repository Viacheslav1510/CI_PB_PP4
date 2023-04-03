# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.urls import reverse
from django.contrib import auth
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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
        """
        Test to get logout confirmation page
        """
        response = self.client.get('/confirmation/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/logout.html')

    def test_get_logout_confirm_second_page(self):
        """
        Test to get logout confirmation page
        """
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

    def test_that_user_gets_logged_in(self):
        """
        Test to log in user
        """
        response = self.client.post(
            reverse('accounts-register'), {
                        'username': "Hulk",
                        'email': 'hulk@gmail.com',
                        'password1': 'qwerty6922',
                        'password2': 'qwerty6922',
                    })
        response = self.client.post(
            reverse('accounts-login'), {
                'username': 'Hulk',
                'password': 'qwerty6922',
                'remember_me': False,
            })
        user = auth.get_user(self.client)
        assert user.is_authenticated

    def test_can_logout(self):
        """
        Test to log out user
        """
        response = self.client.post(
            reverse('logout-confirmation'),
            {'logout': True})
        self.assertRedirects(response, '/')
