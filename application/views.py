from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import *


def home(request):
    # check to see if logging in
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, ("Sikeres bejelentkezés!"))
            return redirect('home')
        else:
            messages.success(request, ("Helytelen felhasználónév vagy jelszó!"))
            return redirect('home')

    else:
        return render(request, 'home.html', {})


# def login_user(request):
#     pass


def logout_user(request):
    logout(request)
    messages.success(request, ("Sikeres kijelentkezés!"))
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ("Sikeres regisztráció!"))
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
