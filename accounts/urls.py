from django.urls import path
from . import views

# added urls for authentication and dashboard to display status of registered user or admin after login
urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]
