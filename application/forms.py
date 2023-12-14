from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

# Regisztrációs űrlap
class DiszpecserCreationForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email cím'}))
    family_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vezetéknév'}))
    given_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Keresztnév'}))
    nev = f'{family_name} {given_name}'
    beosztas = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Beosztás'}))

    # felhasználó (diszpécser) létrehozása user táblában
    class Meta:
        model = Diszpecser
        fields = ('nev', 'email', 'password1', 'password2', 'beosztas')
    
    def __init__(self, *args, **kwargs):
        super(DiszpecserCreationForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Jelszó'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Jelszavának legalább 8 karaktert kell tartalmaznia.</li><li>Jelszava nem állhat csak számokból.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Jelszó megerősítése'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Adja meg jelszavát még egyszer.</small></span>'


# Hivasok rogzitese
class AddHivasForm(forms.ModelForm):
    hivas_kezdete = forms.DateTimeField(required=True, widget=forms.widgets.DateTimeInput(attrs={"placeholder": "Hívás kezdete", "class": "form-control"}), label="")
    hivas_vege = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={"placeholder": "Hívás vége", "class": "form-control"}), label="")
    hivo_telefonszama = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Hívó telefonszáma", "class": "form-control"}), label="")
    hivo_neve = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Hívó neve", "class": "form-control"}), label="")
    telepules = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Település", "class": "form-control"}), label="")
    kozterulet = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Közterület", "class": "form-control"}), label="")
    hazszam = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Házszám", "class": "form-control"}), label="")
    eset_leirasa = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Eset leírása", "class": "form-control"}), label="")

    class Meta:
        model = Hivas
        exclude = ("fogado_diszpecser", "intezkedes_kezdete", "intezkedes_leirasa")


# Intezkedesek rogzitese
class AddIntezkedesForm(forms.ModelForm):
    intezkedes_kezdete = forms.DateTimeField(required=True, widget=forms.widgets.DateTimeInput(attrs={"placeholder": "Intézkedés kezdete", "class": "form-control"}), label="")
    intezkedes_leirasa = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Intézkedés leírása", "class": "form-control"}), label="")

    class Meta:
        model = Hivas
        exclude = ("hivas_kezdete", "hivas_vege", "hivo_telefonszama", "hivo_neve", "telepules", "kozterulet", "hazszam", "eset_leirasa", "fogado_diszpecser")


# Esetek rogzitese
class AddEsetForm(forms.ModelForm):
    eset_kod = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder": "Esetkód", "class": "form-control"}), label="")
    eset_neve = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Esetnév", "class": "form-control"}), label="")
    fontossag = forms.IntegerField(widget=forms.widgets.NumberInput(attrs={"placeholder": "Fontosság", "class": "form-control"}), label="")
    ertesitesi_szint = forms.IntegerField(widget=forms.widgets.NumberInput(attrs={"placeholder": "Értesítési szint", "class": "form-control"}), label="")

    class Meta:
        model = Eset
        exclude = ()

