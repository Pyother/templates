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
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'main.html', context)

def redirect_editor(request):
    return render(request, 'editor.html')
    
class EditorView(TemplateView):
    template_name = 'editor.html'

def Import_csv(request):
    print('s')               
    try:
        if request.method == 'POST' and request.FILES['myfile']:
          
            myfile = request.FILES['myfile']        
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print(excel_file) 
            empexceldata = pd.read_csv("."+excel_file,encoding='utf-8')
            print(type(empexceldata))
            dbframe = empexceldata
            for dbframe in dbframe.itertuples():
                 
                fromdate_time_obj = dt.datetime.strptime(dbframe.DOB, '%d-%m-%Y')
                obj = System.objects.create(Empcode=dbframe.Empcode,firstName=dbframe.firstName, middleName=dbframe.middleName,
                                                lastName=dbframe.lastName, email=dbframe.email, phoneNo=dbframe.phoneNo, address=dbframe.address, 
                                                exprience=dbframe.exprience, gender=dbframe.gender, DOB=fromdate_time_obj,
                                                qualification=dbframe.qualification)
                print(type(obj))
                obj.save()
 
            return render(request, 'importexcel.html', {
                'uploaded_file_url': uploaded_file_url
            })    
    except Exception as identifier:            
        print(identifier)
     
    return render(request, 'importexcel.html',{})

def redirect_output(request):
    return render(request, 'output.html')

def simple_upload(request):

    if request.method == 'POST':
        system_resource = SystemResource()
        dataset = Dataset()
        new_system = request.FILES['myfile']

        if new_system.name.endswith('xlsx'):
            messages.info(request, 'Wrong format')
            return render(request, 'upload.html')

        imported_data = dataset.load(new_system.read(), format='xlsx')
        
        for data in imported_data:
            value = System(data[0], data[1], data[2], data[3], data[4], data[5])
            value.save()
    
    return render(request, 'upload.html')

