from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm, TextInput, Select, DateInput
from calculator.models import *
from calculator.views import *
from django import forms


class SystemForm(ModelForm):
    class Meta:
        model = System
        fields = '__all__'

class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'
        
        widgets = {
            'feature_1': Select(attrs={
                'class': 'form-control',
                'style': 
                    'font-family: Raleway, sans-serif;'
                    'font-weight: bold;'
                    'width: 700px;'
                    'background-color: rgb(255, 255, 255);'
                    'color:#051937;'
                    'border: 0;'
                    'border-radius: 0px;'
                    'box-shadow: rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset;'  
            }, choices={
                ("PGE EC", "PGE EC"),
                ("PGE EC Oddzial Krakow", "PGE EC Oddział Kraków"),
                ("PGE EC Oddzial Gdansk", "PGE EC Oddział Gdańsk"),
                ("PGE EC Oddzial Szczecin", "PGE EC Oddział Szczecin"),
                ("PGE EC Oddzial Zgierz", "PGE EC Oddział Zgierz"),
                ("PGE EC Oddzial Zielona Gora", "PGE EC Oddział Zielona Góra"),
                ("PGE EC Oddzial Wybrzeze", "PGE EC Oddział Wybrzeże"),
                ("PGE EC Torun", "PGE EC Toruń"),
                ("ZEW Kogeneracja", "ZEW Kogeneracja"),
                ("PGE Paliwa", "PGE Paliwa")
            }),

            'feature_2': Select(attrs={
                'class': 'form-control',
                'style': 
                    'font-family: Raleway, sans-serif;'
                    'font-weight: bold;'
                    'width: 700px;'
                    'background-color: rgb(255, 255, 255);'
                    'color:#051937;'
                    'border: 0;'
                    'border-radius: 0px;'
                    'box-shadow: rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset;'  
            }, choices={
                ("Premia kwartalna", "Premia kwartalna"),
                ("Premia polroczna", "Premia półroczna"),
                ("Premia MBO", "Premia MBO")
            }),

            'feature_3': TextInput(attrs={
                'class': 'form-control',
                'style': 
                    'font-family: Raleway, sans-serif;'
                    'font-weight: bold;'
                    'width: 700px;'
                    'background-color: rgb(255, 255, 255);'
                    'color:#051937;'
                    'border: 0;'
                    'border-radius: 0px;'
                    'box-shadow: rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset;'  
            }),

            'feature_4': TextInput(attrs={
                'class': 'form-control',
                'style': 
                    'font-family: Raleway, sans-serif;'
                    'font-weight: bold;'
                    'width: 700px;'
                    'background-color: rgb(255, 255, 255);'
                    'color:#051937;'
                    'border: 0;'
                    'border-radius: 0px;'
                    'box-shadow: rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset;'  
            }),

            'feature_5': Select(attrs={
                'class': 'form-control',
                'style': 
                    'font-family: Raleway, sans-serif;'
                    'font-weight: bold;'
                    'width: 700px;'
                    'background-color: rgb(255, 255, 255);'
                    'color:#051937;'
                    'border: 0;'
                    'border-radius: 0px;'
                    'box-shadow: rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset;'  
            }, choices={
                ("Mezczyzna", "Mężczyzna"),
                ("Kobieta", "Kobieta")
            }), 

            'feature_6': TextInput(attrs={
                'class': 'form-control',
                'style': 
                    'font-family: Raleway, sans-serif;'
                    'font-weight: bold;'
                    'width: 700px;'
                    'background-color: rgb(255, 255, 255);'
                    'color:#051937;'
                    'border: 0;'
                    'border-radius: 0px;'
                    'box-shadow: rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset;'  
            }),

            'feature_7': TextInput(attrs={
                'class': 'form-control',
                'style': 
                    'font-family: Raleway, sans-serif;'
                    'font-weight: bold;'
                    'width: 700px;'
                    'background-color: rgb(255, 255, 255);'
                    'color:#051937;'
                    'border: 0;'
                    'border-radius: 0px;'
                    'box-shadow: rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset;'  
            }), 

            'feature_8': TextInput(attrs={
                'class': 'form-control',
                'style': 
                    'font-family: Raleway, sans-serif;'
                    'font-weight: bold;'
                    'width: 700px;'
                    'background-color: rgb(255, 255, 255);'
                    'color:#051937;'
                    'border: 0;'
                    'border-radius: 0px;'
                    'box-shadow: rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset;'  
            }),

            'feature_9': TextInput(attrs={
                'class': 'form-control',
                'style': 
                    'font-family: Raleway, sans-serif;'
                    'font-weight: bold;'
                    'width: 700px;'
                    'background-color: rgb(255, 255, 255);'
                    'color:#051937;'
                    'border: 0;'
                    'border-radius: 0px;'
                    'box-shadow: rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset;'  
            }),

            'feature_10': TextInput(attrs={
                'class': 'form-control',
                'style': 
                    'font-family: Raleway, sans-serif;'
                    'font-weight: bold;'
                    'width: 700px;'
                    'background-color: rgb(255, 255, 255);'
                    'color:#051937;'
                    'border: 0;'
                    'border-radius: 0px;'
                    'box-shadow: rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset;'  
            }),

            'feature_11': TextInput(attrs={
                'class': 'form-control',
                'style': 
                    'font-family: Raleway, sans-serif;'
                    'font-weight: bold;'
                    'width: 700px;'
                    'background-color: rgb(255, 255, 255);'
                    'color:#051937;'
                    'border: 0;'
                    'border-radius: 0px;'
                    'box-shadow: rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset;'  
            })

        }
        


