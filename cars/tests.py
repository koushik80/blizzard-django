from django.test import TestCase
from django.urls import reverse, resolve
from .models import Car
from .views import cars, search

# Created url and functions tests here.

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

    def test_car_design_isresolved(self):
        url = reverse('cars')
        self.assertEqual(resolve(url).func, cars)
class SearchTests(TestCase):
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

    def test_car_search_isresolved(self):
        url = reverse('search')
        self.assertEqual(resolve(url).func, search)

# Car model test

class CarModelTest(TestCase):

    def test_string_car_title(self):
        title = Car(car_title = "Cars shape", features = "Cars Specs")
        self.assertEqual(str(title), title.car_title, title.features)



