from django.http import HttpResponse
from django.shortcuts import render
from multiprocessing import context
from django.conf import settings
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.clickjacking import xframe_options_sameorigin
from .forms import CandidateForm
from .calculator import Calculator
from .forms import *

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

            # Create an object of the Calculator class, to compute values:
            values = Calculator(array_elements=array_elements) 

            # Create an output file:
            file = PDF(array_elements=array_elements)
                
            form.save()
        
    print("ARRAY ELEMENTS")
    print(array_elements)
    
    context = {'form': form}
    return render(request, 'main.html', context)

def redirect_output(request):
    return render(request, 'output.html')

@xframe_options_exempt
def ok_to_load_in_a_frame(request):
    return HttpResponse("This page is safe to load in a frame on any site.")

@xframe_options_sameorigin
def view_two(request):
    return HttpResponse("Display in a frame if it's from the same origin as me.")
