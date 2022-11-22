from django.urls import path
from . import views

# added urls for the car, searching and specification of the car

urlpatterns = [
    path('', views.cars, name='cars'),
    path('<int:id>', views.car_detail, name='car_detail'),
    path('search', views.search, name='search'),
]
