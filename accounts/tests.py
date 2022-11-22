from django.test import TestCase
from django.urls import reverse, resolve
from .views import login, register, logout


# Created functions for testing Login and Register here.

class LoginAccountsTests(TestCase):

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/accounts/login")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("login"))
        self.assertTemplateUsed(response, "accounts/login.html")

    def test_template_content(self):
        response = self.client.get(reverse("login"))
        self.assertContains(response, "<h1>Login To Your Account</h1>")
        self.assertNotContains(response, "Should not be here!")

    def test_login_isresolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login)


class RegisterAccountsTests(TestCase):

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/accounts/register")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("register"))
        self.assertTemplateUsed(response, "accounts/register.html")

    def test_template_content(self):
        response = self.client.get(reverse("register"))
        self.assertContains(response, "<h1>Register Your Account</h1>")
        self.assertNotContains(response, "Should not be here!")

    def test_register_isresolved(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register)


class LogoutAccountsTests(TestCase):
    def test_logout_isresolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout)





