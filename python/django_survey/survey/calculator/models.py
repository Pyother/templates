from django.db import models

class Pracodawca(models.Model):
    nazwa_pracodawcy = models.CharField(max_length=100)

class System(models.Model):
    nazwa_systemu = models.CharField(max_length=100)

class Stanowisko(models.Model):
    nazwa_stanowiska = models.CharField(max_length=100)

class Płeć(models.Model):
    nazwa_płci = models.CharField(max_length=100)

class Wynagrodzenie(models.Model):
    kwota_wynagrodzenia = models.IntegerField(max_length=100)

class DataZatrudnienia(models.Model):
    data_zatrudnienia = models.DateField('data zatrudnienia')

class DodatekFunkcyjny(models.Model):
    nazwa_dodatku = models.CharField(max_length=100)

class Komentarz(models.Model):
    imie_rekrutera = models.CharField(max_length=100)
    nazwisko_rekrutera = models.CharField(max_length=100)
    email_rekrutera = models.CharField(max_length=100)

class DaneKandydata(models.Model):
    imie_kandydata = models.CharField(max_length=100)
    nazwisko_kandydata = models.CharField(max_length=100)



