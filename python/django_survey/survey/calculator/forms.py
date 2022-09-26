from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm, widgets, TextInput, Select, NumberInput, DateInput
from calculator.models import *
from calculator.views import *

class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'
        
        widgets = {
            'feature_1': Select(attrs={
                'class': 'form-control',
                'style': 
                    'width: 700px;'
                    'background-color: white;'
                    'border: 0;'
                    'box-shadow: rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset;'  
            }, choices={
                ("Feature 1", "Feature 1"),
                ("Feature 2", "Feature 2"),
                ("Feature 3", "Feature 3")
            }),

            'feature_2': Select(attrs={
                'class': 'form-control',
                'style': 
                    'width: 700px;'
                    'background-color: white;'
                    'border: 0;'
                    'box-shadow: rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset;'  
            }, choices={
                ("Feature 1", "Feature 1"),
                ("Feature 2", "Feature 2"),
                ("Feature 3", "Feature 3")
            }),

            'feature_3': TextInput(attrs={
                'class': 'form-control',
                'style': 
                    'width: 700px;'
                    'background-color: white;'
                    'border: 0;'
                    'box-shadow: rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset;'  
            }),

            'feature_4': TextInput(attrs={
                'class': 'form-control',
                'style': 
                    'width: 700px;'
                    'background-color: white;'
                    'border: 0;'
                    'box-shadow: rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset;'  
            }),

            'feature_5': DateInput(attrs={
                'class': 'form-control',
                'style': 
                    'width: 700px;'
                    'background-color: white;'
                    'border: 0;'
                    'box-shadow: rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset;'  
            }),

            'feature_6': TextInput(attrs={
                'class': 'form-control',
                'style': 
                    'width: 700px;'
                    'background-color: white;'
                    'border: 0;'
                    'box-shadow: rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset;'  
            }),

            'feature_7': TextInput(attrs={
                'class': 'form-control',
                'style': 
                    'width: 700px;'
                    'background-color: white;'
                    'border: 0;'
                    'box-shadow: rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset;'  
            }),

            'feature_8': TextInput(attrs={
                'class': 'form-control',
                'style': 
                    'width: 700px;'
                    'background-color: white;'
                    'border: 0;'
                    'box-shadow: rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset;'  
            }),

            'feature_9': TextInput(attrs={
                'class': 'form-control',
                'style': 
                    'width: 700px;'
                    'background-color: white;'
                    'border: 0;'
                    'box-shadow: rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset;'  
            }),

            'feature_10': TextInput(attrs={
                'class': 'form-control',
                'style': 
                    'width: 700px;'
                    'background-color: white;'
                    'border: 0;'
                    'box-shadow: rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset;'  
            }),

            'feature_11': TextInput(attrs={
                'class': 'form-control',
                'style': 
                    'width: 700px;'
                    'background-color: white;'
                    'border: 0;'
                    'box-shadow: rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset;'  
            })

        }
        
        