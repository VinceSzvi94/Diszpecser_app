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
        form = DiszpecserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=email, password=password)
            login(request, user)
            messages.success(request, ("Sikeres regisztráció!"))
            return redirect('home')
    else:
        form = DiszpecserCreationForm()
        return render(request, 'register.html', {'form': form})


def add_hivas(request):
    form = AddHivasForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, ("Hívás sikeresen rögzítve!"))
                return redirect('home')
        return render(request, 'XXX', {'form': form})
    else:
        messages.success(request, ("Kérem jelentkezzen be a hívások rögzítéséhez!"))
        return redirect('home')


# def add_intezkedes(request):
#     form = AddIntezkedesForm(request.POST or None)
#     pass
