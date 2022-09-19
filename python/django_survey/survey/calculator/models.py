import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):

    feature_1 = models.CharField(max_length=100)
    feature_2 = models.CharField(max_length=100)
    feature_3 = models.CharField(max_length=100)
    feature_4 = models.CharField(max_length=100)
    feature_5 = models.CharField(max_length=100)
    feature_6 = models.CharField(max_length=100)
    feature_7 = models.DateField('Hiring date')
    feature_8 = models.CharField(max_length=100)
    feature_9 = models.CharField(max_length=100)
    feature_10 = models.CharField(max_length=100)
    feature_11 = models.CharField(max_length=100)


    def publishment(self):
        return self.feature_4 >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

