from django.test import TestCase
from django.urls import reverse, resolve
from .models import Contact
from .views import inquiry

# Created tests here.

class ContactTests(TestCase):
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

    def test_inquiry_isresolved(self):
        url = reverse('inquiry')
        self.assertEqual(resolve(url).func, inquiry)

# Contact model test

class ContactModelTest(TestCase):

    def test_string_email(self):
        contact = Contact(email = "Users email address", user_id = "Users ID")
        self.assertEqual(str(contact), contact.email, contact.user_id)