from django.test import TestCase
from django.urls import reverse
# Created my tests here.

class CarsTests(TestCase):  # new
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("cars"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("cars"))
        self.assertTemplateUsed(response, "cars/cars.html")

    def test_template_content(self):
        response = self.client.get(reverse("cars"))
        self.assertContains(response, "<h1>Our Car Inventory</h1>")
        self.assertNotContains(response, "Should not be here!")



class SearchTests(TestCase):  # new
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("search"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("search"))
        self.assertTemplateUsed(response, "cars/search.html")

    def test_template_content(self):
        response = self.client.get(reverse("search"))
        self.assertContains(response, "<h1>Search Results</h1>")
        self.assertNotContains(response, "Should not be here!")





