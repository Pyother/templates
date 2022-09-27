import datetime
from django.db import models
from django.utils import timezone


class Candidate(models.Model):

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

    array_elements = [feature_1, feature_2, feature_3, feature_4, feature_5, 
    feature_6, feature_7, feature_8, feature_9, feature_10, feature_11]

    def display(self):
        return self.array_elements

class Choice(models.Model):
    question = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

