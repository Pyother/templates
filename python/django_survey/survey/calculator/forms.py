from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm, widgets
from calculator.models import *
from calculator.views import *

class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = {'feature_1', 'feature_2', 'feature_3', 'feature_4'}
        widgets = {
            
        }
        
        