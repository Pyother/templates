from django.db import models
from django.utils import timezone
from .output import PDF

class Candidate(models.Model):

    # All features required in form:
    feature_1 = models.CharField('Feature 1:', max_length=100)
    feature_2 = models.CharField('Feature 2:', max_length=100)
    feature_3 = models.CharField('Feature 3 (optional):', max_length=100, blank=True)
    feature_4 = models.CharField('Feature 4 (optional):', max_length=100, blank=True)
    feature_5 = models.CharField('Feature 5 (optional):', max_length=100, blank=True)
    feature_6 = models.CharField('Feature 6:', max_length=100)
    feature_7 = models.DateField('Feature 7:', default='01/01/2023')
    feature_8 = models.CharField('Feature 8:', max_length=100)
    feature_9 = models.CharField('Feature 9 (optional):', max_length=100, blank=True)
    feature_10 = models.CharField('Feature 10 (optional):', max_length=100, blank=True)
    feature_11 = models.CharField('Feature 11 (optional):', max_length=100, blank=True)
    
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