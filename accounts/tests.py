from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class DashboardPageTests(TestCase):  # new
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/accounts/dashboard/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("dashboard"))
        self.assertTemplateUsed(response, "accounts/dashboard.html")

    def test_template_content(self):
        response = self.client.get(reverse("dashboard"))
        self.assertContains(response, "<p>Here are the cars that you have inquired about</p>")
        self.assertNotContains(response, "Should not be here!")



class RegisterPageTests(TestCase):  # new
    def test_url_exists_at_correct_location(self):
        response = self.client.post("/accounts/register/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.post(reverse("register"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.post(reverse("register"))
        self.assertTemplateUsed(response, "accounts/register.html")

    def test_template_content(self):
        response = self.client.post(reverse("register"))
        self.assertContains(response, "<span>Or Login With</span>")
        self.assertNotContains(response, "Should not be here!")