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
    
    form = CandidateForm()
    if request.method == "POST":
        print(request.POST)
        form = CandidateForm(request.POST)

        print (form['feature_1'].value())
        print (form.data['feature_1'])

        if form.is_valid():

            print (form.cleaned_data['feature_1'])
            print (form.instance.feature_1)

            form.save()

    context = {'form': form}
    return render(request, 'main.html', context)

def redirect_output(request):
    return render(request, 'output.html')


