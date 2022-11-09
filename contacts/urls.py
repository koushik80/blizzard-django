from django.urls import path
from . import views

# Here I added one url for clients inquiry

urlpatterns = [
      path('inquiry', views.inquiry, name='inquiry'),
]