from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Djangoban a tablakat a ORM-en keresztül lehet kezelni
# Diszpecser tablahoz a djangoba beepitett User objektumot kell atalakitani egyeni celokra
# A felhasznalokat kezelo Diszpecser osztalyhoz kell egy Manager osztaly is
class DiszpecserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("Nem adott meg helyes email címet")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(username, email, password, **extra_fields)


class Diszpecser(AbstractBaseUser, PermissionsMixin):
    azonosito = models.AutoField(auto_created=True, primary_key=True)
    email = models.EmailField(max_length=254, unique=True)
    nev = models.CharField(max_length=150)
    beosztas = models.CharField(max_length=50, null=True) # NOT NULL a deafult

    objects = DiszpecserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.azonosito}: '+self.nev


# Hivasok tabla intezkedesekkel konszolidalva
# CREATE TABLE hivasok (
#     hivas_id INTEGER PRIMARY KEY,
#     hivas_kezdete DATETIME NOT NULL,
#     hivas_vege DATETIME,
#     hivo_telefonszama VARCHAR(20) NOT NULL,
#     hivo_neve VARCHAR(150),
#     telepules VARCHAR(100),
#     kozterulet VARCHAR(100),
#     hazszam VARCHAR(20),
#     eset_leirasa VARCHAR(500),
#     intezkedes_kezdete DATETIME NOT NULL,
#     intezkedes_leirasa VARCHAR(300)
#     fogado_diszpecser VARCHAR(30) REFERENCES diszpecser.azonosito ON DELETE NO ACTION);
class Hivas(models.Model):
    hivas_id = models.BigAutoField(auto_created=True, primary_key=True)
    hivas_kezdete = models.DateTimeField(),
    hivas_vege = models.DateTimeField(null=True),
    hivo_telefonszama = models.CharField(max_length=20)
    hivo_neve = models.CharField(max_length=150, null=True)
    telepules = models.CharField(max_length=100, null=True)
    kozterulet = models.CharField(max_length=100, null=True)
    hazszam = models.CharField(max_length=20, null=True)
    eset_leirasa = models.CharField(max_length=500, null=True)
    intezkedes_kezdete = models.DateTimeField()
    intezkedes_leirasa = models.CharField(max_length=300, null=True)
    fogado_diszpecser = models.ForeignKey(Diszpecser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.hivas_id}: {self.hivo_telefonszama} {self.hivas_kezdete}-kor'


# Esetek tabla
# CREATE TABLE esetek (
#     esetkod INTEGER PRIMARY KEY,
#     esetnev VARCHAR(40) NOT NULL,
#     fontossag INTEGER NOT NULL,
#     ertesitesi_szint INTEGER NOT NULL);
class Eset(models.Model):
    esetkod = models.IntegerField(primary_key=True)
    esetnev = models.CharField(max_length=60)
    fontossag = models.IntegerField()
    ertesitesi_szint = models.IntegerField()

    def __str__(self):
        return f'{self.esetkod}: {self.esetnev}'


# IntezkedesEsetek tabla
# CREATE TABLE intezkedes_esetek (
#     hivas_id INTEGER REFERENCES hivasok(hivas_id),
#     esetkod INTEGER REFERENCES esetek(esetkod));
class IntezkedettEsetek(models.Model):
    hivas_id = models.ForeignKey(Hivas, on_delete=models.CASCADE)
    esetkod = models.ForeignKey(Eset, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.hivas_id}: {self.esetkod}'
