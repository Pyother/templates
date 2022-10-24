from django.shortcuts import render
from multiprocessing import context
from django.conf import settings
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
                
            form.save()
        
    print("ARRAY ELEMENTS")
    print(array_elements)

    # Create an object of the Calculator class, to compute values:
    values = Calculator(array_elements=array_elements) 

    # Create an output file:
    file = PDF(array_elements=array_elements)

    context = {'form': form}
    return render(request, 'main.html', context)

def redirect_output(request):
    return render(request, 'output.html')


