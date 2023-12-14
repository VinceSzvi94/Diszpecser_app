from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'), - Bejelentkezes a home page-en
    path('kijelentkezes/', views.logout_user, name='logout'),
    path('regisztracio/', views.register_user, name='register'),
    path('hivasrogzites/', views.add_hivas, name='hivasrogzites'),
    # path('esetek/', views.esetek, name='esetek'),
    # path('lekerdezesek/', views.lekerdezesek, name='lekerdezesek'),
]
