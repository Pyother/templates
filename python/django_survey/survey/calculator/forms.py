from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from calculator.models import Candidate

class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'