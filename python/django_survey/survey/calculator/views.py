from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("C A L C U L A T O R")
