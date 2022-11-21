from django.urls import path
from .import views

# here I added my all urls for pages
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),

]

