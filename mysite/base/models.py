from django.db import models

# Create your models here.
class Uzytkownicy (models.Model):
    iduzytkownika = models.IntegerField()
    typ = models.IntegerField()
    imie = models.CharField(max_length=250)
    nazwisko = models.CharField(max_length=250)
    miasto = models.CharField(max_length=250)
    numertelefonu = models.IntegerField()
    from_date = models.DateTimeField('od kiedy jest w bazie')


class Autorzy(models.Model):
    idautora = models.IntegerField()
    imie = models.CharField(max_length=250)
    nazwisko = models.CharField(max_length=250)
    numerkontaktowy = models.IntegerField()


class ksiazki(models.Model):
    idksiazki = models.IntegerField()
    nazwa = models.CharField(max_length=250)
    ilosc = models.CharField(max_length=250)
    nrkontakowy = models.IntegerField()
    pub_date = models.DateTimeField('date published')

class Zamowienia(models.Model):
    idzamowienia = models.IntegerField()
    idrodzaj = models.IntegerField()
    datasprzedazy = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    datadoreczenia = models.CharField(max_length=250)
    order_date = models.DateTimeField('date zamowienia')


class Reklamacje(models.Model):
    idreklamacji = models.IntegerField()
    reklamacja_date = models.DateTimeField('data reklamacji')
    status_reklamacji = models.IntegerField()
    decyzja = models.IntegerField()

