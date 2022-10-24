from re import X
from django.shortcuts import render
from calculator.forms import CandidateForm
from django.views.generic import TemplateView
from multiprocessing import context
from .forms import *
import datetime as dt
import pandas as pd
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .resources import SystemResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse

def index(request):
    
    # Objects and variables:
    form = CandidateForm()
    array_elements = []

    if request.method == "POST":

        print(request.POST)
        form = CandidateForm(request.POST)

        # Save form values to the list:
        if form.is_valid():

            for x in form.cleaned_data:
                array_elements.append(form[x].value())
                
            form.save()
        
    print("ARRAY ELEMENTS")
    print(array_elements)

    # Create output file:
    file = PDF(array_elements=array_elements)
    context = {'form': form}
    return render(request, 'main.html', context)

def redirect_output(request):
    return render(request, 'output.html')


