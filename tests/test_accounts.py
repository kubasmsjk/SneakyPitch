from django.test import TestCase
from django.urls import reverse
from accounts.forms import *

class BaseTest(TestCase):
    def setUp(self):
        self.register_url=reverse('register')
        self.login_url=reverse('login')
        self.logout_url=reverse('logout')
        self.user={
            'first_name':'Adam',
            'last_name':'Bonczek',
            'email':'testemail@wp.pl',
            'username':'bonczuras',
            'password1':'marek12345',
            'confirm':'marek12345',
        }
        self.user_wrong_data = {
            'first_name': 'Adam',
            'last_name': 'Bonczek',
            'email': 'temailwp.pl',
            'username': 'bonczuras1',
            'password1': 'pass',
            'confirm': 'pass',
        }
        self.user_wrong_login = {
            'username':'admin',
            'password':'admin',
        }

        return super().setUp()

class RegisterTest(BaseTest):

    def test_can_view_page_correctly(self):
        response=self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'register.html')

    def test_can_register_user(self):
        response=self.client.post(self.register_url, self.user, format='text/html')
        self.assertEqual(response.status_code,200)

    def test_cant_register_user_wrong_data(self):
        self.client.post(self.register_url, self.user_wrong_data, format='text/html')
        form = CustomUserCreationForm(self.user_wrong_data)
        self.assertFalse(form.is_valid())

class LoginTest(BaseTest):

    def test_can_view_page_correctly(self):
        response=self.client.get(self.login_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_cant_login(self):
        response = self.client.post(self.login_url, self.user_wrong_login, format='text/html')
        self.assertEqual(response.status_code, 302)

class LogoutTest(BaseTest):

    def test_can_view_page_correctly(self):
        response=self.client.get(self.logout_url)
        self.assertEqual(response.status_code,302)

