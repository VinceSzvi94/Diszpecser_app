from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def login_user(request):
    pass
    # if request.method == "POST":
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     # print(username, password)
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         messages.success(request, ("Sikeres bejelentkezés!"))
    #         return render(request, 'home.html', {})
    #     else:
    #         messages.success(request, ("Helytelen felhasználónév vagy jelszó!"))
    #         return render(request, 'login.html', {})
    # else:
    #     return render(request, 'login.html', {})

def logout_user(request):
    pass
    # logout(request)
    # messages.success(request, ("Sikeres kijelentkezés!"))
    # return render(request, 'home.html', {})