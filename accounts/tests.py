from django.test import TestCase
from django.urls import reverse


# Created Login and Register tests here.

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









