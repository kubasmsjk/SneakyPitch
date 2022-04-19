import pytz as pytz
from django.db import models

class Druzyna(models.Model):

    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=20, blank=False, null=True)
    stadion = models.CharField(max_length=20, blank=False, null=True)
    Trener = models.CharField(max_length=30, blank=False, null=True)
    data_zalozenia = models.DateField(blank=False, null=True)

    class Meta:
        verbose_name = "Drużyna"
        verbose_name_plural = "Drużyny"

class Player(models.Model):

    def __str__(self):
        return self.imie +" "+ self.nazwisko

    imie = models.CharField(max_length=30, blank=False, null=True)
    nazwisko = models.CharField(max_length=10, blank=False, null=True)
    data_urodzenia = models.DateField(blank=False, null=True)
    POZYCJA_PILKARZA = [
        ('BR', 'Bramkarz'),
        ('Ob', 'Obrońca'),
        ('Po', 'Pomocnik'),
        ('Na', 'Napastnik'),
    ]
    pozycja = models.CharField(max_length=10, choices=POZYCJA_PILKARZA, blank=False, null=True)
    country = models.CharField(max_length=2, choices=pytz.country_names.items(), null=True)
    ilosc_bramek = models.IntegerField(default=0)

    druzyna = models.ForeignKey(Druzyna, blank=True, on_delete=models.CASCADE, null=True)


    class Meta:
        verbose_name = "Zawodnik"
        verbose_name_plural = "Zawodnicy"

class Mecz(models.Model):

    def __str__(self):
        return str(self.druzynaGospodarzy) + " vs " + str(self.druzynaGosci)

    druzynaGospodarzy = models.ForeignKey(Druzyna, blank=True, on_delete=models.CASCADE, null=True, related_name='gospodarze')
    druzynaGosci = models.ForeignKey(Druzyna, blank=True, on_delete=models.CASCADE, null=True, related_name='goscie')
    data_meczu = models.DateField(blank=False, null=True)
    nr_kolejki = models.IntegerField(null=True)
    wynik_meczu = models.CharField(max_length=5, null=True)

    class Meta:
        verbose_name = "Mecz"
        verbose_name_plural = "Mecze"



