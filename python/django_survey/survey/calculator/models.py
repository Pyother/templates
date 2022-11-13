from django.db import models
from django.utils import timezone
from .output import PDF

class Candidate(models.Model):

    # All features required in form:
    feature_1 = models.CharField('Pracodawca:', max_length=100)
    feature_2 = models.CharField('System wynagradzania:', max_length=100)
    feature_3 = models.CharField('Imię:', max_length=100)
    feature_4 = models.CharField('Nazwisko:', max_length=100)
    feature_5 = models.CharField('Płeć:', max_length=100)
    feature_6 = models.CharField('Proponowane wynagrodzenie zasadnicze (PLN):', max_length=100)
    feature_7 = models.DateField('Przewidywana data zatrudnienia:', default='01/01/2023')
    feature_8 = models.CharField('Dodatek funkcyjny:', max_length=100)
    feature_9 = models.CharField('Imię rekrutera:', max_length=100, default='Name')
    feature_10 = models.CharField('Nazwisko rekrutera:', max_length=100, default='Surname')
    feature_11 = models.CharField('E-mail rekrutera:', max_length=100, default='rec@site.com')
    
    # Function displaying features:
    def display(self):
        return self.array_elements

class Choice(models.Model):
    question = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

class System(models.Model):

    employer = models.CharField("Employer", max_length=100)
    substract = models.CharField("Substract", max_length=100)
    system = models.CharField("System", max_length=100)
    value = models.FloatField("Value", max_length=100)
    border_date = models.CharField("Border date", max_length=100)
    basis = models.CharField("Basis", max_length=100, default="Wynagrodzenie zasadnicze")
    comment = models.CharField("Comment", max_length = 160)

    tab = [employer, substract, system, value, border_date, comment]

    def display(self):
        return self.tab