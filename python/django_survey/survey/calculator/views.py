from django.shortcuts import render
from django.http import HttpResponse
from calculator.forms import CandidateForm
from django.views.generic import TemplateView
from multiprocessing import context
from .forms import *

def index(request):
    
    form = CandidateForm()
    if request.method == "POST":
        print(request.POST)
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'main.html', context)

def redirect_editor(request):
    return render(request, 'editor.html')
    
class EditorView(TemplateView):
    template_name = 'editor.html'
