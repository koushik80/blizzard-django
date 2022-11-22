from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from contacts.models import Contact


# Created functions for authentication.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

         # condition for matching password & confirm_password
        if password == confirm_password:
            #checking if the username is exist
            if User.objects.filter(username=username).exists(): # here one username from the variable declared and another username form the User model
                messages.error(request, 'Username already exists!')
                return redirect('register')
            else: #checking if the email is exist
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('register')
                else: # if username and email is not exist then user will be logged in will be redirected to the dashboard page
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in.')
                    return redirect('dashboard')
                    user.save()
                    messages.success(request, 'You are registered successfully.')
                    return redirect('login')

        else: # if not than the condition will throw error and will be redirected to register page
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

# user must have to be logged in to access dashboard
@login_required(login_url = 'login')
def dashboard(request): # after successful login user can see their inquiry for the car if the previously send
    user_inquiry = Contact.objects.order_by('-create_date').filter(user_id=request.user.id)

    data = {
        'inquiries': user_inquiry,
    }
    return render(request, 'accounts/dashboard.html', data)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are successfully logged out.')
        return redirect('home')
    return redirect('home')
