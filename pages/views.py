from django.shortcuts import render,redirect
from .models import Team
from cars.models import Car
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages


# here are pages views for blizzard.
# Created functions for home, about, services and contact for the urls.

def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct() #distinct() will bring all unique values
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new message from Blizzard Auto regarding ' + subject
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail( # https://docs.djangoproject.com/en/4.1/topics/email/
                email_subject,
                message_body,
                'finfotek80@gmail.com',
                [admin_email],
                fail_silently=False,
            )

        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')


    return render(request, 'pages/contact.html')
