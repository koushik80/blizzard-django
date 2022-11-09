from django.test import TestCase
from django.urls import reverse
from .models import Team, Client

# Created tests here.


class HomepageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "pages/home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h5>Come and visit our high-tech performance cars that are made only for you.</h5>")
        self.assertNotContains(response, "Not on the page")

class AboutPageTests(TestCase):  # new
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "pages/about.html")

    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<p>Our team will help you every step of the way during your Blizzard shopping experience.</p>")
        self.assertNotContains(response, "Should not be here!")

class ContactPageTests(TestCase):  # new
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
        self.assertContains(response, "<h5>Phone:</h5>")
        self.assertNotContains(response, "Should not be here!")

class ServicesPageTests(TestCase):  # new
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/services")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("services"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("services"))
        self.assertTemplateUsed(response, "pages/services.html")

    def test_template_content(self):
        response = self.client.get(reverse("services"))
        self.assertContains(response, "<h3>Super Fast</h3>")
        self.assertNotContains(response, "Should not be here!")

# Model tests
class TeamModelTest(TestCase):

    def test_string_representation(self):
        team = Team(first_name = "first name", last_name = "last name")
        self.assertEqual(str(team), team.first_name, team.last_name)

class ClientModelTest(TestCase):

    def test_string_name(self):
        client = Client(name= "Client's name", email = "Client's email address")
        self.assertEqual(str(client), client.name, client.email)
