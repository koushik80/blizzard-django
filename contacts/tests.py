from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class ContactTests(TestCase):  # new
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/contact")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("contact"))
        self.assertTemplateUsed(response, "pages/contact.html")

    def test_template_content(self):
        response = self.client.get(reverse("contact"))
        self.assertContains(response, "<h5>Email:</h5>")
        self.assertNotContains(response, "Should not be here!")